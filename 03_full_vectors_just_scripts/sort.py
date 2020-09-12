from glob import glob
from os import system as s

if __name__ == "__main__":
	files = glob("*.tsv")
	for file in files:
		print(file)
		s("sort --temporary-directory=./temporal -ur "+file+" >sort_"+file)
