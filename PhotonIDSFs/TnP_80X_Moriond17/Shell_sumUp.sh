#!/bin/bash

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose80X --sumUp

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium80X --sumUp

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight80X --sumUp

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA80Xwp80 --sumUp

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA80Xwp90 --sumUp
