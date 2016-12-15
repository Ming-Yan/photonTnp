#!/bin/bash

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --createHists

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --createHists

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --createHists

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA --createHists

