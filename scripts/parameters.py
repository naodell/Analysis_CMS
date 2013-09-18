#! /usr/bin/env python
import ROOT as r
import pickle

### Set styles
styleDict = {}

# Data
styleDict['DATA']               = (2, r.kBlack, 0, 21, 'Observed')
styleDict['DATA_MUON']          = (2, r.kGray, 0, 21, 'Observed (#mu#mu)')
styleDict['DATA_ELECTRON']      = (2, r.kGray+1, 0, 21, 'Observed (ee)')
styleDict['DATA_MUEG']          = (2, r.kGray+2, 0, 21, 'Observed (e#mu)')

#V+jets
styleDict['VJets']              = (0, r.kRed, 1, 1, 'V+jets') # Vector boson combination
styleDict['ZJets']              = (0, r.kRed, 1, 1, 'Z+jets') # Vector boson combination
styleDict['ZJets_M-50']         = (0, r.kRed+1, 1, 1, 'Z+jets (M_{Z/#gamma*} > 50)')
styleDict['ZJets_M-10To50']     = (0, r.kRed+2, 1, 1, 'Z+jets (M_{Z/#gamma*} < 50)')
styleDict['ZbbToLL']            = (2, r.kRed-8, 1, 1, 'Z+bb')
styleDict['ZG']                 = (0, r.kRed-9, 1, 1, 'Z#gamma')
styleDict['WJets']              = (2, r.kAzure-3, 1, 1, 'W+jets')
styleDict['WbbToLNu']           = (2, r.kAzure-2, 1, 1, 'W+bb')
styleDict['WG']                 = (0, r.kAzure-1, 1, 1, 'WG*')
styleDict['WGStarLNu2E']        = (0, r.kAzure, 1, 1, 'WG*#ell#nu2e')
styleDict['WGStarLNu2Mu']       = (0, r.kAzure, 1, 1, 'WG*#ell#nu2#mu')
styleDict['WGStarLNu2Tau']      = (0, r.kAzure, 1, 1, 'WG*#ell#nu2#tau')

# Madgraph diboson
styleDict['Diboson']            = (0, r.kGray+1, 1, 1, 'diboson')
styleDict['WW/ZZ']              = (0, r.kGray+1, 1, 1, 'WW/ZZ')
styleDict['ZZ4l']               = (0, r.kGray+1, 1, 1, 'ZZ#rightarrow4l')
styleDict['ZZJets2L2Nu']        = (2, r.kGreen+3, 1, 1, 'ZZ#rightarrow2l2#nu')
styleDict['ZZJets2L2Q']         = (2, r.kBlue-7, 1, 1, 'ZZ#rightarrow2l2q')
styleDict['ZZJets4L']           = (2, r.kBlue+2, 1, 1, 'ZZ#rightarrow4l')
styleDict['WWJets2L2Nu']        = (0, r.kGray+1, 1, 1, 'WW#rightarrow2l2#nu')
styleDict['WZJets3LNu']         = (3, r.kMagenta+1, 3004, 1, 'WZ#rightarrow3l#nu')
styleDict['WZJets2L2Q']         = (3, r.kBlue-3, 0, 1, 'WZ#rightarrow2l2q')

# Powheg diboson
styleDict['ZZ4mu']              = (2, r.kOrange+10, 1, 1,'ZZ#rightarrow 4l')
#styleDict['ZZ4mu']              = (2, r.kOrange+10, 1, 1, 'ZZ#rightarrow 4#mu')
styleDict['ZZ4e']               = (2, r.kOrange+9, 1, 1, 'ZZ#rightarrow 4e')
styleDict['ZZ4tau']             = (2, r.kOrange+8, 1, 1, 'ZZ#rightarrow 4#tau')
styleDict['ZZ2e2mu']            = (2, r.kOrange+7, 1, 1, 'ZZ#rightarrow 2e2#mu')
styleDict['ZZ2e2tau']           = (2, r.kOrange+6, 1, 1, 'ZZ#rightarrow 2e2#tau')
styleDict['ZZ2mu2tau']          = (2, r.kOrange+5, 1, 1, 'ZZ#rightarrow 2#mu2#tau')

