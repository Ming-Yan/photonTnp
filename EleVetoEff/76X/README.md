myrun_HZg_all_MC.C  -> runs xAna.cc; stores the needed FSR photons

combine dataC.root and dataD.root by using "hadd -f data.root dataC.root dataD.root"

run.C -> runs analyse3.c and generates a table (.csv file) for the scaling factors and root files for the kinematics plots

to draw the kinematics plots, move to the folder "plotcode"

*note: don't compile when running the run files; e.g. .x run.C and NOT .x run.C++

*if you have more pT/eta bins, use analyse3plots.c to plot the scaling factors as histograms