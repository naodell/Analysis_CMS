#include "WeightUtils.h"

WeightUtils::WeightUtils(string sampleName, string dataPeriod, string selection, bool isRealData)
{
    _sampleName = sampleName;
    _dataPeriod = dataPeriod;
    _selection  = selection;
    _isRealData = isRealData;

    Initialize();

    // Muon reco efficiencies
    TFile* f_muRecoSF2012 = new TFile("../data/Muon_ID_iso_Efficiencies_Run_2012ABCD_53X.root", "OPEN"); 

    _muSF2012[0] = (TGraphErrors*)f_muRecoSF2012->Get("DATA_over_MC_combRelIsoPF04dBeta<02_Tight_pt_abseta<0.9_2012ABCD");
    _muSF2012[1] = (TGraphErrors*)f_muRecoSF2012->Get("DATA_over_MC_combRelIsoPF04dBeta<02_Tight_pt_abseta0.9-1.2_2012ABCD");
    _muSF2012[2] = (TGraphErrors*)f_muRecoSF2012->Get("DATA_over_MC_combRelIsoPF04dBeta<02_Tight_pt_abseta1.2-2.1_2012ABCD");
    _muSF2012[3] = (TGraphErrors*)f_muRecoSF2012->Get("DATA_over_MC_HighPt_pt_abseta2.1-2.4_2012ABCD");

    // Electron reco (MVA) efficiencies
    TFile* f_elRecoFile2012 = new TFile("../data/CombinedMethod_ScaleFactors_IdIsoSip.root", "OPEN");
    h2_EleMVASF = (TH2D*)f_elRecoFile2012->Get("h_electronScaleFactor_IdIsoSip");

    // PU weights
    TFile* f_puFile = new TFile("../data/puReweight.root", "OPEN");
    puReweight["2011"]  = (TH1D*)f_puFile->Get("h1_PU");
    puReweight["2012"]  = (TH1D*)f_puFile->Get("h1_PU");

    // weights for fake background
    TFile* f_fakeFile = new TFile("../data/fakeRates_jetCuts.root", "OPEN");
    h2_EleFakes = (TH2D*)f_fakeFile->Get("h2_Fakes_ele_v1");
    h2_MuFakes = (TH2D*)f_fakeFile->Get("h2_Fakes_mu_v1");

}

void WeightUtils::Initialize()
{
    _puWeight = 1.;
    _zzWeight = 1.;
    _vbfWeight = 1.;
    _recoWeight = 1.;
    _triggerWeight = 1.;
}

void WeightUtils::SetDataBit(bool isRealData)
{
    _isRealData = isRealData;
}

void WeightUtils::SetDataPeriod(string dataPeriod)
{
    _dataPeriod = dataPeriod;
}

void WeightUtils::SetSampleName(string sampleName)
{
    _sampleName = sampleName;
}

void WeightUtils::SetSelection(string selection)
{
    _selection = selection;
}

void WeightUtils::SetPassTrigger(string passTrig)
{
    _passTrig = passTrig;
}

void WeightUtils::SetObjects(vector<TCPhysObject> leptons, vector<TCJet> jets, float nPU, string passTrig)
{
    _leptons    = leptons;
    _jets       = jets;
    _passTrig   = passTrig;
    _nPU        = nPU;
}

float WeightUtils::GetTotalWeight()
{
    Initialize();
    float weight = 1.;

    if (!_isRealData) {
        weight *= PUWeight();
        weight *= RecoWeight();
        //if (_sampleName.compare(0,2,"ZZ") == 0) weight *= ZZWeight(leptons);
    } 
    //cout << _nPU << ", " << weight << endl;

    return weight;
}

float WeightUtils::PUWeight()
{
    if (puReweight.count(_dataPeriod) != 0)
        _puWeight = puReweight[_dataPeriod]->GetBinContent(puReweight[_dataPeriod]->FindBin(_nPU)); 
    else
        _puWeight = 1.;

    return _puWeight;
}

float WeightUtils::RecoWeight()
{
    _triggerWeight = 1.;
    _recoWeight    = 1.;

    for (vector<TCPhysObject>::const_iterator iLep = _leptons.begin(); iLep != _leptons.end(); ++iLep) {
        if (iLep->Type() == "muon") {
            _triggerWeight *= GetMuTriggerEff((TLorentzVector)*iLep);
            _recoWeight    *= GetMuEff((TLorentzVector)*iLep);
        }
        if (iLep->Type() == "electron") {
            _triggerWeight *= 0.995;
            _recoWeight    *= GetElectronEff((TLorentzVector)*iLep);
        }
        //cout << iLep->Type() << ", " << _recoWeight << "\t";
    }

    if (_leptons.size() != 2) _triggerWeight = 1.;

    //cout << endl;


    return _triggerWeight*_recoWeight;
}

