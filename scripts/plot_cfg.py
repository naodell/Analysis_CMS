#! /usr/bin/env python
import subprocess, shlex, datetime, copy
from multiprocessing import Process

import ROOT as r
from PlotProducer import *
from TableMaker import *

now         = datetime.datetime.now()
currentDate = '{0:02d}/{1:02d}/{2:02d}'.format(now.year, now.month, now.day)

### Get command line arguements

if len(sys.argv) > 2:
    batch   = sys.argv[1]
    suffix  = sys.argv[2]
else:
    print 'Need to specify input batch and suffix!!!  Exiting...'
    exit()

### This is the config file for manipulating 
### histograms using the PlotProducer class.  

plotType    = '.pdf'
selection   = 'fcnh'

cutList     = ['1_preselection']
cutList.extend(['2_Z_veto', '3_2jet', '4_MET'])#, '.', 'CR_WZ', 'CR_SUSY', '5_BDT'])
#cutList.extend(['.', '.', '.', 'X_0jet', 'X_1jet'])

period      = '2012'
LUMIDATA    = 19.712 

doPlots     = False
doYields    = True

doLog       = False
doEff       = False
doDiff      = False
doRatio     = True
doNorm      = True
do1D        = True
do2D        = True

doOS        = False
doSS        = True
do3l        = True

### Categories to be plotted ###
catSS       = ['ss_inclusive']
catSS.extend(['ss_mumu', 'ss_ee', 'ss_emu'])
#catSS.extend(['ss_endcap', 'ss_mixed', 'ss_barrel'])
catOS       = ['os_inclusive']
catOS.extend(['os_mumu', 'os_ee', 'os_emu']) 
cat3l       = ['3l_inclusive']
cat3l.extend(['3l_eee', '3l_eemu', '3l_emumu', '3l_mumumu'])
#cat3l.extend(['3l_OSSF', '3l_SSSF'])

### Samples to be included in stacks ###
samples     = {'all':[], 'inclusive':[], 'os':[], 'WZ':[], 'ttbar':[], 'ttZ':[], 'ZFake':[],
                '3l_inclusive':[], '3l_eee':[], '3l_eemu':[], '3l_emumu':[], '3l_mumumu':[], 
                'ss_inclusive':[], 'ss_ee':[], 'ss_emu':[], 'ss_mumu':[]}

#samples['all'].append('TBZ')
#samples['all'].append('WWSS')
#samples['all'].append('Triboson')
#samples['all'].append('ttV')
#samples['all'].append('ZZ4l')
samples['all'].append('Rare')
samples['all'].append('WZJets3LNu')
#samples['all'].append('TTH_M-125')
#samples['all'].append('higgs')

samples['all'].append('ZJets')
#samples['all'].append('ttbar')
#samples['all'].append('Diboson')
#samples['all'].append('WJetsToLNu')
#samples['all'].append('WJets')
#samples['all'].append('WbbToLNu')
#samples['all'].append('WG')
#samples['all'].append('QCD')

#samples['inclusive'].append('higgs')
samples['inclusive'].append('Triboson')
samples['inclusive'].append('ttV')
samples['inclusive'].append('Diboson')
samples['inclusive'].append('ZZ4l')
samples['inclusive'].append('top')
samples['inclusive'].append('ZJets')

## trilepton categories
#samples['3l_inclusive'].append('higgs')
#samples['3l_inclusive'].append('Triboson')
#samples['3l_inclusive'].append('WWSS')
#samples['3l_inclusive'].append('ttV')
#samples['3l_inclusive'].append('ZZ4l')
#samples['3l_inclusive'].append('TTH_M-125')
samples['3l_inclusive'].append('Rare')
samples['3l_inclusive'].append('WZJets3LNu')
#samples['3l_inclusive'].append('top')
#samples['3l_inclusive'].append('ZJets')
samples['3l_inclusive'].append('Fakes')
samples['3l_inclusive'].append('AIC')

