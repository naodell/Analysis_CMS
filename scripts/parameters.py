#! /usr/bin/env python
import ROOT as r
import pickle

signalScale = .01
### Set styles
styleDict = {}

# Data
styleDict['DATA']               = (2, r.kBlack, 0, 20, 'Data')
styleDict['DATA_MUON']          = (2, r.kBlack, 0, 21, 'Data (#mu#mu)')
styleDict['DATA_ELECTRON']      = (2, r.kBlack, 0, 21, 'Data (ee)')
styleDict['DATA_MUEG']          = (2, r.kBlack, 0, 21, 'Data (e#mu)')
styleDict['DATA_FAKES']         = (2, r.kBlue+4, 3001, 22, 'Fail')

# For fake studies
styleDict['PASS']               = (2, r.kBlack, 0, 23, 'Pass')
styleDict['PROMPT']             = (2, r.kRed, 3001, 21, 'Prompt')
styleDict['FAKEABLE']           = (2, r.kBlue, 0, 21, 'Fakeable')
styleDict['Irreducible']        = (2, r.kBlue, 0, 21, 'Irreducible')

#V+jets
styleDict['VJets']              = (0, r.kRed, 1001, 1, 'V+jets') # Vector boson combination
styleDict['ZJets']              = (0, r.kRed, 1001, 1, 'Z+jets') 
styleDict['ZJets_M-50']         = (0, r.kRed+1, 1001, 1, 'Z+jets (M_{Z/#gamma*} > 50)')
styleDict['ZJets_M-10To50']     = (0, r.kRed+2, 1001, 1, 'Z+jets (M_{Z/#gamma*} < 50)')
styleDict['ZbbToLL']            = (2, r.kRed-8, 1001, 1, 'Z+bb')
styleDict['ZG']                 = (0, r.kRed-9, 1001, 1, 'Z#gamma')
styleDict['WJetsToLNu']         = (2, r.kAzure-3, 1001, 1, 'W+jets')
styleDict['WJets']              = (2, r.kAzure-3, 1001, 1, 'W+jets')
styleDict['W1JetsToLNu']        = (2, r.kAzure-4, 1001, 1, 'W+1 jet')
styleDict['W2JetsToLNu']        = (2, r.kAzure+3, 1001, 1, 'W+2 jet')
styleDict['W3JetsToLNu']        = (2, r.kAzure-2, 1001, 1, 'W+3 jet')
styleDict['W4JetsToLNu']        = (2, r.kAzure+1, 1001, 1, 'W+4 jet')
styleDict['WbbToLNu']           = (2, r.kAzure-2, 1001, 1, 'W+bb')
styleDict['WG']                 = (0, r.kAzure-1, 1001, 1, 'W#rightarrow l#nu#gamma')
styleDict['WGstar']             = (0, r.kAzure-1, 1001, 1, 'WG*')
styleDict['WGStarLNu2E']        = (0, r.kAzure, 1001, 1, 'WG*#ell#nu2e')
styleDict['WGStarLNu2Mu']       = (0, r.kAzure, 1001, 1, 'WG*#ell#nu2#mu')
styleDict['WGStarLNu2Tau']      = (0, r.kAzure, 1001, 1, 'WG*#ell#nu2#tau')

# Madgraph diboson
styleDict['Diboson']            = (0, r.kGray+1, 1001, 1, 'diboson')
styleDict['WW/ZZ']              = (0, r.kGray+1, 1001, 1, 'WW/ZZ')
styleDict['ZZ4l']               = (0, r.kGray+1, 1001, 1, 'ZZ#rightarrow4l')
styleDict['VV2l']               = (0, r.kGray+2, 1001, 1, 'VV#rightarrow2l2x')
styleDict['ZZJets2L2Nu']        = (2, r.kGreen+3, 1001, 1, 'ZZ#rightarrow2l2#nu')
styleDict['ZZJets2L2Q']         = (2, r.kBlue-7, 1001, 1, 'ZZ#rightarrow2l2q')
styleDict['ZZJets4L']           = (2, r.kBlue+2, 1001, 1, 'ZZ#rightarrow4l')
styleDict['WWJets2L2Nu']        = (0, r.kGreen+2, 1001, 1, 'WW#rightarrow2l2#nu')
styleDict['WZJets3LNu']         = (3, r.kMagenta+1, 1001, 1, 'WZ#rightarrow3l#nu')
styleDict['WZJets2L2Q']         = (3, r.kBlue-3, 0, 1, 'WZ#rightarrow2l2q')

