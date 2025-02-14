#! /usr/bin/env python
from array import array
from AnalysisTools import *
import subprocess
import ROOT as r

def make_graph_ratio_1D(outName, h1_Numer, h1_Denom):
    ### Mostly useful for 1D efficiencies ###
    #h1_Numer.Print("range")
    #h1_Denom.Print("range")

    g_Eff = r.TGraphAsymmErrors()
    g_Eff.Divide(h1_Numer, h1_Denom)
    g_Eff.SetName('g_{0}'.format(outName))
    g_Eff.SetTitle('{0};{1};#varepsilon'.format(outName, h1_Numer.GetXaxis().GetTitle(), h1_Numer.GetYaxis().GetTitle()))

    return g_Eff

def make_graph_ratio_2D(outName, h2_Numer, h2_Denom):
    ### Mostly useful for 2D efficiencies, returns an array of
    ### TGraphAsymmErrors

    gList = []
    for i in range(h2_Numer.GetYaxis().GetNbins()):
        h1_Numer = h2_Numer.ProjectionX('h_Numer_{0}_{1}'.format(outName, i+1), i+1, i+1)
        h1_Denom = h2_Denom.ProjectionX('h_Denom_{0}_{1}'.format(outName, i+1), i+1, i+1)

        for j in range(h1_Numer.GetNbinsX()):
            numerContent = h1_Numer.GetBinContent(j+1)
            if numerContent < 0:
                h1_Numer.SetBinContent(i+1, 0.)

            denomContent = h1_Denom.GetBinContent(j+1)
            if denomContent < 0:
                h1_Denom.SetBinContent(i+1, 0.)

        gList.append(r.TGraphAsymmErrors())
        gList[i].Divide(h1_Numer, h1_Denom)
        gList[i].SetName('g_{0}_{1}'.format(outName, i+1))
        gList[i].SetTitle('{0}_{1};{2};#varepsilon'.format(outName, i+1, h2_Numer.GetXaxis().GetTitle()))

    return gList