### eee
samples['3l_eee'].extend(samples['3l_inclusive'])
#samples['3l_eee'].extend(['eFakes', 'llFakes'])
#samples['3l_eee'].append('eeeAIC')
#
### eemu
samples['3l_eemu'].extend(samples['3l_inclusive'])
#samples['3l_eemu'].extend(['eFakes', 'muFakes', 'llFakes'])
#samples['3l_eemu'].append('eemuAIC')
#
### emumu
samples['3l_emumu'].extend(samples['3l_inclusive'])
#samples['3l_emumu'].extend(['eFakes', 'muFakes', 'llFakes'])
#samples['3l_emumu'].append('emumuAIC')
#
### mumumu
samples['3l_mumumu'].extend(samples['3l_inclusive'])
#samples['3l_mumumu'].extend(['muFakes', 'llFakes'])
#samples['3l_mumumu'].append('mumumuAIC')

## 3l inclusive
#samples['3l_inclusive'].append('Fakes')
#samples['3l_inclusive'].append('AIC')


## same-sign categories
#samples['ss_inclusive'].append('higgs')
#samples['ss_inclusive'].append('TBZ')
#samples['ss_inclusive'].append('WWSS')
#samples['ss_inclusive'].append('Triboson')
#samples['ss_inclusive'].append('ttV')
#samples['ss_inclusive'].append('ZZ4l')

#samples['ss_inclusive'].append('TTH_M-125')
samples['ss_inclusive'].append('Rare')
samples['ss_inclusive'].append('WZJets3LNu')
samples['ss_inclusive'].append('Fakes')

#samples['ss_inclusive'].append('ttbar')
#samples['ss_inclusive'].append('WJets')
#samples['ss_inclusive'].append('QCD')
#samples['ss_inclusive'].append('WbbToLNu')
#samples['ss_inclusive'].append('WG')
#samples['ss_inclusive'].append('top')
#samples['ss_inclusive'].append('Diboson')
#samples['ss_inclusive'].append('ZJets')

## dielectrons
samples['ss_ee'].extend(samples['ss_inclusive'])
#samples['ss_ee'].extend(['eFakes', 'llFakes'])
samples['ss_ee'].append('QFlips')

## electron+muon
samples['ss_emu'].extend(samples['ss_inclusive'])
#samples['ss_emu'].extend(['eFakes', 'muFakes', 'llFakes'])
samples['ss_emu'].append('QFlips')

## dimuons
samples['ss_mumu'].extend(samples['ss_inclusive'])
#samples['ss_mumu'].append('ttbar')
#samples['ss_mumu'].append('QCD')
#samples['ss_mumu'].append('WJets')
#samples['ss_mumu'].extend(['muFakes', 'llFakes'])

## inclusive
#samples['ss_inclusive'].append('Fakes')
samples['ss_inclusive'].append('QFlips')

## geometric categories
samples['ss_endcap']    = samples['ss_mumu']
samples['ss_mixed']     = samples['ss_mumu']
samples['ss_barrel']    = samples['ss_mumu']

## opposite-sign categories
samples['os'].extend(['Diboson', 'top', 'ZJets'])

samples['WZ'].extend(['WW/ZZ', 'top', 'ZJets', 'WZJets3LNu'])
samples['ttbar'].extend(['single top', 'ZJets', 'ttbar'])
samples['ttZ'].extend(['top', 'ZJets', 'ZZ4l', 'WZJets3LNu', 'ttW', 'ttG', 'ttZ'])
samples['ZFake'].extend(['ZZ4l', 'WZJets3LNu', 'Fakes'])

p_plot = []