# Powheg diboson
#styleDict['ZZ4mu']              = (2, r.kOrange+10, 1, 1,'ZZ#rightarrow 4l')
styleDict['ZZ4mu']              = (2, r.kOrange+10, 1001, 1, 'ZZ#rightarrow 4#mu')
styleDict['ZZ4e']               = (2, r.kOrange+9, 1001, 1, 'ZZ#rightarrow 4e')
styleDict['ZZ4tau']             = (2, r.kOrange+8, 1001, 1, 'ZZ#rightarrow 4#tau')
styleDict['ZZ2e2mu']            = (2, r.kOrange+7, 1001, 1, 'ZZ#rightarrow 2e2#mu')
styleDict['ZZ2e2tau']           = (2, r.kOrange+6, 1001, 1, 'ZZ#rightarrow 2e2#tau')
styleDict['ZZ2mu2tau']          = (2, r.kOrange+5, 1001, 1, 'ZZ#rightarrow 2#mu2#tau')

#top
styleDict['top']                = (0, r.kBlue+1, 1001, 1, 't#bar{t}/t')
styleDict['single top']         = (0, r.kBlue+2, 3004, 1, 't')
styleDict['ttbar']              = (0, r.kBlue+0, 1001, 2, 't#bar{t}')
styleDict['ttbarHad']           = (0, r.kBlue+3, 1001, 1, 't#bar{t} (had)')
styleDict['ttbarSemilep']       = (0, r.kBlue+3, 1001, 1, 't#bar{t} (semi-lep)')
styleDict['ttbarLep']           = (0, r.kAzure+2, 1001, 1, 't#bar{t} (lep)')
styleDict['tW']                 = (2, r.kBlue-1, 1001, 1, 'tW')
styleDict['tbarW']              = (2, r.kBlue-2, 1001, 1, '#bar{t}W')
styleDict['t_t-channel']        = (2, r.kBlue-3, 1001, 1, 't (t-channel)')
styleDict['tbar_t-channel']     = (2, r.kBlue-4, 1001, 1, '#bar{t} (t-channel)')

# tt+V
styleDict['ttV']                = (0, r.kGreen+1, 1001, 1, 't#bar{t}V')
styleDict['ttZ']                = (0, r.kGreen+1, 1001, 1, 't#bar{t}Z')
styleDict['ttW']                = (0, r.kGreen+2, 1001, 1, 't#bar{t}W')
styleDict['ttG']                = (0, r.kGreen+3, 1001, 1, 't#bar{t}G')

#triboson
styleDict['Triboson']           = (0, r.kCyan+0, 1001, 1, 'triboson')
styleDict['WWW']                = (0, r.kCyan+0, 1001, 1, 'WWW')
styleDict['WWZ']                = (0, r.kCyan+1, 1001, 1, 'WWZ')
styleDict['WZZ']                = (0, r.kCyan+2, 1001, 1, 'WZZ')
styleDict['ZZZ']                = (0, r.kCyan+3, 1001, 1, 'ZZZ')
styleDict['WWG']                = (0, r.kCyan+4, 1001, 1, 'WWG')

#QCD
styleDict['QCD']                = (2, r.kOrange+3, 1001, 1, 'QCD')
styleDict['QCD_EM']             = (2, r.kOrange+1, 1001, 1, 'QCD e#gamma')
styleDict['QCD_20_MU']          = (2, r.kOrange-1, 1001, 1, 'QCD #mu')

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
styleDict['ZGstar']             = (2, r.kBlue+3, 0, 1, 'Z#gamma^{*}')
styleDict['WWSS']               = (2, r.kBlue+2, 0, 1, 'W^{#pm}W^{#pm}')
styleDict['WmWmqq']             = (2, r.kBlue+2, 0, 1, 'W^{-}W^{-}')
styleDict['WpWppq']             = (2, r.kBlue+4, 0, 1, 'W^{+}W^{+}')
styleDict['WWDPS']              = (2, r.kBlue+5, 0, 1, 'WW (DPS)')
styleDict['TBZ']                = (2, r.kCyan+5, 0, 1, 'tqZ')
styleDict['GJets_15to30']       = (2, r.kYellow+2, 0, 1, 'gamma+jets') 

#Higgs
styleDict['higgs']              = (2, r.kBlue+3, 0, 1, 'higgs')
styleDict['TTH_M-125']          = (2, r.kBlue+3, 0, 1, 'ttH')
styleDict['ggHToZZ4L_M-125']    = (2, r.kBlue+3, 0, 1, 'H#rightarrow 4l')