float WeightUtils::ZZWeight(vector<TLorentzVector> leptons)
{
    float zPt = (leptons[0] + leptons[1]).Pt();
    _zzWeight = 0.12 + (1.108 + 0.002429*zPt - (1.655e-6)*pow(zPt, 2));  
    return _zzWeight;
}


float WeightUtils::VBFHiggsWeight(float genMass, int higgsMass)
{
    _vbfWeight = float(higgsMass)/genMass;
    return _vbfWeight;
}

float WeightUtils::GetMuTriggerEff(TLorentzVector lep) const
{
    //float trigEff[4][4]; 
    int etaBin  = 0;
    int ptBin   = 0;
    float weight = 1.;
    float etaBins[] = {0., 0.8, 1.2, 2.1, 2.4};
    float ptBins[]  = {20., 30., 40., 50., 1e5};

    for (int i = 0; i < 4; ++i) {
        if (fabs(lep.Eta()) > etaBins[i] && fabs(lep.Eta()) <= etaBins[i+1]) {
            etaBin = i;
            break;
        }
    }
    for (int i = 0; i < 4; ++i) {
        if (lep.Pt() > ptBins[i] && lep.Pt() <= ptBins[i+1]) {
            ptBin = i;
            break;
        }
    }

    return weight; //trigEff[etaBin][ptBin];
}

float WeightUtils::GetElectronEff(TLorentzVector lep) const
{
    /*
    // Scale factors based for 2012 8 TeV data (53X) for tight muon selection
    float eleScale[5][6] = {
    {0.818, 0.928, 0.973, 0.979, 0.984, 0.983},
    {0.840, 0.914, 0.948, 0.961, 0.972, 0.977},
    {1.008, 0.877, 0.983, 0.983, 0.957, 0.978},
    {0.906, 0.907, 0.957, 0.962, 0.985, 0.986},
    {0.991, 0.939, 1.001, 1.002, 0.999, 0.995}
    };

    int ptBin  = 0;
    int etaBin = 0;
    float ptBins[]  = {10., 15., 20., 30., 40., 50., 9999.};
    float etaBins[] = {0., 0.8, 1.442, 1.556, 2.0, 2.5};
    float weight    = 1.;

    for (int i = 0; i < 5; ++i) {
    if (fabs(lep.Eta()) > etaBins[i] && fabs(lep.Eta()) <= etaBins[i+1]) {
    etaBin = i;
    break;
    }
    }

    for (int i = 0; i < 6; ++i) {
    if (lep.Pt() > ptBins[i] && lep.Pt() <= ptBins [i+1]) {
    ptBin = i;
    break;
    }
    }
    weight = eleScale[etaBin][ptBin];
     */

    float weight = 1.;

    if (lep.Pt() < 200) 
        weight = h2_EleMVASF->GetBinContent(h2_EleMVASF->FindBin(lep.Pt(), lep.Eta()));
    else
        weight = h2_EleMVASF->GetBinContent(h2_EleMVASF->FindBin(199, lep.Eta()));

    return weight;
}

float WeightUtils::GetMuEff(TLorentzVector lep) const
{
    int etaBin = 0;
    float binningEta[] = {0., 0.9, 1.2, 2.1, 2.4};
    float weight = 1.;

    for (int i = 0; i < 4; ++i) {
        if (fabs(lep.Eta()) > binningEta[i] && fabs(lep.Eta()) <= binningEta[i+1]) {
            etaBin = i;
            break;
        }
    }

    if (lep.Pt() < 500.)
        weight = _muSF2012[etaBin]->Eval(lep.Pt());
    //cout << etaBin << "\t" << lep.Pt() << "\t" << weight << endl;
    else
        weight = 1;

    return weight;
}

float WeightUtils::FakeWeight(TCPhysObject fakeableP4)
{
    float fakeRate = 0;

    if (fakeableP4.Type() == "electron") {
        fakeRate = h2_EleFakes->GetBinContent(h2_EleFakes->FindBin(fakeableP4.Eta(), fakeableP4.Pt()));
    } else if (fakeableP4.Type() == "muon") {
        fakeRate = h2_MuFakes->GetBinContent(h2_EleFakes->FindBin(fakeableP4.Eta(), fakeableP4.Pt()));
    }

    if (fakeRate > 0.99)
        return 0.;
    else
        return fakeRate / (1 - fakeRate);
}

