#!/bin/bash

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --sumUp

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --sumUp

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --sumUp

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA --sumUp