#Misc
styleDict['BGERROR']            = (0, r.kBlack, 3003, 0, 'BG uncertainty')
#styleDict['FCNH']               = (3, r.kRed+3, 0, 20, 'FCNH (#times 2)')
styleDict['FCNH']               = (3, r.kRed+3, 0, 0, 't#rightarrow Hc') # (BR = {0:1.0%})'.format(signalScale))
styleDict['FCNHWW']             = (3, r.kRed+3, 0, 0, 't#rightarrow Hc #rightarrow WW')
styleDict['FCNHZZ']             = (3, r.kRed+3, 0, 0, 't#rightarrow Hc #rightarrow ZZ')
styleDict['FCNHTauTau']         = (3, r.kRed+3, 0, 0, 't#rightarrow Hc #rightarrow #tau#tau')
#styleDict['FCNHUp']             = (3, r.kBlue+3, 0, 0, 't#rightarrow Hu (BR = {0:1.0\%})'.format(signalScale))
styleDict['FCNHUp']             = (3, r.kBlue+3, 0, 0, 't#rightarrow Hu')# (BR = {0:1.0%})'.format(signalScale))
styleDict['FCNHUpWW']           = (3, r.kBlue+3, 0, 0, 't#rightarrow Hu #rightarrow WW')
styleDict['FCNHUpZZ']           = (3, r.kBlue+3, 0, 0, 't#rightarrow Hu #rightarrow ZZ')
styleDict['FCNHUpTauTau']       = (3, r.kBlue+3, 0, 0, 't#rightarrow Hu #rightarrow #tau#tau')

styleDict['SUM_EFF']            = (2, r.kBlue, 1001, 21, 'BG')
styleDict['SIG_EFF']            = (2, r.kRed, 1001, 21, 'Signal')
styleDict['SIGNIFICANCE']       = (2, r.kGreen, 1001, 21, 'Signficance')
styleDict['RATIO']              = (0, r.kBlack, 3002, 20, 'Ratio')
styleDict['AVG']                = (0, r.kBlue, 3005, 0, 'Average')
styleDict['AIC']                = (2, r.kCyan+2, 1001, 20, 'AIC')

styleDict['eeeAIC']             = (2, r.kCyan+2, 1001, 20, 'AIC')
styleDict['eemuAIC']            = (2, r.kCyan+2, 1001, 20, 'AIC')
styleDict['emumuAIC']           = (2, r.kCyan+2, 1001, 20, 'AIC')
styleDict['mumumuAIC']          = (2, r.kCyan+2, 1001, 20, 'AIC')
styleDict['Fakes']              = (2, r.kRed-3, 1001, 20, 'Non-prompt')
styleDict['eFakes']             = (2, r.kCyan, 3001, 20, 'Fakes e')
styleDict['muFakes']            = (2, r.kMagenta+3, 3001, 20, 'Fakes #mu')
styleDict['llFakes']            = (2, r.kViolet+9, 3001, 1, 'Fakes ll')
styleDict['QFlips']             = (2, r.kAzure+2, 1001, 1, 'Charge MisID')
styleDict['Rare']               = (2, r.kYellow+2, 1001, 1, 'Rare')

styleDict['ss_ee']             = (2, r.kCyan, 3001, 20, 'e^{#pm}e^{#pm}')
styleDict['ss_mumu']           = (2, r.kRed-1, 3001, 20, '#mu^{#pm}#mu^{#pm}')
styleDict['ss_emu']            = (2, r.kViolet+9, 3001, 1, 'e^{#pm}#mu^{#pm}')
styleDict['3l_inclusive']      = (2, r.kGreen-2, 3001, 1, 'trilepton')


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
scaleDict['2011']['ttbarHad']           = 165*30*70
scaleDict['2011']['ttbarLep']           = 165*30*30
scaleDict['2011']['tW']                 = 7.87
scaleDict['2011']['tbarW']              = 7.87

scaleDict['2011']['DYToMuMu']           = 1666.
scaleDict['2011']['DYToEE']             = 1666.
scaleDict['2011']['DYToTauTau']         = 1666.
scaleDict['2011']['ZZ']                 = 0.214
scaleDict['2011']['WZ']                 = 0.596
scaleDict['2011']['WW']                 = 4.51
scaleDict['2011']['GluGluWW']           = 0.1505
scaleDict['2011']['WJetsToLNu']         = 31314
scaleDict['2011']['ZGToNuNu']           = 3.462

