import ROOT
from optparse import OptionParser
import sys

def makeTable(h, tablefilename):
    nX = h.GetNbinsX()
    nY = h.GetNbinsY()
  
    print "Writing...", tablefilename
    f = open(tablefilename, "w+")

    for i in xrange(1, nX+1):
    
        pT0 = h.GetXaxis().GetBinLowEdge(i)
        pT1 = h.GetXaxis().GetBinLowEdge(i+1)
    
        for j in xrange(1, nY+1):
            x    = h.GetBinContent(i,j)
            dx   = h.GetBinError(i,j)
            eta0 = h.GetYaxis().GetBinLowEdge(j)
            eta1 = h.GetYaxis().GetBinLowEdge(j+1)
      
            f.write("%4.1f  %4.1f   %+6.4f   %+6.4f  %6.4f   %6.4f \n" %(pT0, pT1, eta0, eta1, x, dx))
  
    f.close()


def main(options):

    print "##################################################   "
    print "starting ... what is options.cc", options.cc
    if(options.cc):
        print "Plotting efficiency from cut & count. No background subtraction performed !"
        print "If you want to plot MC truth efficiency, please set: isMCTruth = true."
    else:
        print "Plotting efficiency from simultaneous fit."
        print "##################################################   "
        

    
    print "opening file", options.input
    f = ROOT.TFile(options.input)
    f.cd(options.directory)


    keyList = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
    print "printint keylist", keyList
    for k in keyList:

        print "name of hte keylist is ",k
        if (not options.isMCTruth and "MCtruth" in k):
            continue
        if (options.isMCTruth and not "MCtruth" in k):
            continue        

        print "directory at this point is : ", ROOT.gDirectory.GetName()
        obj = ROOT.gDirectory.GetKey(k).ReadObj();
        name = obj.GetName()

        if (not obj.IsA().InheritsFrom("TDirectory")):
            continue

        etbin = "0"
        etabin = "0"

#        for etbin in range(0,1):
#            for etabin in range(0,1):
#                print  "   ==================================================   "
#                print "et,eta",etbin,etabin
                #dirName = "%s/probe_sc_et_bin%s__probe_sc_eta_bin%s__mcTrue_true__pdfSignalPlusBackground"%(name,etbin,etabin)
                #dirName = "%s/probe_sc_et_bin%s__probe_sc_eta_bin%s__pdfSignalPlusBackground"%(name,etbin,etabin)
#                dirName = "%s/probe_sc_abseta_bin%s__probe_sc_et_bin%s__pdfSignalPlusBackground"%(name,etbin,etabin)
#                print "dirname", dirName
#                originalDir = ROOT.gDirectory.GetName()
#                pwd = ROOT.gFile.pwd()
#                print "original directory is ",originalDir
#                print "path is ",pwd
#                ROOT.gDirectory.cd(dirName)
#                keyList2 = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
#                tableDone = False
#                for k in  keyList2:
#                    obj = ROOT.gDirectory.GetKey(k).ReadObj();
#                    innername = obj.GetName()
#                    if (obj.ClassName() == "TCanvas"):
#                        for p in obj.GetListOfPrimitives():
#                            print "list of primitives ",p
                            #                    if (p.ClassName() == "TH2F" and not tableDone):
                            #                        makeTable(p, name+".txt")
                            #                        tableDone = True
#                            obj.Draw()
#                            innername = innername.replace("&", "")            
#                            print innername
#                            plotname = name + innername + ".png"
#                            plotname = "%s_%s_etbin%s_etabin%s.png"%(innername,name,etbin,etabin)
#                            obj.SaveAs(plotname)
                            #motherDirName = ROOT.gDirectory.GetMotherDir.GetName()
                #print "name of mother dir is ", motherDirName
