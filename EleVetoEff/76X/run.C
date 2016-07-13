#include <iostream>
#include <fstream>
#include <TSystem.h>
#include <TROOT.h>

void run(){

	gROOT->LoadMacro("analyse3.c");

	std::ofstream outputFile;
	outputFile.open("values.csv");

	TString IDtype[4] = { "Loose", "Medium", "Tight", "MVA" };
	TString CutType[2] = { "HasPix", "CSEV" };
	TString region[2] = { "EB", "EE" };
	TString R9Type[3] = { "GT", "LT", "Inc" };

	for (int i = 0; i < 4; i++){
		for (int j = 0; j < 2; j++){
			for (int k = 0; k < 2; k++){
				for (int l = 0; l < 3; l++){

					double hsval, hdval, hserr, hderr, sferr, sfval;

					analyse3(IDtype[i], CutType[j], R9Type[l], region[k], 0, &hdval, &hsval, &sfval, &hderr, &hserr, &sferr);//puType: 0,1,2 -> puwei, up, down

					outputFile << std::fixed << setprecision(4);

					if (j == 0 && l == 0 && k == 0) outputFile << IDtype[i] << std::endl;
					if (k == 0 && l == 0) outputFile << CutType[j] << std::endl;
					if (l == 0 && k == 0) outputFile << region[k];
					if (l == 0 && k == 1) outputFile << endl << region[k];

					outputFile << "," << R9Type[l] << "," << hdval << " +/- " << hderr <<
						"," << hsval << " +/- " << hserr <<
						"," << sfval << " +/- " << sferr << std::endl;

					/*outputFile << IDtype[i] << CutType[j] << region[k] << "," << R9Type[l] << "," << hdval << " +/- " << hderr <<
						"," << hsval << " +/- " << hserr <<
						"," << sfval << " +/- " << sferr << std::endl;*/

					/*outputFile << "data" << IDtype[i] << CutType[j] << R9Type[k] << region[l] << hdval << hderr << std::endl;
					outputFile << "MC" << IDtype[i] << CutType[j] << R9Type[k] << region[l] << hsval << hserr << std::endl;
					outputFile << "SF" << IDtype[i] << CutType[j] << R9Type[k] << region[l] << sfval << sferr << std::endl;*/
				}
			}
		}
	}
	outputFile.close();
}