scaleDict['2011']['FCNC_M125_t']        = 0.004#*20
scaleDict['2011']['FCNC_M125_tbar']     = 0.004#*20

scaleDict['2011']['DATA_MUON']          = 1.
scaleDict['2011']['DATA_ELECTRON']      = 1.
scaleDict['2011']['DATA_MUEG']          = 1.
scaleDict['2011']['Fakes']              = 1.
scaleDict['2011']['QFlips']             = 1.

### 2012 x-sections
scaleDict['2012']['WJetsToLNu']         = 36257.
scaleDict['2012']['W1JetsToLNu']        = 0.5*17754.
scaleDict['2012']['W2JetsToLNu']        = 0.5*10744.
scaleDict['2012']['W3JetsToLNu']        = 0.5*6432.
scaleDict['2012']['W4JetsToLNu']        = 0.5*3747.
scaleDict['2012']['WbbToLNu']           = 39.9 
scaleDict['2012']['WG']                 = 461.6 # Find the right number for this
scaleDict['2012']['WGStarLNu2E']        = 5.873
scaleDict['2012']['WGStarLNu2Mu']       = 1.914
scaleDict['2012']['WGStarLNu2Tau']      = 0.336
scaleDict['2012']['ZJets_M-50']         = 3532.8 
scaleDict['2012']['ZJets_M-10To50']     = 860.5
scaleDict['2012']['ZbbToLL']            = 94.1 #* 10 
scaleDict['2012']['ZG']                 = 159.12

scaleDict['2012']['ZZJets2L2Nu']        = 0.365
scaleDict['2012']['ZZJets2L2Q']         = 1.28
scaleDict['2012']['ZZJets4L']           = 0.0921
scaleDict['2012']['WZJets3LNu']         = 1.086 
scaleDict['2012']['WZJets2L2Q']         = 5.09
scaleDict['2012']['WWJets2L2Nu']        = 5.995

scaleDict['2012']['ttbar']              = 252
scaleDict['2012']['ttbarHad']           = 252
scaleDict['2012']['ttbarSemilep']       = 252
scaleDict['2012']['ttbarLep']           = 252
scaleDict['2012']['tW']                 = 11.177
scaleDict['2012']['tbarW']              = 11.177
scaleDict['2012']['t_t-channel']        = 55.53
scaleDict['2012']['tbar_t-channel']     = 30.7
scaleDict['2012']['ttW']                = 0.232
scaleDict['2012']['ttZ']                = 0.206
scaleDict['2012']['ttG']                = 2.166

scaleDict['2012']['WWW']                = 0.082
scaleDict['2012']['WWZ']                = 0.063
scaleDict['2012']['WZZ']                = 0.0192
scaleDict['2012']['ZZZ']                = 0.0046
scaleDict['2012']['WWG']                = 0.528

scaleDict['2012']['QCD_20_MU']          = 134680.
scaleDict['2012']['QCD_20-30_EM']       = 2920632.
scaleDict['2012']['QCD_30-80_EM']       = 4615893.
scaleDict['2012']['QCD_80-170_EM']      = 183722
scaleDict['2012']['QCD_170-250_EM']     = 4588
scaleDict['2012']['QCD_250-350_EM']     = 556.75
scaleDict['2012']['QCD_350_EM']         = 89.1
scaleDict['2012']['QCD_15-30_B+MU']     = 0.00004*9.883E8
scaleDict['2012']['QCD_30-50_B+MU']     = 0.00062*6.629E7
scaleDict['2012']['QCD_50-150_B+MU']    = 0.0024*9.2E6
scaleDict['2012']['QCD_150_B+MU']       = 0.0086*50000 # Can't find value for this

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
scaleDict['2012']['ZGToNuNu']           = 3.462
scaleDict['2012']['ZGstar']             = 0.5

scaleDict['2012']['WmWmqq']             = 0.0889
scaleDict['2012']['WpWpqq']             = 0.2482
scaleDict['2012']['WWDPS']              = 0.587
scaleDict['2012']['TBZ']                = 0.0114

scaleDict['2012']['ggHToZZ4L_M-125']    = 19.3*0.0264*0.09*0.09
scaleDict['2012']['WHToWWW3L_M-125']    = .705*0.3*0.3*0.3
scaleDict['2012']['ggHToWW2L2Nu_M-125'] = 19.3*0.215*0.3*0.3
scaleDict['2012']['TTH_M-125']          = .1032