#top
styleDict['top']                = (0, r.kBlue+1, 1, 1, 't#bar{t}/t')
styleDict['single top']         = (0, r.kBlue+2, 3004, 1, 't')
styleDict['ttbar']              = (0, r.kBlue+0, 1, 1, 't#bar{t}')
styleDict['tW']                 = (2, r.kBlue-1, 1, 1, 'tW')
styleDict['tbarW']              = (2, r.kBlue-2, 1, 1, '#bar{t}W')
styleDict['t_t-channel']        = (2, r.kBlue-3, 1, 1, 't (t-channel)')
styleDict['tbar_t-channel']     = (2, r.kBlue-4, 1, 1, '#bar{t} (t-channel)')

# tt+V
styleDict['ttV']                = (0, r.kGreen+1, 1, 1, 't#bar{t}V')
styleDict['ttZ']                = (0, r.kGreen+1, 1, 1, 't#bar{t}Z')
styleDict['ttW']                = (0, r.kGreen+2, 1, 1, 't#bar{t}W')
styleDict['ttG']                = (0, r.kGreen+3, 1, 1, 't#bar{t}G')

#triboson
styleDict['Triboson']           = (0, r.kCyan+0, 1, 1, 'triboson')
styleDict['WWW']                = (0, r.kCyan+0, 1, 1, 'WWW')
styleDict['WWZ']                = (0, r.kCyan+1, 1, 1, 'WWZ')
styleDict['WZZ']                = (0, r.kCyan+2, 1, 1, 'WZZ')
styleDict['ZZZ']                = (0, r.kCyan+3, 1, 1, 'ZZZ')
styleDict['WWG']                = (0, r.kCyan+4, 1, 1, 'WWG')

#QCD
styleDict['QCD']                = (2, r.kOrange, 1, 1, 'QCD')

#Alternative MC
styleDict['PhotonJets']         = (2, r.kRed, 0, 1, 'Z+jets (data)')
styleDict['DYToMuMu']           = (2, r.kRed, 0, 1, 'Z+jets (#mu#mu)')
styleDict['DYToEE']             = (2, r.kRed, 0, 1, 'Z+jets (ee)')
styleDict['DYToTauTau']         = (2, r.kRed-3, 0, 1, 'Z+jets (#tau#tau)')
styleDict['ZZToMuMu']           = (2, r.kGreen+3, 0, 1, 'ZZ#rightarrow 4l ')
styleDict['ZZToEE']             = (2, r.kGreen-3, 0, 1, 'ZZ (ee)')
styleDict['ZZToTauTau']         = (2, r.kGreen+2, 0, 1, 'ZZ (#tau#tau)')
styleDict['ZZToEMu']            = (2, r.kGreen-2, 0, 1, 'ZZ (e#mu)')
styleDict['ZZToETau']           = (2, r.kGreen-2, 0, 1, 'ZZ (e#tau)')
styleDict['ZZToMuTau']          = (2, r.kGreen-2, 0, 1, 'ZZ (#mu#tau)')
styleDict['ZZ']                 = (2, r.kOrange+4, 0, 1, 'ZZ')
styleDict['WW']                 = (2, r.kGreen-4, 0, 1, 'WW')
styleDict['WZ']                 = (2, r.kPink+9, 0, 1, 'WZ')
styleDict['ZGToNuNu']           = (2, r.kBlue+3, 0, 1, 'ZG->#nu#nu')
styleDict['GJets_15to30']       = (2, r.kYellow+2, 0, 1, 'gamma+jets') 

#Higgs
styleDict['higgs']              = (2, r.kBlue+3, 0, 1, 'higgs')

#Misc
styleDict['BGERROR']            = (0, r.kBlack, 3018, 0, 'BG error')
styleDict['FCNH']               = (3, r.kPink+3, 2, 22, 'FCNH')
styleDict['SUM_EFF']            = (1, r.kBlue, 3018, 21, 'BG')
styleDict['SIG_EFF']            = (1, r.kRed, 3018, 21, 'Signal')
styleDict['RATIO']              = (0, r.kBlack, 3002, 21, 'Ratio')
styleDict['fakes']              = (2, r.kBlack, 0, 21, 'fakes')

### Set scales
scaleDict = {'2011':{}, '2012':{}}

### 2011 x-sections
scaleDict['2011']['ZJets_M-50']         = 3048.
scaleDict['2011']['ZJets_M-10To50']     = 742.6
scaleDict['2011']['ZbbToLL']            = 304.
scaleDict['2011']['ZG']                 = 159.12

