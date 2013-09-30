#! /usr/bin/env python
import BatchMaster as b
import sys

cfg = b.JobConfig

''' Specify parameters '''
dCache      = '/pnfs/cms/WAX/11/store/user'
executable  = 'execBatch.csh'

selection   = 'fcnc'
period      = '2012'
doData      = False
doBG        = False
doSignal    = False
doFakes     = False

# Config from command line #

if len(sys.argv) > 0:
    period = sys.argv[1]
if 'data' in sys.argv[1:]:
    doData = True
if 'bg' in sys.argv[1:]:
    doBG = True
if 'signal' in sys.argv[1:]:
    doSignal = True
if 'fakes' in sys.argv[1:]:
    doFakes = True

############################

''' 
    Set job configurations.  The order of arguments is:
    (Dataset, path to data, number of jobs, arguments to pass to executable, output directory name)
'''

data    = []
fakes   = []
bg      = []
signal  = []


if period == '2012':
    data.extend([
        cfg('muon_2012A', dCache+'/devildog/nuTuples_v6_8TeV/DoubleMu_Run2012A_13Jul', 20, 'DATA_MUON muon 2012'),
        cfg('muon_2012B', dCache+'/devildog/nuTuples_v6_8TeV/DoubleMu_Run2012B_13Jul', 20, 'DATA_MUON muon 2012'),
        #cfg('muon_2012C_prompt', dCache+'/devildog/nuTuples_v6_8TeV/DoubleMu_Run2012C_Prompt', 20, 'DATA_MUON muon 2012'),
        #cfg('muon_2012C_recover', dCache+'/devildog/nuTuples_v6_8TeV/DoubleMu_Run2012C_Recover', 5, 'DATA_MUON muon 2012'),
        #cfg('muon_2012C_24Aug', dCache+'/devildog/nuTuples_v6_8TeV/DoubleMu_Run2012C_24Aug', 10, 'DATA_MUON muon 2012'),
        #cfg('muon_2012D', dCache+'/devildog/nuTuples_v6_8TeV/DoubleMu_Run2012D', 20, 'DATA_MUON muon 2012'),

        cfg('electron_2012A', dCache+'/devildog/nuTuples_v6_8TeV/DoubleElectron_Run2012A_13Jul', 20, 'DATA_ELECTRON electron 2012'),
        cfg('electron_2012B', dCache+'/devildog/nuTuples_v6_8TeV/DoubleElectron_Run2012B_13Jul', 20, 'DATA_ELECTRON electron 2012'),
        #cfg('electron_2012C_prompt', dCache+'/devildog/nuTuples_v6_8TeV/DoubleElectron_Run2012C_Prompt', 20, 'DATA_ELECTRON electron 2012'),
        #cfg('electron_2012C_recover', dCache+'/devildog/nuTuples_v6_8TeV/DoubleElectron_Run2012C_Recover', 5, 'DATA_ELECTRON electron 2012'),
        #cfg('electron_2012C_24Aug', dCache+'/devildog/nuTuples_v6_8TeV/DoubleElectron_Run2012C_24Aug', 10, 'DATA_ELECTRON electron 2012'),
        #cfg('electron_2012D', dCache+'/devildog/nuTuples_v6_8TeV/DoubleElectron_Run2012D_Prompt', 20, 'DATA_ELECTRON electron 2012'),

        cfg('muEG_2012A', dCache+'/devildog/nuTuples_v6_8TeV/MuEG_Run2012A', 20, 'DATA_MUEG muEG 2012'),
        #cfg('muEG_2012A_recover', dCache+'/devildog/nuTuples_v6_8TeV/MuEG_Run2012A_Recover', 20, 'DATA_MUEG muEG 2012'),
        cfg('muEG_2012B', dCache+'/devildog/nuTuples_v6_8TeV/MuEG_Run2012B', 20, 'DATA_MUEG muEG 2012')#,
        #cfg('muEG_2012C_prompt', dCache+'/devildog/nuTuples_v6_8TeV/MuEG_Run2012C_Prompt', 20, 'DATA_MUEG muEG 2012'),
        #cfg('muEG_2012C_recover', dCache+'/devildog/nuTuples_v6_8TeV/MuEG_Run2012C_Recover', 5, 'DATA_MUEG muEG 2012'),
        #cfg('muEG_2012C_24Aug', dCache+'/devildog/nuTuples_v6_8TeV/MuEG_Run2012C_24Aug', 10, 'DATA_MUEG muEG 2012'),
        #cfg('muEG_2012D', dCache+'/devildog/nuTuples_v6_8TeV/MuEG_Run2012D_Prompt', 20, 'DATA_MUEG muEG 2012')
        ])

    bg.extend([
        cfg('ZJets', dCache+'/naodell/nuTuples_v6_8TeV/DYJetsToLL_M-50', 40, 'ZJets muon 2012'),
        cfg('ZJets_M-10To50', dCache+'/naodell/nuTuples_v6_8TeV/DYJetsToLL_M-10To50', 20, 'ZJets_M-10To50 muon 2012'),
        #cfg('ZbbToLL', dCache+'/naodell/nuTuples_v6_8TeV/ZbbToLL', 20, 'ZbbToLL muon 2012'),
        #cfg('WbbToLNu', dCache+'/naodell/nuTuples_v6_8TeV/WbbJetsToLNu', 20, 'WbbToLNu muon 2012'),
        cfg('WJets', dCache+'/naodell/nuTuples_v6_8TeV/WJetsToLNu', 30, 'WJets muon 2012'),
        #cfg('WG', dCache+'/naodell/nuTuples_v6_8TeV/WGToLNuG', 10, 'WG muon 2012'),
        #cfg('ZG', dCache+'/naodell/nuTuples_v6_8TeV/ZGToLLG', 10, 'ZG muon 2012'),

        cfg('ttbar', dCache+'/naodell/nuTuples_v6_8TeV/TTJets', 40, 'ttbar muon 2012'),
        cfg('tbarW', dCache+'/naodell/nuTuples_v6_8TeV/Tbar_tW', 30, 'tbarW muon 2012'),
        cfg('tW', dCache+'/naodell/nuTuples_v6_8TeV/T_tW', 15, 'tW muon 2012'),
        cfg('t_t-channel', dCache+'/naodell/nuTuples_v6_8TeV/T_t', 15, 't_t-channel muon 2012'),
        cfg('tbar_t-channel', dCache+'/naodell/nuTuples_v6_8TeV/Tbar_t', 15, 'tbar_t-channel muon 2012'),
        cfg('ttW', dCache+'/naodell/nuTuples_v6_8TeV/TTWJets', 10, 'ttW muon 2012'),
        cfg('ttZ', dCache+'/naodell/nuTuples_v6_8TeV/TTZJets', 10, 'ttZ muon 2012'),

        cfg('WWW', dCache+'/naodell/nuTuples_v6_8TeV/WWWJets', 10, 'WWW muon 2012'),
        cfg('ZZJets2L2Nu', dCache+'/naodell/nuTuples_v6_8TeV/ZZJetsTo2L2Nu', 5, 'ZZJets2L2Nu muon 2012'),
        #cfg('ZZJets2L2Q', dCache+'/naodell/nuTuples_v6_8TeV/ZZJetsTo2L2Q', 5, 'ZZJets2L2Q muon 2012'),
        #cfg('ZZJets4L', dCache+'/naodell/nuTuples_v6_8TeV/ZZJetsTo4L', 5, 'ZZJets4L muon 2012'),
        cfg('ZZTo4e', dCache+'/naodell/nuTuples_v6_8TeV/ZZTo4e', 5, 'ZZ4e muon 2012'),
        cfg('ZZTo4mu', dCache+'/naodell/nuTuples_v6_8TeV/ZZTo4mu', 5, 'ZZ4mu muon 2012'),
        cfg('ZZTo4tau', dCache+'/naodell/nuTuples_v6_8TeV/ZZTo4tau', 5, 'ZZ4tau muon 2012'),
        cfg('ZZTo2e2mu', dCache+'/naodell/nuTuples_v6_8TeV/ZZTo2e2mu', 5, 'ZZ2e2mu muon 2012'),
        cfg('ZZTo2e2tau', dCache+'/naodell/nuTuples_v6_8TeV/ZZTo2e2tau', 5, 'ZZ2e2tau muon 2012'),
        cfg('ZZTo2mu2tau', dCache+'/naodell/nuTuples_v6_8TeV/ZZTo2mu2tau', 5, 'ZZ2mu2tau muon 2012'),
        cfg('WWJets2L2Nu', dCache+'/naodell/nuTuples_v6_8TeV/WWJetsTo2L2Nu', 5, 'WWJets2L2Nu muon 2012'),
        cfg('WZJets3LNu', dCache+'/naodell/nuTuples_v6_8TeV/WZJetsTo3LNu', 5, 'WZJets3LNu muon 2012'),
        #cfg('WZJets2L2Q', dCache+'/naodell/nuTuples_v6_8TeV/WZJetsTo2L2Q', 10, 'WZJets2L2Q muon 2012')

        cfg('QCD_20-30_EM', dCache+'/naodell/nuTuples_v6_8TeV/QCD_Pt_20-30_EM', 10, 'QCD_20-30_EM muon 2012'),
        cfg('QCD_30-80_EM', dCache+'/naodell/nuTuples_v6_8TeV/QCD_Pt_30-80_EM', 10, 'QCD_30-80_EM muon 2012'),
        cfg('QCD_80-170_EM', dCache+'/naodell/nuTuples_v6_8TeV/QCD_Pt_80-170_EM', 10, 'QCD_80-170_EM muon 2012'),
        cfg('QCD_170-250_EM', dCache+'/naodell/nuTuples_v6_8TeV/QCD_Pt_170-250_EM', 10, 'QCD_170-250_EM muon 2012'),
        cfg('QCD_250-350_EM', dCache+'/naodell/nuTuples_v6_8TeV/QCD_Pt_250-350_EM', 10, 'QCD_250-350_EM muon 2012'),
        cfg('QCD_350_EM', dCache+'/naodell/nuTuples_v6_8TeV/QCD_Pt_350_EM', 10, 'QCD_350_EM muon 2012'),
        cfg('QCD_20_MU', dCache+'/naodell/nuTuples_v6_8TeV/QCD_Pt_20_Mu', 10, 'QCD_20_MU muon 2012'),

        cfg('ggHToZZ4L_M-125', dCache+'/naodell/nuTuples_v6_8TeV/GluGluToHToZZTo4L_M-125', 2, 'ggHToZZ4L_M-125 muon 2012'),
        cfg('ggHToWW2L2Nu_M-125', dCache+'/naodell/nuTuples_v6_8TeV/GluGluToHToWWTo2LAndTau2Nu_M-125', 2, 'ggHToWW2L2Nu_M-125 muon 2012'),
        cfg('WHToWWW3L_M-125', dCache+'/naodell/nuTuples_v6_8TeV/WH_HToWW_3l_M-125', 2, 'WHToWWW3L_M-125 muon 2012')
        ])

    signal.extend([
        cfg('FCNC_M125_tHj', dCache+'/naodell/nuTuples_v6_8TeV/FCNH_M125_t', 2, 'FCNC_M125_t mc 2012'),
        cfg('FCNC_M125_tbarHj', dCache+'/naodell/nuTuples_v6_8TeV/FCNH_M125_tbar', 2, 'FCNC_M125_tbar mc 2012')
        ])


