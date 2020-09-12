from glob import glob

if __name__ =="__main__":
	files = glob("head*")
	for file in files:
		currentSize = file.split("_")[-1]
		f = open(file,"r")
		for l in f:
			l = l[:-1].split("\t")
			#no h4k20m1
			f2 = open("head_no_h4k20me1_"+currentSize,"w")
			noh4k20me1 = ""
			for data in l:
				if "H4K20me1.tsv_"not in data:
					noh4k20me1 += data+"\t"
			noh4k20me1 = noh4k20me1[:-1] 
			f2.write(noh4k20me1)
			f2.close()

			#noh3k79me2
			f3 = open("head_no_h3k79me2_"+currentSize,"w")
			noh3k79me2 = ""
			for data in l:
				if "H3K79me2.tsv_"not in data:
					noh3k79me2 += data+"\t"
			noh3k79me2 = noh3k79me2[:-1]
			f3.write(noh3k79me2)
			f3.close()

			#noh3k36me3
			f4 = open("head_no_h3k36me3_"+currentSize,"w")
			noh3k36me3 = ""
			for data in l:
				if "H3K36me3.tsv_"not in data:
					noh3k36me3 += data+"\t"
			noh3k36me3 = noh3k36me3[:-1]
			f4.write(noh3k36me3)
			f4.close()
			
			#notTheThree
			f5 = open("head_no_three_"+currentSize,"w")
			noThree = ""
			for data in l:
				if "H3K36me3.tsv_" not in data:
					if "H3K79me2.tsv_" not in data:
						if "H4K20me1.tsv_" not in data:
							noThree += data+"\t"
			noThree = noThree[:-1]
			f5.write(noThree)
			f5.close()

		f.close()				