#scaleDict['GJets_15to30']       = 1/0.012
#scaleDict['GJets_30to50']       = 1/0.131
#scaleDict['GJets_50to80']       = 1/0.748
#scaleDict['GJets_80to120']      = 1/4.577
#scaleDict['GJets_120to170']     = 1/24.81
#scaleDict['GJets_170to300']     = 1/91.294
#scaleDict['GJets_300to470']     = 1/1391.1
#scaleDict['GJets_470to800']     = 1/15812.2

scaleDict['2012']['FCNC_M125_t']            = signalScale*252*1.*0.215*3*0.324*0.324
scaleDict['2012']['FCNC_M125_tbar']         = signalScale*252*1.*0.215*3*0.324*0.324
scaleDict['2012']['FCNC_ZZ_t']              = signalScale*252*1.*0.0264*(2*0.1*0.2 + 2*0.1*0.70 + 0.1*0.1)*0.324
scaleDict['2012']['FCNC_ZZ_tbar']           = signalScale*252*1.*0.0264*(2*0.1*0.2 + 2*0.1*0.70 + 0.1*0.1)*0.324
scaleDict['2012']['FCNC_TauTau_t']          = signalScale*252*1.*0.063*0.324
scaleDict['2012']['FCNC_TauTau_tbar']       = signalScale*252*1.*0.063*0.324

scaleDict['2012']['FCNHUp_M125_tbar']       = 2.*signalScale*252*1.*0.215*3*0.324*0.324
scaleDict['2012']['FCNHUp_ZZ_tbar']         = 2.*signalScale*252*1.*0.0264*(2*0.1*0.2 + 2*0.1*0.70 + 0.1*0.1)*0.324
scaleDict['2012']['FCNHUp_TauTau_tbar']     = 2.*signalScale*252*1.*0.063*0.324

scaleDict['2012']['DATA_MUON']          = 1.
scaleDict['2012']['DATA_ELECTRON']      = 1.
scaleDict['2012']['DATA_MUEG']          = 1.
scaleDict['2012']['AIC']                = 1.
scaleDict['2012']['eeeAIC']             = 1.
scaleDict['2012']['eemuAIC']            = 1.
scaleDict['2012']['emumuAIC']           = 1.
scaleDict['2012']['mumumuAIC']          = 1.
scaleDict['2012']['Fakes']              = 1.
scaleDict['2012']['eFakes']             = 1.
scaleDict['2012']['muFakes']            = 1.
scaleDict['2012']['llFakes']            = 1. 
scaleDict['2012']['QFlips']             = 1.

combineDict = {}
combineDict['FCNH']             = ['FCNC_M125_t', 'FCNC_M125_tbar', 'FCNC_ZZ_t', 'FCNC_ZZ_tbar', 'FCNC_TauTau_t', 'FCNC_TauTau_tbar']
combineDict['FCNHUpWW']         = ['FCNHUp_M125_tbar']
combineDict['FCNHUpZZ']         = ['FCNHUp_ZZ_tbar']
combineDict['FCNHUpTauTau']     = ['FCNHUp_TauTau_tbar']
combineDict['FCNHWW']           = ['FCNC_M125_t', 'FCNC_M125_tbar']
combineDict['FCNHZZ']           = ['FCNC_ZZ_t', 'FCNC_ZZ_tbar']
combineDict['FCNHTauTau']       = ['FCNC_TauTau_t', 'FCNC_TauTau_tbar']
combineDict['FCNHUp']           = ['FCNHUp_M125_tbar', 'FCNHUp_ZZ_tbar', 'FCNHUp_TauTau_tbar']
#combineDict['FCNH']             = ['FCNC_M125_t', 'FCNC_M125_t_semilep', 'FCNC_M125_t_ZZ', 'FCNC_M125_t_TauTau']
combineDict['DATA']             = ['DATA_MUON', 'DATA_ELECTRON', 'DATA_MUEG']

