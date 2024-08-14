import os
import pandas as pd
import subprocess
#Make obabel available first

inputfolder = '/Users/febrinam/Documents/INBIO/Docking/Separated'
outputfolder = '/Users/febrinam/Documents/NIGINTERN/DTIScreening/Screened'
listofdrugs = pd.read_csv('/Users/febrinam/Documents/NIGINTERN/DTIScreening/ProteinDrugScreeningData/gbi_03726_ra.csv')['drugbank_id'].tolist()

for file in os.listdir(inputfolder): 
    if file.endswith(".sdf"):
        drug_id = file.replace(".sdf", "")
        if drug_id in listofdrugs:
            file_path = os.path.join(inputfolder, file)
            command = f"obabel {file_path} -omol2 -O {outputfolder}/{drug_id}.mol2"
            subprocess.run(command, shell=True, check=True)
