#!/bin/bash

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose --createHists

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium --createHists

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight --createHists

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose80X --createHists

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium80X --createHists

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight80X --createHists

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA80Xwp80 --createHists

#python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA80Xwp90 --createHists

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingLoose80X --createHists --sample mcAlt

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMedium80X --createHists --sample mcAlt

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingTight80X --createHists --sample mcAlt

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA80Xwp80 --createHists --sample mcAlt

python tnpEGM_fitter.py etc/config/settings_pho.py --flag passingMVA80Xwp90 --createHists --sample mcAlt