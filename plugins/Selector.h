#ifndef _Selector_H
#define _Selector_H

#include <bitset>
#include <string>
#include <vector>
#include <map>

#include "TFile.h"
#include "TObject.h"
#include "TLorentzVector.h"
#include "TClonesArray.h"
#include "TRandom3.h"
#include "TGraphAsymmErrors.h"

#include "../interface/TCPrimaryVtx.h"
#include "../interface/TCPhysObject.h"
#include "../interface/TCJet.h"
#include "../interface/TCMuon.h"
#include "../interface/TCElectron.h"
#include "../interface/TCPhoton.h"
#include "../interface/TCGenParticle.h"
#include "../interface/TCGenJet.h"

#include "EGammaMvaEleEstimator.h"

using namespace std;

class Selector : public TObject {
    public:
        Selector();
        virtual ~Selector();

        Selector(const float*, const float*, const float*, const float*);

        //Selectors
        void    PVSelector(TClonesArray*);
        void    MuonSelector(TClonesArray*);
        void    ElectronSelector(TClonesArray*);
        void    JetSelector(TClonesArray*);
        void    PhotonSelector(TClonesArray*);
        void    GenParticleSelector(TClonesArray*, unsigned, unsigned, string);
        void    GenJetSelector(TClonesArray*);

        bool    ElectronMVA(TCElectron*);
        bool    ElectronTightID(TCElectron*);
        bool    ElectronLooseID(TCElectron*);
        bool    MuonTightID(TCMuon*);
        bool    MuonLooseID(TCMuon*);
        bool    PhotonTightID(TCPhoton*);
        //bool    PhotonLooseID(TCPhoton*);

        EGammaMvaEleEstimator *electronMVA;

        //Set internal variables
        void    SetRho(float);

        // Useful tools
        bool    IsZCandidate(TCPhysObject*, TCPhysObject*, float);
        float   EffectiveArea(TCPhysObject*); 
        bool    BTagModifier(TCJet, string);

        //Get processed collections
        vector<TVector3*>       GetSelectedPVs();
        vector<TCMuon>          GetSelectedMuons(string);
        vector<TCElectron>      GetSelectedElectrons(string);
        vector<TCPhoton>        GetSelectedPhotons(string);
        vector<TCJet>           GetSelectedJets(string);
        vector<TCGenParticle>   GetSelectedGenParticles(string);
        vector<TCGenJet>        GetSelectedGenJets();

        //Need to clear maps at the end of an event
        void    PurgeObjects();

        // jet efficiencies and resolution
        TCJet JERCorrections(TCJet*);

        ClassDef(Selector,1);

    private:
        //inputs
        float       _rho;

        //cuts
        const float*        _muPtCuts;
        const float*        _elePtCuts;
        const float*        _jetPtCuts;
        const float*        _phoPtCuts;

        //objects
        vector<TVector3*>   _selVertices;
        unsigned            _vtxIndex;

        //object maps
        map<string, vector<TCMuon> >        _selMuons;
        map<string, vector<TCElectron> >    _selElectrons;
        map<string, vector<TCPhoton> >      _selPhotons;
        map<string, vector<TCJet> >         _selJets;
        map<string, vector<TCGenParticle> > _selGenParticles;
        vector<TCGenJet>                    _selGenJets;

        // b-tag efficiencies from MC 
        TGraphAsymmErrors*  _misTagEff;
        TGraphAsymmErrors*  _bTagEff;

        //Misc
        TRandom3* rnGen;
};

#endif

#if !defined(__CINT__)
ClassImp(Selector);
#endif