scaleDict['2011']['ZZJets2L2Nu']        = 0.1787
scaleDict['2011']['ZZJets2L2Q']         = 0.6246
scaleDict['2011']['WZJets3LNu']         = 0.856
scaleDict['2011']['WZJets2L2Q']         = 1.8329
scaleDict['2011']['WWJets2L2Nu']        = 4.783

scaleDict['2011']['ttbar']              = 165
scaleDict['2011']['tW']                 = 7.87
scaleDict['2011']['tbarW']              = 7.87

scaleDict['2011']['DYToMuMu']           = 1666.
scaleDict['2011']['DYToEE']             = 1666.
scaleDict['2011']['DYToTauTau']         = 1666.
scaleDict['2011']['ZZ']                 = 0.214
scaleDict['2011']['WZ']                 = 0.596
scaleDict['2011']['WW']                 = 4.51
scaleDict['2011']['GluGluWW']           = 0.1505
scaleDict['2011']['WJets']              = 31314
scaleDict['2011']['ZGToNuNu']           = 3.462

scaleDict['2011']['FCNC_M125_t']        = 0.004#*20
scaleDict['2011']['FCNC_M125_tbar']     = 0.004#*20
scaleDict['2011']['DATA_MUON']          = 1.
scaleDict['2011']['DATA_ELECTRON']      = 1.
scaleDict['2011']['DATA_MUEG']          = 1.
scaleDict['2011']['fakes']              = 1.

### 2012 x-sections
scaleDict['2012']['WJets']              = 36257.2
scaleDict['2012']['WbbToLNu']           = 10000. 
scaleDict['2012']['WG']                 = 1000.0
scaleDict['2012']['WGStarLNu2E']        = 5.873
scaleDict['2012']['WGStarLNu2Mu']       = 1.914
scaleDict['2012']['WGStarLNu2Tau']      = 0.336
scaleDict['2012']['ZJets_M-50']         = 3532.8 
scaleDict['2012']['ZJets_M-10To50']     = 860.5
scaleDict['2012']['ZbbToLL']            = 100. 
scaleDict['2012']['ZG']                 = 159.12

scaleDict['2012']['ZZJets2L2Nu']        = 0.365
scaleDict['2012']['ZZJets2L2Q']         = 1.28
scaleDict['2012']['ZZJets4L']           = 0.0921
scaleDict['2012']['WZJets3LNu']         = 1.086#*1.05 #<-- Check this
scaleDict['2012']['WZJets2L2Q']         = 5.09
scaleDict['2012']['WWJets2L2Nu']        = 5.995

scaleDict['2012']['ttbar']              = 234#*1.2  
scaleDict['2012']['tW']                 = 11.77
scaleDict['2012']['tbarW']              = 11.77
scaleDict['2012']['t_t-channel']        = 55.53
scaleDict['2012']['tbar_t-channel']     = 30.7
scaleDict['2012']['ttW']                = 0.249
scaleDict['2012']['ttZ']                = 0.208
scaleDict['2012']['ttG']                = 1.44

scaleDict['2012']['WWW']                = 0.082
scaleDict['2012']['WWZ']                = 0.063
scaleDict['2012']['WZZ']                = 0.0192
scaleDict['2012']['ZZZ']                = 0.0046
scaleDict['2012']['WWG']                = 0.528

scaleDict['2012']['QCD_20_MU']          = 84679.
scaleDict['2012']['QCD_20-30_EM']       = 2920632.
scaleDict['2012']['QCD_30-80_EM']       = 4615893.
scaleDict['2012']['QCD_80-170_EM']      = 183722
scaleDict['2012']['QCD_170-250_EM']     = 4588
scaleDict['2012']['QCD_250-350_EM']     = 556.75
scaleDict['2012']['QCD_350_EM']         = 89.1

scaleDict['2012']['DYToMuMu']           = 1666.
scaleDict['2012']['DYToEE']             = 1666.
scaleDict['2012']['DYToTauTau']         = 1666.
scaleDict['2012']['ZZ4mu']              = 0.07691 
scaleDict['2012']['ZZ4e']               = 0.07691
scaleDict['2012']['ZZ4tau']             = 0.07691
scaleDict['2012']['ZZ2e2mu']            = 0.1767 
scaleDict['2012']['ZZ2e2tau']           = 0.1767
scaleDict['2012']['ZZ2mu2tau']          = 0.1767
scaleDict['2012']['ZZ']                 = 7.7
scaleDict['2012']['WZ']                 = 32.3
scaleDict['2012']['WW']                 = 54.8
scaleDict['2012']['GluGluWW']           = 0.1505
scaleDict['2012']['WJets']              = 31314
scaleDict['2012']['ZGToNuNu']           = 3.462

