from glob import glob
import multiprocessing as mp
from os import system as s

def doAll(data):
	currentCombination, size, noUsingCell = data
	names = {}  #for cell line to save filename to make combinations
	cellsToWorkWith = []
	for cell in combinations[currentCombination]:
		if cell != noUsingCell:
			cellsToWorkWith.append(cell)
	
	for cell in cellsToWorkWith:
		currentNoHistone = []
		f = open(mainFolder+"/"+cell+"/"+size+"/all_sorted.tsv","r")
		header = f.readline()[:-1].split("\t")
		f.close()
		positionOfMark = []
		marks = currentCombination.split("_")
		for mark in marks:
			cont = 0
			for h in header:
				if mark+".tsv_" in h:
					positionOfMark.append(cont)
				cont += 1
		f = open(mainFolder+"/"+cell+"/"+size+"/all_sorted.tsv","r")
		for line in f:
			line = line[:-1].split("\t")
			toPrint = ""
			for i in range(len(line)):
				if i not in positionOfMark:
					toPrint+=line[i]+"\t"
			toPrint = toPrint[:-1] #for the last \t

			s("echo "+toPrint+" >> "+mainFolder+"/"+cell+"/"+size+"/no_"+currentCombination+"_noCell_"+noUsingCell+"_noSortedForK562val.tsv")
		f.close()
		name = mainFolder+"/"+cell+"/"+size+"/no_"+currentCombination+"_noCell_"+noUsingCell+"_noSortedForK562val.tsv"
		s("sort -ur --temporary-directory=./temp "+name+" > "+mainFolder+"/"+cell+"/"+size+"/no_"+currentCombination+"_sorted.tsv")
#		s("rm -rf "+mainFolder+"/"+cell+"/"+size+"/no_"+currentCombination+"_noSorted.tsv")
#		names[cell] = mainFolder+"/"+cell+"/"+size+"/no_"+currentCombination+"_sorted.tsv"

#	for cell in names:
#		command = "cat "
#		used = []
#		for cell2 in names:
#			if cell2 != cell:
#				command += names[cell2]+" "
#				used.append(cell2)
#		
#		command += "> "+mainFolder+"/allWithNo_"+currentCombination+"_for_"+str(used)[1:-1].replace(" ","").replace("'","").replace(",","_")+"_size_"+size+"_noSort.tsv"
#		s(command)
#		s("sort -ur --temporary-directory=./temp "+mainFolder+"/allWithNo_"+currentCombination+"_for_"+str(used)[1:-1].replace(" ","").replace("'","").replace(",","_")+"_size_"+size+"_noSort.tsv > "+mainFolder+"/allWithNo_"+currentCombination+"_for_"+str(used)[1:-1].replace(" ","").replace("'","").replace(",","_")+"_size_"+size+"_sorted.tsv")
##		print(cell,used, command)
#		s("rm -rf "+mainFolder+"/allWithNo_"+currentCombination+"_for_"+str(used)[1:-1].replace(" ","").replace("'","").replace(",","_")+"_size_"+size+"_noSort.tsv")


if __name__ == "__main__":

	global mainFolder
	global combinations

	#############################
	##
	## manual variables
	##
	############################
	mainFolder = "promoter"
	nproc = 9



	##########################
	##
	## script start here
	##
	#########################

	#all possible combinations
	combinations = {}
#	combinations["H4K20me1"] = ["GM12878","H1","K562"]
#	combinations["H3K79me2"] = ["GM12878","H1","HepG2"]
#	combinations["H3K36me3"] = ["GM12878","H1","HeLa-S3"]
	combinations["H4K20me1_H3K79me2_H3K36me3"] = ["GM12878","H1","HeLa-S3","HepG2"]
	
	sizes = ["200","100"]
	sizes = ["100"]

	arguments = []
	for comb in combinations:
		for cell in combinations[comb]:
			for size in sizes:
				arguments.append([comb,size, cell])

	pool = mp.Pool(processes = nproc)
	pool.map(doAll, arguments, chunksize = 1)
	