combineDict['VJets']            = ['ZJets_M-50', 'ZJets_M-10To50', 'WJetsToLNu']
combineDict['ZJets']            = ['ZJets_M-50', 'ZJets_M-10To50']
combineDict['WJets']            = ['W1JetsToLNu', 'W2JetsToLNu', 'W3JetsToLNu', 'W4JetsToLNu'] 
combineDict['WGstar']           = ['WGStarLNu2Mu', 'WGStarLNu2Tau']#, 'WGStarLNu2E']
combineDict['ttbar']            = ['ttbarHad', 'ttbarLep', 'ttbarSemilep']
combineDict['top']              = ['ttbarHad', 'ttbarLep', 'tW', 'tbarW', 't_t-channel', 'tbar_t-channel']
combineDict['single top']       = ['tW', 'tbarW', 't_t-channel', 'tbar_t-channel']
combineDict['ttV']              = ['ttZ', 'ttW', 'ttG']
combineDict['Diboson']          = ['ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'WWJets2L2Nu', 'WZJets3LNu', 'ZZJets2L2Nu', 'ZZJets2L2Q', 'WZJets2L2Q']
combineDict['WW/ZZ']            = ['ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'WWJets2L2Nu', 'ZZJets2L2Nu']
#combineDict['ZZ4l']             = ['ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau']
combineDict['ZZ4l']             = ['ZZ4mu', 'ZZ4e', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau']
combineDict['VV2l']             = ['ZZJets2L2Nu', 'ZZJets2L2Q', 'WWJets2L2Nu', 'ZZJets2L2Nu', 'WZJets2L2Q']
combineDict['WWSS']             = ['WmWmqq', 'WpWpqq', 'WWDPS']
combineDict['Triboson']         = ['WWW', 'WWZ', 'WZZ', 'ZZZ']#, 'WWG']
combineDict['QCD']              = ['QCD_20_MU', 'QCD_20-30_EM', 'QCD_30-80_EM', 'QCD_80-170_EM', 'QCD_170-250_EM', 'QCD_250-350_EM', 'QCD_350_EM']
#combineDict['QCD']              = ['QCD_15-30_B+MU', 'QCD_30-50_B+MU', 'QCD_50-150_B+MU', 'QCD_150_B+MU', 'QCD_20-30_EM', 'QCD_30-80_EM', 'QCD_80-170_EM', 'QCD_170-250_EM', 'QCD_250-350_EM', 'QCD_350_EM']
combineDict['QCD_EM']           = ['QCD_20-30_EM', 'QCD_30-80_EM', 'QCD_80-170_EM', 'QCD_170-250_EM', 'QCD_250-350_EM', 'QCD_350_EM']
combineDict['higgs']            = ['ggHToZZ4L_M-125', 'WHToWWW3L_M-125', 'ggHToWW2L2Nu_M-125', 'TTH_M-125']

combineDict['AIC']              = ['eeeAIC', 'eemuAIC', 'emumuAIC', 'mumumuAIC']
combineDict['AIC_BG']           = ['WZJets3LNu', 'ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'muFakes', 'eFakes', 'llFakes']
combineDict['Fakes']            = ['eFakes', 'muFakes', 'llFakes']
combineDict['Remove_ss']        = ['ZJets_M-50', 'ZJets_M-10To50', 'ttbarLep']#, 'tW', 'tbarW', 'WWJets2L2Nu', 'ZZJets2L2Nu', 'ZZJets2L2Q']
combineDict['Remove_3l']        = ['WZJets3LNu', 'ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau']#, 'ttZ', 'ttW', 'WWW', 'WWZ', 'WZZ', 'ZZZ']
#combineDict['Irreducible']      = ['ggHToZZ4L_M-125', 'WHToWWW3L_M-125', 'ggHToWW2L2Nu_M-125', 'TTH_M-125', 'WZJets3LNu', 'ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'ttZ', 'ttW', 'ttG', 'WWW', 'WWZ', 'WZZ', 'ZZZ']#, 'WWG']
combineDict['Irreducible']      = ['WZJets3LNu', 'ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'ttZ', 'ttW', 'ttG', 'WWW', 'WWZ', 'WZZ', 'ZZZ']#, 'WWG']
combineDict['Rare']             = ['ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 'ttZ', 'ttW', 'ttG', 'WWW', 'WWZ', 'WZZ', 'ZZZ', 'WmWmqq', 'WpWpqq', 'WWDPS', 'TBZ', 'TTH_M-125']
combineDict['PROMPT']           = [
                                   'ZJets_M-50', 'ZJets_M-10To50',
                                   'W1JetsToLNu', 'W2JetsToLNu', 'W3JetsToLNu', 'W4JetsToLNu', 
                                   'ttbarLep', 'ttbarSemilep', 
                                   'WZJets3LNu', 
                                   'ZZ4mu', 'ZZ4e', 'ZZ4tau', 'ZZ2e2mu', 'ZZ2mu2tau', 'ZZ2e2tau', 
                                   'ttZ', 'ttW', 'ttG', 
                                   'WWW', 'WWZ', 'WZZ', 'ZZZ'
                                   ]

combineDict['DATA_FAKES']       = combineDict['DATA']
combineDict['PASS']             = combineDict['DATA']
combineDict['FAKEABLE']         = combineDict['DATA']


categoryDict = {'inclusive':'inclusive',
                'ss_inclusive':'same-sign dilepton', 'ss_mumu':'#mu^{#pm}#mu^{#pm}', 'ss_ee':'e^{#pm}e^{#pm}', 'ss_emu':'e^{#pm}#mu^{#pm}',
                'ss_endcap':'same-sign (EE)', 'ss_mixed':'same-sign (EB)', 'ss_barrel':'same-sign (BB)',
                'os_inclusive':'os dilepton', 'os_mumu':'#mu^{#pm}#mu^{#mp}', 'os_ee':'e^{#pm}e^{#mp}', 'os_emu':'e^{#pm}mu^{#mp}', 
                '3l_inclusive':'trilepton', '3l_OSSF':'(l^{#pm}l^{#mp})l', '3l_SSSF':'(l^{#pm}l^{#pm})l',
                '3l_eee':'eee', '3l_eemu':'ee#mu', '3l_emumu':'e#mu#mu','3l_mumumu':'#mu#mu#mu',
                'AntiIso3l':'Anti-Iso CR', 'QCD2l':'QCD ll', 'ZPlusJet':'Z+jet',
                'PureLep':'Pure Muon', 'SameSign':'l^{#pm}l^{#pm}',
                'low_met':'MET < 20', 'high_met':'45 < MET < 80'
                }

systDict    = {'ss_inclusive':{}, 'ss_ee':{}, 'ss_emu':{}, 'ss_mumu':{}, 'ss_barrel':{}, 'ss_mixed':{}, 'ss_endcap':{}, 
               '3l_inclusive':{}, '3l_eee':{}, '3l_eemu':{}, '3l_emumu':{}, '3l_mumumu':{}}

# same-sign dileptons systematics          [lumi,   jes,    MET,  pileup,  mu_eff, el_eff, mu_trig, el_trig, qFlips, mufakes, elFakes, PDF,     ttbar, ttW,  ttZ,   WZ]
systDict['ss_inclusive']['Irreducible'] =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.03,   0.01,    0.02,    0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_inclusive']['ttW']         =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.03,   0.01,    0.02,    0.,     0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['ss_inclusive']['ttZ']         =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.03,   0.01,    0.02,    0.,     0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['ss_inclusive']['WZJets3LNu']  =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.03,   0.01,    0.02,    0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['ss_inclusive']['fcnh']        =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.03,   0.01,    0.02,    0.,     0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['ss_inclusive']['muFakes']     =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_inclusive']['eFakes']      =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['ss_inclusive']['llFakes']     =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.3,     0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['ss_inclusive']['QFlips']      =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.2,    0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_ee']['Irreducible']        =  [0.026,  0.005,  0.04, 0.01,    0.,     0.04,   0.,      0.02,    0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_ee']['ttW']                =  [0.026,  0.005,  0.04, 0.01,    0.,     0.04,   0.,      0.02,    0.,     0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['ss_ee']['ttZ']                =  [0.026,  0.005,  0.04, 0.01,    0.,     0.04,   0.,      0.02,    0.,     0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['ss_ee']['WZJets3LNu']         =  [0.026,  0.005,  0.04, 0.01,    0.,     0.04,   0.,      0.02,    0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['ss_ee']['fcnh']               =  [0.026,  0.005,  0.04, 0.01,    0.,     0.04,   0.,      0.02,    0.,     0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['ss_ee']['muFakes']            =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_ee']['eFakes']             =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['ss_ee']['llFakes']            =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['ss_ee']['QFlips']             =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.2,    0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_emu']['Irreducible']       =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.02,   0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_emu']['ttW']               =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.02,   0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['ss_emu']['ttZ']               =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.02,   0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['ss_emu']['WZJets3LNu']        =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.02,   0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['ss_emu']['fcnh']              =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.02,   0.01,    0.,      0.,     0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['ss_emu']['muFakes']           =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_emu']['eFakes']            =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['ss_emu']['llFakes']           =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.3,     0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['ss_emu']['QFlips']            =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.2,    0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_mumu']['Irreducible']      =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.,     0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_mumu']['ttW']              =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.,     0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['ss_mumu']['ttZ']              =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.,     0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['ss_mumu']['WZJets3LNu']       =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.,     0.01,    0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['ss_mumu']['fcnh']             =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.,     0.01,    0.,      0.,     0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['ss_mumu']['muFakes']          =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_mumu']['eFakes']           =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_mumu']['llFakes']          =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['ss_mumu']['QFlips']           =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,     0.,      0.,      0.,      0.,    0.,   0.,    0.  ]

# same-sign dileptons systematics          [lumi,   jes,    MET,  pileup,  mu_eff, el_eff, mu_trig, el_trig, mufakes, elFakes, PDF,     ttbar, ttW,  ttZ,   WZ]
systDict['3l_inclusive']['Irreducible'] =  [0.026,  0.005,  0.04, 0.01,    0.015,  0.03,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_inclusive']['ttW']         =  [0.026,  0.005,  0.04, 0.01,    0.015,  0.03,   0.,      0.,      0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['3l_inclusive']['ttZ']         =  [0.026,  0.005,  0.04, 0.01,    0.015,  0.03,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['3l_inclusive']['WZJets3LNu']  =  [0.026,  0.005,  0.04, 0.01,    0.015,  0.03,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['3l_inclusive']['fcnh']        =  [0.026,  0.005,  0.04, 0.01,    0.015,  0.03,   0.,      0.,      0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['3l_inclusive']['muFakes']     =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_inclusive']['eFakes']      =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_inclusive']['llFakes']     =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eee']['Irreducible']       =  [0.026,  0.005,  0.04, 0.01,    0.,     0.06,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eee']['ttW']               =  [0.026,  0.005,  0.04, 0.01,    0.,     0.06,   0.,      0.,      0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['3l_eee']['ttZ']               =  [0.026,  0.005,  0.04, 0.01,    0.,     0.06,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['3l_eee']['WZJets3LNu']        =  [0.026,  0.005,  0.04, 0.01,    0.,     0.06,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['3l_eee']['fcnh']              =  [0.026,  0.005,  0.04, 0.01,    0.,     0.06,   0.,      0.,      0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['3l_eee']['muFakes']           =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eee']['eFakes']            =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eee']['llFakes']           =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eemu']['Irreducible']      =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.04,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eemu']['ttW']              =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.04,   0.,      0.,      0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['3l_eemu']['ttZ']              =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.04,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['3l_eemu']['WZJets3LNu']       =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.04,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['3l_eemu']['fcnh']             =  [0.026,  0.005,  0.04, 0.01,    0.01,   0.04,   0.,      0.,      0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['3l_eemu']['muFakes']          =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eemu']['eFakes']           =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_eemu']['llFakes']          =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_emumu']['Irreducible']     =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.02,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_emumu']['ttW']             =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.02,   0.,      0.,      0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['3l_emumu']['ttZ']             =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.02,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['3l_emumu']['WZJets3LNu']      =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.02,   0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['3l_emumu']['fcnh']            =  [0.026,  0.005,  0.04, 0.01,    0.02,   0.02,   0.,      0.,      0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['3l_emumu']['muFakes']         =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_emumu']['eFakes']          =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,      0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_emumu']['llFakes']         =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.4,     0.,      0.,    0.,   0.,    0.  ]
systDict['3l_mumumu']['Irreducible']    =  [0.026,  0.005,  0.04, 0.01,    0.03,   0.,     0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_mumumu']['ttW']            =  [0.026,  0.005,  0.04, 0.01,    0.03,   0.,     0.,      0.,      0.,      0.,      0.,      0.,    0.11, 0.,    0.  ]
systDict['3l_mumumu']['ttZ']            =  [0.026,  0.005,  0.04, 0.01,    0.03,   0.,     0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.13,  0.  ]
systDict['3l_mumumu']['WZJets3LNu']     =  [0.026,  0.005,  0.04, 0.01,    0.03,   0.,     0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.01]
systDict['3l_mumumu']['fcnh']           =  [0.026,  0.005,  0.04, 0.01,    0.03,   0.,     0.,      0.,      0.,      0.,      0.06,    0.01,  0.,   0.,    0.  ]
systDict['3l_mumumu']['muFakes']        =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_mumumu']['eFakes']         =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.,      0.,      0.,      0.,    0.,   0.,    0.  ]
systDict['3l_mumumu']['llFakes']        =  [0.,     0.005,  0.,   0.,      0.,     0.,     0.,      0.,      0.3,     0.,      0.,      0.,    0.,   0.,    0.  ]

paramFile = open('scripts/fcncParams.pkl', 'wb')
pickle.dump(styleDict, paramFile)
pickle.dump(scaleDict, paramFile)
pickle.dump(combineDict, paramFile)
pickle.dump(categoryDict, paramFile)
pickle.dump(systDict, paramFile)
paramFile.close()