if doPlots:

    print '\nMaking the plots...\n'

    r.gROOT.SetBatch()

    ### Initialize plot producer ###
    plotter = PlotProducer(inputFile = 'fcncAnalysis/combined_histos/{0}_cut1_{1}_{2}.root'.format(selection, period, batch), savePath = '', scale = LUMIDATA, isAFS = False)
    plotter.set_period(period)
    plotter.set_output_type(plotType)

    ### DATASETS ###
    ### Specify the datasets you wish to stack 
    ### and overlay accordingly. 

    plotter.add_datasets(samples['all'])
    plotter._overlayList.extend(['DATA'])
    plotter._overlayList.extend(['FCNH', 'FCNHUp'])

    #plotter.get_scale_factors()
    plotter.get_scale_factors(['FCNH', 'FCNHUp'])

    ### VARIABLES ###
    ### First specify the directories in which your
    ### histograms are stored.  If directories are 
    ### not used enter '' as the only entry.  Then 
    ### list all of the variable names you wish to 
    ### plot while giving a key value which is the 
    ### directory that they are located in as a key.

    #plotter._directoryList1D            = ['Electron']
    plotter._directoryList1D            = ['Misc', 'Electron', 'Lepton', 'Lep+Jet', 'Dilepton', 'DileptonOS', 'Trilepton', 'MET', 'Jet', 'GEN', '4l']
    #plotter._directoryList1D            = ['Lepton', 'Lep+Jet', 'Dilepton', 'DileptonOS', 'Trilepton', 'MET', 'Jet', 'GEN', '4l']
    plotter._directoryList2D            = ['2D']

    plotter._variableDict['Misc']       = ['PvMult', 'YieldByCut', 'YieldByCutRaw', 'EventWeight', 'TriggerStatus', 'BDT']

    plotter._variableDict['Electron']   = [
                                           'ElectronPt', 'ElectronEta', 
                                           'LeadElectronEta', 'TrailingElectronEta',
                                           'ElectronDxy', 'ElectronDz',
                                           'ElectronIsoRel', 'ElectronIso',
                                           'LeadElectronPtBB', 'LeadElectronPtBE', 'LeadElectronPtBT', 
                                           'LeadElectronPtTB', 'LeadElectronPtTE', 'LeadElectronPtTT', 
                                           'LeadElectronPtEB', 'LeadElectronPtEE', 'LeadElectronPtET',
                                           'TrailingElectronPtBB', 'TrailingElectronPtBE', 'TrailingElectronPtBT', 
                                           'TrailingElectronPtTB', 'TrailingElectronPtTE', 'TrailingElectronPtTT', 
                                           'TrailingElectronPtEB', 'TrailingElectronPtEE', 'TrailingElectronPtET'
                                           ] 

    plotter._variableDict['Lepton']     = ['LeptonCharge', 'LeptonFlavor', 
                                           'Lepton1Pt', 'Lepton2Pt','Lepton3Pt',
                                           'Lepton1MT', 'Lepton2MT','Lepton3MT',
                                           'Lepton1Eta', 'Lepton2Eta', 'Lepton3Eta',
                                           'Lepton1IsoRel', 'Lepton2IsoRel', 'Lepton3IsoRel', 
                                           'MuonPt', 'MuonEta',
                                           'MuonDxy', 'MuonDz', 
                                           'MuonIsoRel', 'MuonIso',
                                           'Lepton1dxy', 'Lepton1dz',
                                           'Lepton2dxy', 'Lepton2dz',
                                           'Lepton3dxy', 'Lepton3dz',
                                           'LeptonMult', 'MuEleDeltaR', 'fakeableOverlapMult']
                                           #'Lepton1Phi', 'Lepton2Phi', 'Lepton3Phi']

    plotter._variableDict['Dilepton']   = ['DileptonHiggsMass21', 'DileptonZMass21', 'DileptonMass21', 'DileptonTransMass21', 'DileptonQt21', 'DileptonBalance21',
                                           'DileptonDeltaPhi21', 'DileptonDeltaEta21', 'DileptonDeltaR21', 'DileptonDeltaPt21']
                                           #'DileptonMass31', 'DileptonTransMass31', 'DileptonQt31', 
                                           #'DileptonDeltaPhi31', 'DileptonDeltaEta31', 'DileptonDeltaR31', 'DileptonDeltaPt31',
                                           #'DileptonMass32', 'DileptonTransMass32', 'DileptonQt32', 
                                           #'DileptonDeltaPhi32', 'DileptonDeltaEta32', 'DileptonDeltaR32', 'DileptonDeltaPt32']

    plotter._variableDict['DileptonOS'] = ['DileptonOSMass', 'DileptonOSTransMass', 'DileptonOSBalance',
                                           'DileptonOSQt', 'DileptonOSDeltaPt', 'DileptonOSDeltaR', 
                                           'DileptonOSDeltaEta', 'DileptonOSDeltaPhi'] 

    plotter._variableDict['Trilepton']  = ['DileptonLepDeltaR', 'DileptonLepDeltaPhi', 'DileptonLepDeltaEta', 
                                           'Lep3MetMT', 'TrileptonMass', 'TrileptonPt']

    plotter._variableDict['Lep+Jet']    = ['Lepton1BJetDeltaPhi', 'Lepton1BJetDeltaEta', 'Lepton1BJetDeltaR', 'Lepton1BJetDeltaPt',
                                           #'Lepton2BJetDeltaPhi', 'Lepton2BJetDeltaEta', 'Lepton2BJetDeltaR', 'Lepton2BJetDeltaPt',
                                           #'Lepton3BJetDeltaPhi', 'Lepton3BJetDeltaEta', 'Lepton3BJetDeltaR', 'Lepton3BJetDeltaPt',
                                           'Lepton1JetDeltaPhi', 'Lepton1JetDeltaEta', 'Lepton1JetDeltaR', 'Lepton1JetDeltaPt',
                                           #'Lepton2JetDeltaPhi', 'Lepton2JetDeltaEta', 'Lepton2JetDeltaR', 'Lepton2JetDeltaPt',
                                           #'Lepton3JetDeltaPhi', 'Lepton3JetDeltaEta', 'Lepton3JetDeltaR', 'Lepton3JetDeltaPt',
                                           'DileptonJetDeltaPhi', 'DileptonJetDeltaEta', 'DileptonJetDeltaR', 'DileptonJetDeltaPt',
                                           'DileptonBJetDeltaPhi', 'DileptonBJetDeltaEta', 'DileptonBJetDeltaR', 'DileptonBJetDeltaPt',
                                           'OverlapJetMult'
                                          ]

    plotter._variableDict['Jet']        = ['Jet1Pt', 'Jet2Pt',# 'Jet3Pt',
                                           'Jet1Eta', 'Jet2Eta',# 'Jet3Eta',
                                           #'Jet1Phi', 'Jet2Phi', 'Jet3Phi',
                                           'BJet1BDiscr', 'BJet1Pt', 'BJet1Eta', #'BJet1Phi', 
                                           'BJet2BDiscr', 'BJet2Pt', 'BJet2Eta', #'BJet2Phi',
                                           'HT', 'HTs', 'EventBalance', 'Centrality',
                                           'JetBJetDeltaPhi', 'JetBJetDeltaEta', 'JetBJetDeltaR',
                                           'JetMultCharge', 'JetMult', 'BJetMult', 'AllJetMult',
                                           'MatchedMuJetBDiscr', 'MatchedEleJetBDiscr', 
                                           'DijetMass']

    plotter._variableDict['MET']        = ['Met', 'MHT', 'METLD', 'MHT-MET', 'MetPhi', 'MetSumEt', 'MetSig',
                                           'MetLepton1DeltaPhi', 'MetLepton2DeltaPhi', 'MetLepton3DeltaPhi'
                                           'MetLepDeltaPhiMin', 'nearLepIndex', 'ProjectedMet'] 

    #plotter._variableDict['Fakes']      = ['FakeablePt', 'FakeableEta', 'FakeablePhi'
    #                                       'FakeableDxy', 'FakeableDz', 'FakeableIsoRel']

    plotter._variableDict['GEN']        = ['GenChargeMisId', 'GenMisIdPt', 'GenMisIdEta',
                                           'GenDeltaR', 'GenBalance']

    plotter._variableDict['4l']         = ['4lMass', '4lPt', '4lSumPt', '4lMet']

    plotter._variableDict['2D']         = ['MetVsHT', 'MetVsHT_zoom', 'MetVsSqrtHt', 'TrileptonMVsDileptonMOS',
                                            'DileptonMVsDeltaROS', 'DileptonQtVsDeltaROS', 'LepChargeVsFlavor']


     ###################   
     ### MAKE PLOTS! ###  
     ###################   

    r.gROOT.ProcessLine('.L ./scripts/tdrStyle.C')
    r.gROOT.ProcessLine('.L ./scripts/CMS_lumi.C')
    r.setTDRStyle()

    #r.gROOT.SetStyle('Plain')
    r.TGaxis.SetMaxDigits(3)
    r.gStyle.SetOptStat(0)

    ### 3l selection ###
    if do3l:
        for category in cat3l:
            plotter_3l = copy.deepcopy(plotter)
            plotter_3l.add_datasets(samples[category], Clear=True)
            plotter_3l._overlayList = ['DATA', 'FCNH']#, 'FCNHUp']

            for i, cut in enumerate(cutList):
                if cut == '.':
                    continue

                inFile  = 'fcncAnalysis/combined_histos/{0}_cut{1}_{2}_{3}.root'.format(selection, str(i+1), period, batch)

                if doLog:
                    outFile = 'plots/{0}/{1}_{2}_{3}/log/{4}'.format(currentDate, selection, batch, suffix, cut)
                else:
                    outFile = 'plots/{0}/{1}_{2}_{3}/linear/{4}'.format(currentDate, selection, batch, suffix, cut)

                plotter_3l.make_save_path(outFile, clean=True)
                if i > 1:
                    plotter_3l.set_rebin_factor(2)

                p_plot.append(Process(name = cut[2:] + '/' + category, target = plotter_wrapper, args=(plotter_3l, category, inFile, outFile, do1D, do2D, False, doLog, doRatio, doEff, doDiff)))

    ### ss selection ###
    if doSS:
        for category in catSS:
            ss_plotter = copy.deepcopy(plotter)
            ss_plotter.add_datasets(samples[category], Clear=True)
            ss_plotter._overlayList = ['DATA', 'FCNH']#, 'FCNHUp']
            #ss_plotter.set_clean_fakes(False)

            for i, cut in enumerate(cutList):
                if cut == '.':
                    continue

                inFile  = 'fcncAnalysis/combined_histos/{0}_cut{1}_{2}_{3}.root'.format(selection, i+1, period, batch)

                if doLog:
                    outFile = 'plots/{0}/{1}_{2}_{3}/log/{4}'.format(currentDate, selection, batch, suffix, cut)
                else:
                    outFile = 'plots/{0}/{1}_{2}_{3}/linear/{4}'.format(currentDate, selection, batch, suffix, cut)

                ss_plotter.make_save_path(outFile, clean=True)
                p_plot.append(Process(name = cut[2:] + '/' + category, target = plotter_wrapper, args=(ss_plotter, category, inFile, outFile, do1D, do2D, False, doLog, doRatio, doEff, doDiff)))

                ### overlay of fake distributions for single and double fakes ###
                #if cut in ['1_preselection', 'X_0jet', 'X_1jet', '3_2jet']:
                #    fake_plotter = copy.deepcopy(plotter)
                #    fake_plotter._overlayList = ['llFakes', 'muFakes']
                #    fake_plotter.draw_normalized(True)

                #    inFile  = 'fcncAnalysis/combined_histos/{0}_cut{1}_{2}_{3}.root'.format(selection, i+1, period, batch)
                #    if doLog:
                #        outFile = 'plots/{0}/{1}_{2}_{3}/log/{4}'.format(currentDate, selection, batch, suffix,  'fakes_overlay_{0}'.format(cut[2:]))
                #    else:
                #        outFile = 'plots/{0}/{1}_{2}_{3}/linear/{4}'.format(currentDate, selection, batch, suffix, 'fakes_overlay_{0}'.format(cut[2:]))
                #    fake_plotter.make_save_path(outFile, clean=True)

                #    p_plot.append(Process(name = 'fakes_overlay_{0}/{1}'.format(cut[2:], category), target = plotter_wrapper, args=(fake_plotter, category, inFile, outFile, do1D, False, True, True, False, False, False)))


    ### os selection ###
    if doOS:
        os_plotter = copy.deepcopy(plotter)
        os_plotter.add_datasets(samples['os'], Clear=True)
        os_plotter._overlayList = ['DATA']

        for i, cut in enumerate(cutList):
            if cut == '.':
                continue

            inFile  = 'fcncAnalysis/combined_histos/{0}_cut{1}_{2}_{3}.root'.format(selection, str(i+1), period, batch)

            if doLog:
                outFile = 'plots/{0}/{1}_{2}_{3}/log/{4}'.format(currentDate, selection, batch, suffix, cut)
            else:
                outFile = 'plots/{0}/{1}_{2}_{3}/linear/{4}'.format(currentDate, selection, batch, suffix, cut)

            os_plotter.make_save_path(outFile, clean=True)

            for category in catOS:
                p_plot.append(Process(name = cut[2:] + '/' + category, target = plotter_wrapper, args=(os_plotter, category, inFile, outFile, do1D, do2D, False, doLog, doRatio, False, False)))

    doLog = False

