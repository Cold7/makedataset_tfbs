from glob import glob
import pandas as pd


if __name__ == "__main__":
	sizes = ["5000","1000","500","250","200","100","50"]

	for size in sizes:
		print("###############", size,"###############")
		#no h4k20me1 ==> K562,GM and H1
		print("no h4k20me1")
		cells = ["K562","GM12878","H1"]
		colsToUse = None
		f = open("head_no_h4k20me1_"+size,"r")
		for l in f:
			if l[-1] == "\n":
				colsToUse = l[:-1].split("\t")
			else:
				colsToUse = l.split("\t")
		f.close()
		for cell in cells:
			print("\t"+cell)
			df = pd.read_csv(cell+"/"+size+"/all_sorted.tsv", sep="\t")
			df = df[colsToUse]
			df.to_csv(cell+"/"+size+"/no_h4k20me1.tsv", index=False, sep="\t")

		#no h3k79me2 ==> HepG2,GM and H1
		print("no h3k79me2")
		cells = ["HepG2","GM12878","H1"]
		colsToUse = None
		f = open("head_no_h3k79me2_"+size,"r")
		for l in f:
			if l[-1] == "\n":
				colsToUse = l[:-1].split("\t")
			else:
				colsToUse = l.split("\t")
		f.close()
		for cell in cells:
			print("\t"+cell)
			df = pd.read_csv(cell+"/"+size+"/all_sorted.tsv", sep="\t")
			df = df[colsToUse]
			df.to_csv(cell+"/"+size+"/no_h3k79me2.tsv", index=False, sep="\t")

		#no h3k36me3 ==> HeLa-S3,GM and H1
		print("no h3k36me3")
		cells = ["HeLa-S3","GM12878","H1"]
		colsToUse = None
		f = open("head_no_h3k36me3_"+size,"r")
		for l in f:
			if l[-1] == "\n":
				colsToUse = l[:-1].split("\t")
			else:
				colsToUse = l.split("\t")
		f.close()
		for cell in cells:
			print("\t"+cell)
			df = pd.read_csv(cell+"/"+size+"/all_sorted.tsv", sep="\t")
			df = df[colsToUse]
			df.to_csv(cell+"/"+size+"/no_h3k36me3.tsv", index=False, sep="\t")

		#no threeHM ==> K562,HepG2, HeLa-S3,GM and H1
		print("no three HMs")
		cells = ["K562","HepG2","HeLa-S3","GM12878","H1"]
		colsToUse = None
		f = open("head_no_three_"+size,"r")
		for l in f:
			if l[-1] == "\n":
				colsToUse = l[:-1].split("\t")
			else:
				colsToUse = l.split("\t")
		f.close()
		for cell in cells:
			df = pd.read_csv(cell+"/"+size+"/all_sorted.tsv", sep="\t")
			df = df[colsToUse]
			df.to_csv(cell+"/"+size+"/noh4k20me1_noh3k79me2_noh3k36me3.tsv", index=False, sep="\t")
