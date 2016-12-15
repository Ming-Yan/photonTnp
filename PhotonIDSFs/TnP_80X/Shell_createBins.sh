#!/bin/bash

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --createBins

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --createBins

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --createBins

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA --createBins

