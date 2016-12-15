#!/bin/bash

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --doFit
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --doFit --mcSig --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --doFit --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --doFit --altBkg


python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --doFit
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --doFit --mcSig --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --doFit --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --doFit --altBkg


python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --doFit
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --doFit --mcSig --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --doFit --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --doFit --altBkg


python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA --doFit
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA --doFit --mcSig --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA --doFit --altSig
python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA --doFit --altBkg