### End of configuration for PlotProducer ###

for process in p_plot:
    print 'Plotting {0}'.format(process.name)
    process.start()

for process in p_plot:
    process.join()

print '\n'

if doYields:
    ### Initialize table maker ###
    tableFile       = file('yields/.yields_tmp.tex', 'w')
    yieldTable      = TableMaker('fcncAnalysis/combined_histos/{0}_cut1_{1}_{2}.root'.format(selection, period, batch), 
                                    tableFile, scale = LUMIDATA, 
                                    delimiter = '&', doSumBG = True)
    yieldTable.set_period(period)
    yieldTable.add_datasets(samples['all'], Clear = True)
    if not doPlots:
        #yieldTable.get_scale_factors()
        yieldTable.get_scale_factors(['FCNH', 'FCNHUp'])

    if do3l:
        yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'Fakes', 'BG', 'DATA', 'FCNH']
        #yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'Fakes', 'BG', 'DATA', 'FCNHWW', 'FCNHTauTau', 'FCNHZZ']
        #yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'Fakes', 'BG', 'DATA', 'FCNHUpWW', 'FCNHUpZZ', 'FCNHUpTauTau']
        #yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'Fakes', 'BG', 'DATA', 'TTH_M-125']
        #yieldTable._columnList  = samples['3l_inclusive'] + ['BG', 'DATA', 'FCNH']
        #yieldTable._columnList  = ['BG', 'DATA', 'FCNHWW', 'FCNHZZ', 'FCNHTauTau']
        #yieldTable._columnList  = ['BG', 'DATA', 'FCNH']#, 'Significance'] 

        yieldTable.add_datasets(samples['3l_inclusive'], Clear = True)
        #yieldTable.add_datasets('TTH_M-125')
        yieldTable.add_datasets('FCNH')
        #yieldTable.add_datasets('FCNHWW')
        #yieldTable.add_datasets('FCNHZZ')
        #yieldTable.add_datasets('FCNHTauTau')
        yieldTable.add_datasets('DATA')

        yieldTable._rowList = 5*['.'] + ['ss dilepton', 'Z removal', '2+ jets', 'MET/jet']

        for category in cat3l:
            yieldTable._category = category
            histDict = yieldTable.get_hist_dict('YieldByCut')
            yieldTable.print_table(histDict, doErrors = True, doEff = False, startBin = 1)

    if doSS:

        #yieldTable.add_datasets(['Irreducible', 'Fakes', 'QFlips'], Clear = True)
        yieldTable._rowList = 5*['.'] + ['ss dilepton', 'Z removal', '2+ jets', 'MET']
        yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'QFlips', 'Fakes', 'BG', 'DATA', 'FCNH']
        #yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'QFlips', 'Fakes', 'BG', 'DATA', 'FCNHWW', 'FCNHTauTau', 'FCNHZZ']#, 'Significance'] 
        #yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'QFlips', 'Fakes', 'BG', 'DATA', 'TTH_M-125']
        #yieldTable._columnList  = ['Rare', 'WZJets3LNu', 'QFlips', 'Fakes', 'BG', 'DATA', 'FCNHUp', 'FCNH']

        for category in catSS:


            yieldTable.add_datasets(samples[category], Clear = True)
            #yieldTable.add_datasets('TTH_M-125')
            yieldTable.add_datasets('FCNH')
            #yieldTable.add_datasets('FCNHWW')
            #yieldTable.add_datasets('FCNHZZ')
            #yieldTable.add_datasets('FCNHTauTau')
            yieldTable.add_datasets('DATA')
            yieldTable._category = category

            histDict = yieldTable.get_hist_dict('YieldByCut')
            yieldTable.print_table(histDict, doErrors = True, doEff = False, startBin = 1)

    if False: ## Adding WZ high N_jet check

        yieldTable.set_input_file('fcncAnalysis/combined_histos/{0}_cut{1}_{2}_{3}.root'.format(selection, 6, period, batch))
        yieldTable._rowList     = ['{0} jet'.format(i+1) for i in range(5)]
        yieldTable._columnList  = samples['3l_inclusive'] + ['BG', 'DATA']

        yieldTable._category = '3l_inclusive'
        yieldTable.add_datasets(samples['3l_inclusive'], Clear = True)
        yieldTable.add_datasets('DATA')

        histDict = yieldTable.get_hist_dict('AllJetMult')
        yieldTable.print_table(histDict, doErrors = True, doEff = False, startBin = 1)

    tableFile.close()

    savePath = 'plots/{0}/{1}_{2}_{3}'.format(currentDate, selection, batch, suffix)
    yieldTable.make_save_path(savePath)
    subprocess.call('pdflatex -output-dir=yields yields/yields.tex', shell = True)
    subprocess.call('cp yields/yields.pdf {0}/.'.format(savePath), shell = True)
    subprocess.call('cp yields/.yields_tmp.tex {0}/yields.tex'.format(savePath), shell = True)
