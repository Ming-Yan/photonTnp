#!/bin/bash 


python getTemplatesFromMC.py --input /data2/pwang/TnP/76X_PU/65550/TnP_MC_PO_PU65550.root -o templatesLoose_PU65550.root --idprobe Loose --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO

python getTemplatesFromMC.py --input /data2/pwang/TnP/76X_PU/65550/TnP_MC_PO_PU65550.root -o templatesMedium_PU65550.root --idprobe Medium --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO

python getTemplatesFromMC.py --input /data2/pwang/TnP/76X_PU/65550/TnP_MC_PO_PU65550.root -o templatesTight_PU65550.root --idprobe Tight --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO

python getTemplatesFromMC.py --input /data2/pwang/TnP/76X_PU/65550/TnP_MC_PO_PU65550.root -o templatesMVA_PU65550.root --idprobe MVA --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO



#python getTemplatesFromMC_35pTCut.py --input /data2/pwang/TnP/76X_v2/TnP_MC_PO.root -o templatesLoose_35pTCut.root --idprobe Loose --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO

#python getTemplatesFromMC_35pTCut.py --input /data2/pwang/TnP/76X_v2/TnP_MC_PO.root -o templatesMedium_35pTCutroot --idprobe Medium --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO

#python getTemplatesFromMC_35pTCut.py --input /data2/pwang/TnP/76X_v2/TnP_MC_PO.root -o templatesTight_35pTCut.root --idprobe Tight --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO

#python getTemplatesFromMC_35pTCut.py --input /data2/pwang/TnP/76X_v2/TnP_MC_PO.root -o templatesMVA_35pTCut.root --idprobe MVA --weightVarName totWeight --ptbins=20,30,40,50,200 --etabins=-2.5,-1.566,-1.4442,-1,0,1,1.4442,1.566,2.5 --etaVarName=probe_sc_eta --directory PhotonToRECO