class RatioMaker(AnalysisTools):
    ### For producing efficiency weight files ###
    def __init__(self, inputFileName, outFileName, scale = 1.):
        AnalysisTools.__init__(self, inputFileName, scale)
        self._outFile       = r.TFile(outFileName, 'RECREATE')
        self._ratioDict1D   = {}
        self._ratioDict2D   = {}
        self._hists         = []
        self._dataset       = ''

    def write_outfile(self, hists = []):
        
        for hist in hists:
            self._outFile.Add(hist)

        self._outFile.Write()
        self._outFile.Close()

    def set_ratio_1D(self, ratioDict):
        self._ratioDict1D = ratioDict

    def set_ratio_2D(self, ratioDict):
        self._ratioDict2D = ratioDict

    def set_dataset(self, dataset):
        self._dataset = dataset

    def make_category_directory(self):
        fileName = '{0}_{1}'.format(self._category, self._dataset)
        if not self._outFile.GetDirectory(fileName):
            self._outFile.mkdir(fileName)
            self._outFile.cd(fileName)
                
    def make_1D_ratios(self, ratioSample, bgSample = '', categories = []):
        ### make ratios for all variables specified in ratioDict1D.  Sample
        ### combinations should be specified in combineDict in parameters.py.
        ### bgSample is subtracted off of the inputs for the ratio.

        self.make_category_directory()

        if categories == []:
            categories = [self.get_category(), self.get_category()]

        for key,value in self._ratioDict1D.iteritems():
            self.set_category(categories[0])
            h1_Numer    = self.combine_samples(value[0], ratioSample) 
            self.set_category(categories[1])
            h1_Denom    = self.combine_samples(value[1], ratioSample) 

            if not h1_Numer or not h1_Denom:
                print 'Cannot find {0} in input file'.format(key)
                continue

            if bgSample != '':
                self.set_category(categories[0])
                h1_bgNumer  = self.combine_samples(value[0], bgSample) 
                self.set_category(categories[1])
                h1_bgDenom  = self.combine_samples(value[1], bgSample) 

                h1_Numer.Add(h1_bgNumer, -1.)
                h1_Denom.Add(h1_bgDenom, -1.)

            # Make sure there are no negative weighted histogram bins
            for i in range(h1_Numer.GetNbinsX()):
                binContent = h1_Numer.GetBinContent(i+1),
                if binContent[0] < 0.:
                    h1_Numer.SetBinContent(i+1,0.)

            for i in range(h1_Denom.GetNbinsX()):
                binContent = h1_Denom.GetBinContent(i+1),
                if binContent[0] < 0.:
                    h1_Denom.SetBinContent(i+1,0.)

            ### Save ratios to histograms
            h1_Eff = h1_Numer.Clone()
            h1_Eff.SetName('h1_{0}'.format(key))
            h1_Eff.SetTitle('{0};{1};fake rate'.format(key, h1_Numer.GetXaxis().GetTitle()))
            h1_Eff.Divide(h1_Numer, h1_Denom, 1., 1., 'B')
            
            self._hists.append(h1_Eff)
            self._hists.append(h1_Numer)
            self._hists.append(h1_Denom)

            g_Ratio = make_graph_ratio_1D(key, h1_Numer, h1_Denom)
            self._outFile.GetDirectory('{0}_{1}'.format(self._category, self._dataset)).Add(g_Ratio)


    def make_2D_ratios(self, ratioSample, bgSample = '', doProjections = True): 
        ### make ratios for all variables specified in ratioDict2D.  Sample
        ### combinations should be specified in combineDict in parameters.py.
        ### bgSample is subtracted off of the inputs for the ratio. Produces a
        ### graph for each row in the input 2D histogram

        self.make_category_directory()

        for key,value in self._ratioDict2D.iteritems():
            h2_Numer    = self.combine_samples(value[0], ratioSample, histType = '2D') 
            h2_Denom    = self.combine_samples(value[1], ratioSample, histType = '2D') 

            #print h2_Numer.Integral(),h2_Denom.Integral(), 

            if bgSample != '':
                h2_bgNumer  = self.combine_samples(value[0], bgSample, histType = '2D') 
                h2_bgDenom  = self.combine_samples(value[1], bgSample, histType = '2D') 

                h2_Numer.Add(h2_bgNumer, -1.)
                h2_Denom.Add(h2_bgDenom, -1.)

            self._hists.append(h2_Numer)
            self._hists.append(h2_Denom)

            ### Set negative entries to 0
            for binX in range(h2_Numer.GetNbinsX()):
                for binY in range(h2_Numer.GetNbinsY()):
                    if h2_Numer.GetBinContent(binX+1, binY+1) < 0.:
                        h2_Numer.SetBinContent(binX+1, binY+1, 0.)

                    if h2_Denom.GetBinContent(binX+1, binY+1) < 0.:
                        h2_Denom.SetBinContent(binX+1, binY+1, 0.)

            ### Save ratios to 2D histograms
            h2_Eff = r.TH2D('h2_{0}'.format(key), '{0};;'.format(key),
                             h2_Numer.GetNbinsX(), h2_Numer.GetXaxis().GetXmin(), h2_Numer.GetXaxis().GetXmax(),
                             h2_Numer.GetNbinsY(), h2_Numer.GetYaxis().GetXmin(), h2_Numer.GetYaxis().GetXmax())
            h2_Eff.Divide(h2_Numer, h2_Denom, 1., 1., 'B')
            self._hists.append(h2_Eff)

            ### Save ratios to 1D graphs (TGraphAsymmErrors)
            g_RatioList = make_graph_ratio_2D(key, h2_Numer, h2_Denom)
            for g_Ratio in g_RatioList:
                self._outFile.GetDirectory('{0}_{1}'.format(self._category, self._dataset)).Add(g_Ratio)


    def charge_flip_fitter(self, ratioSample, nToys = 10):
        ### Converts 2D (double electron) charge flip probabilities to 1D
        ### (single electron) charge flip probabilities.  Assumes mapping is
        ### P(i,j) = p(i) + p(j).

        self.make_category_directory()

        for key,value in self._ratioDict2D.iteritems():
            h2_Numer    = self.combine_samples(value[0], ratioSample, histType = '2D') 
            h2_Denom    = self.combine_samples(value[1], ratioSample, histType = '2D') 

            h2_Eff = r.TH2D('h2_{0}'.format(key), '{0};;'.format(key),
                             h2_Numer.GetNbinsX(), h2_Numer.GetXaxis().GetXmin(), h2_Numer.GetXaxis().GetXmax(),
                             h2_Numer.GetNbinsY(), h2_Numer.GetYaxis().GetXmin(), h2_Numer.GetYaxis().GetXmax())

            h2_Eff.Divide(h2_Numer, h2_Denom, 1., 1., 'B')
            self._hists.append(h2_Eff)

            ### Hack for lowest pt barrel-barrel bin ###
            h2_Eff.SetBinContent(1,1,0.0001)
            h2_Eff.SetBinError(1,1,0.0001)

            ### Guess at values of p(i) from diagonal bins, i.e., p(i) = 0.5*P(i,j)
            nBinsX = h2_Eff.GetNbinsX()
            nBinsY = h2_Eff.GetNbinsY()
            prob0 = [[0.5*h2_Eff.GetBinContent(i+1, i+1) for i in range(nBinsX)], [h2_Eff.GetBinError(i+1, i+1) for i in range(nBinsX)]]

            #for prob in prob0[0]: print '{0:.3f}'.format(100*prob),
            #print '\n'

            for toy in range(nToys):
                probs = [[0. for i in range(nBinsX)], [0. for i in range(nBinsX)]]
                for binX in range(nBinsX):
                    for binY in range(nBinsY):
                        #if binX == binY: continue

                        binContentXY    = h2_Eff.GetBinContent(binX+1, binY+1) 
                        binErrorXY      = h2_Eff.GetBinError(binX+1, binY+1) 
                        errX            = binErrorXY*binErrorXY + prob0[1][binY]*prob0[1][binY]
                        errY            = binErrorXY*binErrorXY + prob0[1][binX]*prob0[1][binX]

                        if binContentXY != 0:
                            if prob0[0][binY] != 0:
                                probs[0][binX] += (binContentXY - prob0[0][binY])/errX
                                probs[1][binX] += 1./errX
                            if prob0[0][binX] != 0 and binX != binY:
                                probs[0][binY] += (binContentXY - prob0[0][binX])/errY
                                probs[1][binY] += 1./errY
                        else:
                            continue

                        #if binX == 0: 
                        #    print (binX+1, binY+1), '{0:.3f} {1:.3f}'.format(100*probs[0][binX]/probs[1][binX], 100*probs[0][binY]/probs[1][binY])
                        #if binY == 0: 
                        #    print (binX+1, binY+1), '{0:.3f} {1:.3f}'.format(100*probs[0][binX]/probs[1][binX], 100*probs[0][binY]/probs[1][binY])
                        

                for binX in range(nBinsX):
                    #print probs[binX], probs[0][binX]/nBinsX
                    if probs[1][binX] != 0:
                        probs[0][binX] = probs[0][binX]/probs[1][binX]
                        probs[1][binX] = 1./sqrt(probs[1][binX])

                prob0 = probs[:]

                #for prob in probs[0]: print '{0:.3f}'.format(100*prob),
                #print ''

            ### Set datapoints to bin centers, should possibly be done in smarter way 
            ptBins = [25., 50., 105.]
            g_ProbBB = r.TGraphErrors(len(ptBins), array('f', ptBins),  array('f', probs[0][:nBinsX/3]), \
                                                   array('f', [0.1 for bin in ptBins]), array('f', probs[1][:nBinsX/3]))
            g_ProbBB.SetName('g_{0}_BB'.format(key))
            g_ProbBB.SetTitle('inner barrel electron charge flips;iPt;#varepsilon')

            g_ProbBE = r.TGraphErrors(len(ptBins), array('f', ptBins),  array('f', probs[0][nBinsX/3:2*nBinsX/3]), 
                                                   array('f', [0.1 for bin in ptBins]), array('f', probs[1][nBinsX/3:2*nBinsX/3]))
            g_ProbBE.SetName('g_{0}_BE'.format(key))
            g_ProbBE.SetTitle('outer barrel electron charge flips;iPt;#varepsilon')

            g_ProbEE = r.TGraphErrors(len(ptBins), array('f', ptBins),  array('f', probs[0][2*nBinsX/3:]), 
                                                   array('f', [0.1 for bin in ptBins]), array('f', probs[1][2*nBinsX/3:]))
            g_ProbEE.SetName('g_{0}_EE'.format(key))
            g_ProbEE.SetTitle('endcap electron charge flips;iPt;#varepsilon')

            self._outFile.GetDirectory(self._category).Add(g_ProbBB)
            self._outFile.GetDirectory(self._category).Add(g_ProbBE)
            self._outFile.GetDirectory(self._category).Add(g_ProbEE)


