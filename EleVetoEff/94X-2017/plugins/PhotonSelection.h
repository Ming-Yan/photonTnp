bool PhotonSelection(TreeReader& data, int i)
{
  Int_t  nPho       = data.GetInt("nPho");
  float* phoE      = data.GetPtrFloat("phoE");
  float* phoEt      = data.GetPtrFloat("phoEt");
  float* phoCalibEt = data.GetPtrFloat("phoCalibEt"); // calibrated photon pT
  float* phoEta     = data.GetPtrFloat("phoEta");
  float* phoPhi     = data.GetPtrFloat("phoPhi");
  float* phoSCEta   = data.GetPtrFloat("phoSCEta");
  float* phoIDMVA   = data.GetPtrFloat("phoIDMVA");
  Int_t* phoEleVeto = data.GetPtrInt("phoEleVeto");

  bool PassKinematics = false;
  PassKinematics = ( (fabs(phoSCEta[i]) < 2.5) && (fabs(phoSCEta[i]) < 1.4442 || fabs(phoSCEta[i]) > 1.566) );
  bool PassEleVeto = false;
  PassEleVeto = (phoEleVeto[i] == 1);
  bool PassPhoMVA = false;
  
  if(fabs(phoSCEta[i]) < 1.4442) 
    PassPhoMVA = (phoIDMVA[i] > 0.2);
    //PassPhoMVA = (phoIDMVA[i] < 0.2); // revert photon MVA
    //PassPhoMVA = (phoIDMVA[i] > -1.0);
  else
    PassPhoMVA = (phoIDMVA[i] > 0.2);
    //PassPhoMVA = (phoIDMVA[i] < 0.2); 
    //PassPhoMVA = (phoIDMVA[i] > -1.0);
  
  return (PassKinematics && PassEleVeto && PassPhoMVA);
}
