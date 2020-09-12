from os import system as s
from glob import glob
import multiprocessing as mp

def doAll(folder):
	files = glob(folder+"/*.tsv")
	command = "cat "
	for f in files:
		command+=f+"\t"
	command = command[:-1]+" > "+folder+"/all_no_sorted.tsv"
	s(command)

	command = "sort -ur --temporary-directory=./temp "+folder+"/all_no_sorted.tsv > "+folder+"/all_sorted.tsv"
	s(command)
	

if __name__ == "__main__":
	files =glob("promoter/*/*")#+glob("TFBS_unk/*/*")+glob("TFBS_unk_noOrientation/*/*")

	pool = mp.Pool(processes=11)
	pool.map(doAll, files, chunksize = 1)
