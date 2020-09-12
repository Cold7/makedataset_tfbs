import argparse   # arguments parser
from Bio import SeqIO
import pandas as pd
import numpy as np
import multiprocessing as mp
import os


def doData(data):
	currentCHR, length = data
	

	##doing a list of TF for I have data, then I will add motifs just for these chipseq
	f = open(args.class_File,"r")
	tfList = []
	for line in f:
		tfList.append(line.split("\t")[0].upper())
	f.close()


	##class definition##
	f = open(args.class_definition,"r")
	dictSite = {}
	count = 0
	for line in f:
		aux = line[:-1].split("\t")
		if aux[1] == currentCHR:
			motifs = aux[4].split(",")
			motifs = [x.upper() for x in motifs] # motifs in uppper
			dictSite[count] = {"init":int(aux[2])-1,"end":int(aux[3])-1, "status":False, "motifs":[], "tfInSite":[], "id":aux[0]} #-1 assuming 1-base

			for motif in motifs:
				if motif in tfList:
					dictSite[count]["motifs"].append(motif)
			count += 1
	f.close()

	##chip overlapping class##
	auxVector = np.zeros(int(length/args.fragment)+1, dtype=np.int8)
	class_File = open(args.class_File,"r")
	for line in class_File:
		data = line[:-1].split("\t")
		name= data[0].upper()
		path = data[1]
		f = open(path, "r")
		for line in f:
			aux = line.split("\t")
			if aux[0] == currentCHR:
				class_init = int(aux[1])
				class_end = int(aux[2]) - 1
				if args.class_base == "1":
					class_init -= 1
				for i in range(len(dictSite)):
					if name in dictSite[i]["motifs"]:
						if class_end > dictSite[i]["init"] and class_init < dictSite[i]["end"]:
							dictSite[i]["status"] = True
							if name not in dictSite[i]["tfInSite"]:
								dictSite[i]["tfInSite"].append(name)
		f.close()
	class_File.close()

	##printing input data, chr, promoter  active, inactive, size of promoter,  TF used and not used
	print("current chr "+currentCHR)  
	active = 0
	inactive = 0
	for i in dictSite: #i is a number acting as a key
		if dictSite[i]["status"] == True:
			active += 1
		else:
			inactive += 1
		
####dictSite[count] = {"init":int(aux[2])-1,"end":int(aux[3])-1, "status":False, "motifs":[], "tfInSite":[], "id":aux[0]} 
	print("status of active sites in chr "+currentCHR)
	print("number of active promoters: "+str(active))
	print("number of inactive promoters: "+str(inactive))
	print("listing active sites")
	print("site\tlength+\tTFs bound")
	for i in dictSite: #i is a number acting as a key
		if dictSite[i]["status"] == True:
			print(dictSite[i]["id"]+"\t"+str(dictSite[i]["end"]- dictSite[i]["init"])+"\t"+str(dictSite[i]["tfInSite"])[1:-1])
	print("listing inactive sites")
	print("site\tlength")
	for i in dictSite: #i is a number acting as a key
		if dictSite[i]["status"] == False:
			 print(dictSite[i]["id"]+"\t"+str(dictSite[i]["end"]- dictSite[i]["init"]))
#	print("number of active promoters: "+str(active))
#	print("number of inactive promoters: "+str(inactive))
#	for site in dictSite:
		

	print("\n")

if __name__ == "__main__":
	global args, genomeFile

	#input
	parser = argparse.ArgumentParser()
	parser.add_argument("-g", "--genome", help="Path to genome file (in fasta format)", required = True)
	parser.add_argument("-f","--fragment", help="number of bases to fragment DNA sequence. Default: 50", type = int, default=50)
	parser.add_argument("-fm","--filling_mode", help="form as data is presented. Options are score to use the score in tsv file or percentage to use percentage of occupancy. Default: score", default="score",choices=["score","percentage"])

	####################################
	##
	## Class arguments
	##
	####################################
	parser.add_argument("-cf","--class_File", help="file with path to 5 columns chip-seq results for the current class.", required = True)
	parser.add_argument("-cd","--class_definition", help="tsv file with site definition (format is id, chr, init, end and  motifs).", required = True)
	parser.add_argument("-Cb","--class_base", help="to use 0-based or 1-based coord system. Default: 0", choices=["0","1"], default="1")

	args = parser.parse_args()

	chrs = []
	genomeFile = args.genome
	for record in SeqIO.parse(args.genome, "fasta"):
		dataset = pd.DataFrame()
		if "_" not in record.id and "chrM" not in record.id and "chrE" not in record.id:
			doData([record.id, len(record.seq)])
