myrun_HZg_all_MC.C  -> runs xAna.cc; stores the needed FSR photons

run.C -> runs analyse3.c and generates a table (.csv file) for the scaling factors and root files for the kinematics plots

to draw the kinematics plots, move tdrstyle.C, CMS_lumi.C/h, run.c, and xHistosCombine.C to a subfolder

run.c

*note: don't compile when running the run files; e.g. .x run.C NOT .x run.C++