#                tmpmotherDir = ROOT.gDirectory.GetMotherDir()
#                motherDir = tmpmotherDir.GetMotherDir()
#                motherDir.GetName()
#                print "mother directory name is ",motherDir.GetName()
#                motherDir.cd()
                #ROOT.gDirectory.GetMotherDir.cd()

        print  "   ==================================================   "
        dirName = "%s/cnt_eff_plots/"%(name)
        if(not options.cc):
            dirName = "%s/fit_eff_plots/"%(name)
            
        print "****************************dirName = ", dirName
        ROOT.gDirectory.cd(dirName)
        keyList2 = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
        tableDone = False
        print "keyList2 ", keyList2
        for k in  keyList2:
            print "k is ", k
            if (not "probe_sc_et_probe_sc_eta_PLOT" in k and not "probe_sc_abseta_probe_sc_et_PLOT_mcTrue_true" in k):
                continue
            obj = ROOT.gDirectory.GetKey(k).ReadObj();
            innername = obj.GetName()
            if (obj.ClassName() == "TCanvas"):
                for p in obj.GetListOfPrimitives():
                    print "list of primitives ",p
                    if (p.ClassName() == "TH2F" and not tableDone):
                        makeTable(p, name+".txt")
                        tableDone = True
                print "is table done", tableDone
                obj.Draw()
                innername = innername.replace("&", "")            
                plotname = name+"_"+innername + ".png"
                print "what is the plotname", plotname
                obj.SaveAs(plotname)
            print "options.cc", options.cc

            if(not options.cc):
                ROOT.gDirectory.cd("../")
                keyList = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
                for k in  keyList:
                    obj = ROOT.gDirectory.GetKey(k).ReadObj();
                    innername = obj.GetName()
                    if (not obj.IsA().InheritsFrom("TDirectory") or not "_bin" in innername):
                        continue
                    #if( "probe_sc_abseta_bin2__probe_sc_et_bin" in innername ):
                    if( "probe_sc_et_bin0__probe_sc_eta_bin1" in innername ):
                        continue
                    if( "probe_sc_et_bin0__probe_sc_eta_bin1" in innername ):
                        continue
                    if( "probe_sc_et_bin1__probe_sc_eta_bin1" in innername ):
                        continue
                    if( "probe_sc_et_bin2__probe_sc_eta_bin1" in innername ):
                        continue
                    if( "probe_sc_et_bin3__probe_sc_eta_bin1" in innername ):
                        continue
                    
                    if( "probe_sc_et_bin0__probe_sc_eta_bin6" in innername ):
                        continue
                    if( "probe_sc_et_bin1__probe_sc_eta_bin6" in innername ):
                        continue
                    if( "probe_sc_et_bin2__probe_sc_eta_bin6" in innername ):
                        continue
                    if( "probe_sc_et_bin3__probe_sc_eta_bin6" in innername ):
                        continue

                    
                    ROOT.gDirectory.cd(innername)
                    c = ROOT.gDirectory.Get("fit_canvas")
                    c.Draw()
                    plotname = "fit" + name + "_" + innername + ".png"
                    pltoname = plotname.replace("probe_sc_", "")
                    plotname = plotname.replace("&", "")
                    plotname = plotname.replace("__pdfSignalPlusBackground", "")
                    c.SaveAs(plotname)
                    ROOT.gDirectory.cd("../")
                    print "saving fit ... at this point name of the directory is ",ROOT.gDirectory.GetName()
            if(not options.cc): 
                ROOT.gDirectory.cd("../")
                #ROOT.gDirectory.cd("../../")
                print "at this point, name of the directory is ",ROOT.gDirectory.GetName()
            else:
                ROOT.gDirectory.cd("../../")
                
            print "   ==================================================   "




#    if(not options.cc):
#        ROOT.gDirectory.cd("../")
#        keyList = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
#        for k in  keyList:
#            obj = ROOT.gDirectory.GetKey(k).ReadObj();
#            innername = obj.GetName()
#            if (not obj.IsA().InheritsFrom("TDirectory") or not "_bin" in innername):
#                continue
#            ROOT.gDirectory.cd(innername)
#            c = ROOT.gDirectory.Get("fit_canvas")
#            c.Draw()
#            plotname = "fit" + name + "_" + innername + ".png"
#            pltoname = plotname.replace("probe_sc_", "")
#            plotname = plotname.replace("&", "")
#            plotname = plotname.replace("__pdfSignalPlusBackground", "")
#            c.SaveAs(plotname)
#            ROOT.gDirectory.cd("../")
#            print "saving fit ... at this point name of the directory is ",ROOT.gDirectory.GetName()
#    if(not options.cc): 
#        ROOT.gDirectory.cd("../")
#        #ROOT.gDirectory.cd("../../")
#        print "at this point, name of the directory is ",ROOT.gDirectory.GetName()
#    else:
#        ROOT.gDirectory.cd("../../")

#    print "   ==================================================   "


if (__name__ == "__main__"):
    parser = OptionParser()
    parser.add_option("-i", "--input", default="efficiency-mc-GsfElectronToId.root", help="Input filename")
    parser.add_option("-d", "--directory", default="GsfElectronToRECO", help="Directory with workspace")
    parser.add_option("-c", dest="cc", action="store_true", help="Is simple Cut and Count", default=False)
    parser.add_option("-b", dest="batch", action="store_true", help="ROOT batch mode", default=False)
    parser.add_option("-m", dest="isMCTruth", action="store_true", help="Subdirectory with results", default=False)

    (options, arg) = parser.parse_args()

    if (options.batch):
        ROOT.gROOT.SetBatch(True)

    main(options)


