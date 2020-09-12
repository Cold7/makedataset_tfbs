"""
usage: active_promoters.py [-h] -g GENOME [-f FRAGMENT] [-o OUTPUT]
                           [-fm {score,percentage}] -cf CLASS_FILE -cd
                           CLASS_DEFINITION [-Cb {0,1}]
active_promoters.py: error: the following arguments are required: -g/--genome, -cf/--class_File, -cd/--class_definition

"""

from glob import glob
from os import system as s
if __name__ == "__main__":
	fragments = ["100"]
	
	Class = "promoter"

	folders = glob("../00_epigenomas/encode_reference_epigenome/*/")
	folders.remove("../00_epigenomas/encode_reference_epigenome/pythonScripts/")

	for fragment in fragments:
		for folder in folders:
			cell = folder.split("/")[-2]
			command = "python3.6 ../01_make_central_vectors/active_promoters.py "
			command += "-g ../00_epigenomas/encode_reference_epigenome/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta "
			command += "-f "+fragment+" "
			command += "-Cb 1 " #due data came from ensembl instead of encode
			command += "-cd  ../00_epigenomas/genome_features/hocomoco_core/final_promoter "
			if cell == "H1":
				command += "-cf path_tfs/H1 "
			elif cell == "GM12878":
				command += "-cf path_tfs/GM12878 "
			elif cell == "K562":
				command += "-cf path_tfs/K562 "
			elif cell == "HeLa-S3":
				command += "-cf path_tfs/HeLa-S3 "
			elif cell == "HepG2":
				command += "-cf path_tfs/HepG2 "

#			f = open("a.sh","w")
#			f.write("#!/bin/bash\n")
#			f.write("#SBATCH --job-name="+cell+"\n")
#			f.write("#SBATCH --output="+cell+".log\n")
#			f.write(command)
#			f.close()
#			s("sbatch a.sh")
			print("nohup "+command +" > "+cell+".log &")
