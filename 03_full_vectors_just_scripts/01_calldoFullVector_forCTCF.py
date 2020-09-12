from glob import glob
from os import system as s



if __name__ == "__main__":
	finalSize1 = 200000
	finalSize2 = 20000
	folders = glob("../02*/CTCF/*/*/")
	for folder in folders:
		aux = folder.split("/")
		cell = aux[-3]
		size = int(aux[-2])
		Class = "CTCF"
		command = "python3.6 00_doFullVectors.py -f "+folder+" -n 4 -C "+Class+" "
		if size != 150:
			if size < 1000:
				sizeToUse = str(int(finalSize2 / size))
				command += "-lv "+sizeToUse+" -rv "+sizeToUse
			else:
				sizeToUse = str(int(finalSize1 / size))
				command += "-lv "+sizeToUse+" -rv "+sizeToUse
			
			command += " -o ./"+cell+"/"+str(size)+"/ "
			command += " -fl "
					
			file0 = open(glob(folder+"/*.tsv")[0],"r")
			cont = 0
			dataToUse = ""
			for line in file0:
				if cont == 0:
					dataToUse = line[:-1].split("\t")
					cont = 1
			for use in dataToUse:
				if use != Class:
					command += use+" "

			s(command)
