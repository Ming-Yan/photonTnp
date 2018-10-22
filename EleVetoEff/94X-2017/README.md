## Electron veto scale factors measurement for 2017 data ##

All the plots can be found in https://hjheng.web.cern.ch/hjheng/EleVeto_2017/

#### Usage ####
- Run ntuples: `root -l -q -b run_XXX.C++`
    - (On pcncu) run_data.C, run_mc_DYJets_aMCatNLO.C
    - (On lxplus, /eos directory) run_mc_WJets_MG.C, run_mc_ttbar.C, run_mc_DYJetsToLL_MG.C
- Produce plots: 
    - `root -l -q -b MakeSimpleHist.C`: Efficiency dependence on nVtx/photon E<sub>2T/sub>
    - `root -l -q -b MakeCombHist.C`: Summary plots
    - `root -l -q -b DrawKinematics.C`: Kinematic plots 
    - `root -l -q -b Draw_PUcheck.C\([IDtype], [EleVetoSet]\)`: Study of pile-up weights
        - IDtype: **1**-->Loose; **2**-->Medium; **3**-->Tight; **4**-->General purpose MVA 
        - EleVetoSet: **1**-->Pixel seed veto; **2**-->Conversion safe veto
    
#### TO-DO #### 
- [ ] Make a script to run all macros