scaleDict['2012']['ggHToZZ4L_M-125']    = .01
scaleDict['2012']['WHToWWW3L_M-125']    = .01
scaleDict['2012']['ggHToWW2L2Nu_M-125'] = .01

#scaleDict['GJets_15to30']       = 1/0.012
#scaleDict['GJets_30to50']       = 1/0.131
#scaleDict['GJets_50to80']       = 1/0.748
#scaleDict['GJets_80to120']      = 1/4.577
#scaleDict['GJets_120to170']     = 1/24.81
#scaleDict['GJets_170to300']     = 1/91.294
#scaleDict['GJets_300to470']     = 1/1391.1
#scaleDict['GJets_470to800']     = 1/15812.2

scaleDict['2012']['FCNC_M125_t']        = 234*2*1.*0.01*0.215*0.1*0.1*0.1
scaleDict['2012']['FCNC_M125_tbar']     = 234*2*1.*0.01*0.215*0.1*0.1*0.1
scaleDict['2012']['DATA_MUON']          = 1.
scaleDict['2012']['DATA_ELECTRON']      = 1.
scaleDict['2012']['DATA_MUEG']          = 1.
scaleDict['2012']['fakes']              = 1.

combineDict = {}
combineDict['FCNH']             = ['FCNC_M125_t', 'FCNC_M125_tbar']
combineDict['DATA']             = ['DATA_MUON', 'DATA_ELECTRON', 'DATA_MUEG']
combineDict['VJets']            = ['ZJets_M-50', 'ZJets_M-10To50', 'WJets']
combineDict['ZJets']            = ['ZJets_M-50', 'ZJets_M-10To50']
combineDict['WGStar']           = ['WGStarLNu2E', 'WGStarLNu2Mu', 'WGStarLNu2Tau']
combineDict['top']              = ['ttbar', 'tW', 'tbarW', 't_t-channel', 'tbar_t-channel']
combineDict['single top']       = ['tW', 'tbarW', 't_t-channel', 'tbar_t-channel']
combineDict['Diboson']          = ['ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'WWJets2L2Nu', 'ZZJets2L2Nu', 'WZJets3LNu']
combineDict['WW/ZZ']            = ['ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'WWJets2L2Nu', 'ZZJets2L2Nu']
combineDict['ZZ4l']             = ['ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau']
combineDict['ttV']              = ['ttZ', 'ttW', 'ttG']
combineDict['Triboson']         = ['WWW', 'WWZ', 'WZZ', 'ZZZ', 'WWG']
combineDict['QCD']              = ['QCD_20_MU', 'QCD_20-30_EM', 'QCD_30-80_EM', 'QCD_80-170_EM', 'QCD_170-250_EM', 'QCD_250-350_EM', 'QCD_350_EM']
combineDict['higgs']            = ['ggHToZZ4L_M-125', 'WHToWWW3L_M-125'] #, 'ggHToWW2L2Nu_M-125']

categoryDict = {'inclusive':'inclusive',
                'ss_inclusive':'ss inclusive', 'ss_mumu':'#mu^{#pm}#mu^{#pm}', 'ss_ee':'e^{#pm}e^{#pm}', 'ss_emu':'e^{#pm}#mu^{#pm}',
                'os_inclusive':'os inclusive', 'os_mumu':'#mu^{#pm}#mu^{#mp}', 'os_ee':'e^{#pm}e^{#mp}', 'os_emu':'e^{#pm}mu^{#mp}', 
                '3l_inclusive':'3l inclusive', '3l_OSSF':'(l^{#pm}l^{#mp})l', '3l_SSSF':'(l^{#pm}l^{#pm})l',
                '3l_eee':'eee', '3l_eemu':'ee#mu', '3l_emumu':'e#mu#mu','3l_mumumu':'#mu#mu#mu'
                }

paramFile = open('scripts/fcncParams.pkl', 'wb')
pickle.dump(scaleDict, paramFile)
pickle.dump(styleDict, paramFile)
pickle.dump(combineDict, paramFile)
pickle.dump(categoryDict, paramFile)
paramFile.close()