if __name__ == '__main__':

    r.gROOT.SetBatch()
    r.gStyle.SetOptStat(0)
    r.TH1.SetDefaultSumw2(r.kTRUE)
    r.TH2.SetDefaultSumw2(r.kTRUE)

    if len(sys.argv) > 1:
        type    = sys.argv[1]
        batch   = sys.argv[2]
    else:
        print 'A batch and ratio type must be specified.  Otherwise, do some hacking so this thing knows about your inputs.'
        exit()

    ### For AIC rates ###
    if type == 'AIC':
        inFile  = 'fcncAnalysis/combined_histos/fcnh_cut1_2012_{0}.root'.format(batch)
        outFile = 'data/AIC_TEST.root'

        ratioMaker = RatioMaker(inFile, outFile, scale = 19.7)
        ratioMaker.set_category('inclusive')
        ratioMaker.get_scale_factors(['AIC_BG'], corrected = False)
        #ratioMaker.get_scale_factors([''], corrected = False)

        ratioMaker.set_ratio_1D({'mumumu':('ThirdMuonPt_AIC', 'PhotonPt_AIC_Mu3l')})
        ratioMaker.make_1D_ratios('DATA', bgSample = '', categories = ['3l_mumumu', 'inclusive'])
        ratioMaker.set_ratio_1D({'emumu':('ThirdElectronPt_AIC', 'PhotonPt_AIC_Mu3l')})
        ratioMaker.make_1D_ratios('DATA', bgSample = '', categories = ['3l_emumu', 'inclusive'])

        ratioMaker.set_ratio_1D({'eemu':('ThirdMuonPt_AIC', 'PhotonPt_AIC_El3l')})
        ratioMaker.make_1D_ratios('DATA', bgSample = '', categories = ['3l_eemu', 'inclusive'])
        ratioMaker.set_ratio_1D({'eee':('ThirdElectronPt_AIC', 'PhotonPt_AIC_El3l')})
        ratioMaker.make_1D_ratios('DATA', bgSample = '', categories = ['3l_eee', 'inclusive'])

        ratioMaker.write_outfile()

    ### For electron charge misID efficiencies ###
    if type == 'QFlips':
        inFile  = 'fcncAnalysis/combined_histos/fcnh_cut1_2012_{0}.root'.format(batch)
        outFile = 'data/electronQMisID_TEST.root'

        ratioMaker = RatioMaker(inFile, outFile, scale = 19.7)
        ratioMaker.set_category('inclusive')

        eMisQDict = {
            #'LeadElectronMisQ':('LeadElecQMisIDNumer', 'LeadElecQMisIDDenom'),
            #'TrailingElectronMisQ':('TrailingElecQMisIDNumer', 'TrailingElecQMisIDDenom'),
            'DielectronMisQ':('DileptonQMisIDNumer', 'DileptonQMisIDDenom'),
            'DielectronMisQLowJet':('DileptonQMisIDNumerLowJet', 'DileptonQMisIDDenomLowJet'),
            'DielectronMisQHighJet':('DileptonQMisIDNumerHighJet', 'DileptonQMisIDDenomHighJet')
            }

        ratioMaker.set_ratio_2D(eMisQDict)
        #ratioMaker.make_2D_ratios('DATA_ELECTRON', doProjections = False)
        ratioMaker.charge_flip_fitter('DATA_ELECTRON', nToys = 5)
        #ratioMaker.charge_flip_fitter('ZJets', nToys = 100)

        mcMisQDict = {
            'EleQMisID_MC':('EleQMisIDNumerMC', 'EleQMisIDDenomMC'),
            'EleQMisIDInZ_MC':('EleQMisIDNumerMCInZ', 'EleQMisIDDenomMCInZ'),
            'EleQMisIDOutZ_MC':('EleQMisIDNumerMCOutZ', 'EleQMisIDDenomMCOutZ')
        }

        ratioMaker.set_ratio_2D(mcMisQDict)
        #ratioMaker.make_2D_ratios('ZJets', doProjections = False)

        ratioMaker.write_outfile()