if period == '2011':
    data.extend([
        cfg('muon_2011A', dCache+'/andreypz/nuTuples_v2_7TeV/DoubleMu_HZZ_Run2011A', 30, 'DATA muon 2011'),
        cfg('muon_2011B', dCache+'/andreypz/nuTuples_v2_7TeV/DoubleMu_HZZ_Run2011B', 30, 'DATA muon 2011'),
        cfg('muEG_2011A', dCache+'/naodell/nuTuples_v2_7TeV/MuEG_Run2011A', 30, 'DATA muEG 2011'),
        cfg('muEG_2011B', dCache+'/naodell/nuTuples_v2_7TeV/MuEG_Run2011B', 30, 'DATA muEG 2011'),
        #cfg('electron_2011A', dCache+'/naodell/nuTuples_v2_7TeV/DoubleElectron_Run2011A', 20, 'DATA 16,17,18 electron 2011')
        #cfg('electron_2011B', dCache+'/andreypz/nuTuples_v2_7TeV/DoubleElectron_HZZ_Run2011B', 20, 'DATA 16,17,18 electron 2011')
        ])

    bg.extend([
        cfg('ZJets', dCache+'/andreypz/nuTuples_v2_7TeV/DYjets', 40, 'ZJets mc 2011'),
        cfg('ttbar', dCache+'/andreypz/nuTuples_v2_7TeV/TTJets', 40, 'ttbar mc 2011'),
        cfg('tbarW', dCache+'/andreypz/nuTuples_v2_7TeV/tbarW', 30, 'tbarW mc 2011'),
        cfg('tW', dCache+'/andreypz/nuTuples_v2_7TeV/tW', 15, 'tW mc 2011'),
        cfg('ZZJets2L2Nu', dCache+'/naodell/nuTuples_v2_7TeV/ZZJetsTo2L2Nu', 5, 'ZZJets2L2Nu mc 2011'),
        cfg('ZZJets2L2Q', dCache+'/naodell/nuTuples_v2_7TeV/ZZJetsTo2L2Q', 5, 'ZZJets2L2Q mc 2011'),
        cfg('WWJets2L2Nu', dCache+'/naodell/nuTuples_v2_7TeV/WWJetsTo2L2Nu', 5, 'WWJets2L2Nu mc 2011'),
        cfg('WZJets3LNu', dCache+'/naodell/nuTuples_v2_7TeV/WZJetsTo3LNu', 5, 'WZJets3LNu mc 2011'),
        cfg('WZJets2L2Q', dCache+'/naodell/nuTuples_v2_7TeV/WZJetsTo2L2Q', 5, 'WZJets2L2Q mc 2011')
        ])


    signal.extend([
        cfg('FCNC', dCache+'/devildog/nuTuples_v2_7TeV/FCNC_tH', 5, 'FCNC mc 2011')
        ])

inputSamples = []

if doData:
    inputSamples.extend(data)
if doBG:
    inputSamples.extend(bg)
if doSignal:
    inputSamples.extend(signal)
if doFakes:
    inputSamples.extend(fakes)

if len(inputSamples) is not 0:
    batcher = b.BatchMaster(inputSamples, shortQueue = False, stageDir = 'batchStage', executable = executable, selection = selection + '_' + period)
    batcher.submit_to_batch()

