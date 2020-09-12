from glob import glob
from os import system as s



if __name__ == "__main__":

#head ../02_central_vectors/promoter_flanking_region_core/K562/100/centralVector_chr1.tsv 
#DNAse-seq	methylation	CG	CTCF	POLR2A	rnaseq	TSS	Gene	H3K27ac.tsv	H3K36me3.tsv	H3K79me2.tsv	H3K9me3.tsv	H3K27me3.tsv	H3K4me3.tsv	H3K4me1.tsv	H3K4me2.tsv	H3K9ac.tsv	promoter_flanking_region


	finalSize1 = 200000
	finalSize2 = 20000
	job = 0
	folders = glob("../02*/promoter_core/*/*/")
	for folder in folders:
		aux = folder.split("/")
		cell = aux[-3]
		size = int(aux[-2])
		Class = "promoter"
		
		command = "python3.4 00_doFullVectors.py -f "+folder+" -n 8 -O yes -C "+Class+" "
		if size != 150:
			if size < 1000:
				sizeToUse = str(int(finalSize2 / size))
				command += "-lv "+sizeToUse+" -rv "+sizeToUse
			else:
				sizeToUse = str(int(finalSize1 / size))
				command += "-lv "+sizeToUse+" -rv "+sizeToUse
			
			command += " -o ./"+Class+"/"+cell+"/"+str(size)+"/ "
			command += " -fl "
			cont = 0
			file0 = open(glob(folder+"/*.tsv")[0],"r")
			dataToUse = ""
			for line in file0:
				if cont == 0:
					dataToUse = line[:-1].split("\t")
					cont = 1
			file0.close()
			for use in dataToUse:
				if use != Class:
					command += use+" "
			f = open("job.sh","w")
			f.write("#!/bin/bash\n")
			f.write("#SBATCH -c 8\n")
			f.write("#SBATCH -e "+str(cont)+".err")
			f.write("#SBATCH --job-nam=job"+str(job)+"\n")
			f.write(command)
			f.close()
			s("sbatch job.sh")
			job += 1
