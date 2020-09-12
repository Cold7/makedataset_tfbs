from glob import glob
from os import system as s
if __name__ == "__main__":
	fragments = ["5000","1000","500","250","200","150","100","50"]
	
	all = ["ChIP-seq/H3K27ac-human/H3K27ac.tsv","ChIP-seq/H4K20me1-human/H4K20me1.tsv","ChIP-seq/H3K36me3-human/H3K36me3.tsv","ChIP-seq/H3K79me2-human/H3K79me2.tsv","ChIP-seq/H3K9me3-human/H3K9me3.tsv","ChIP-seq/H3K27me3-human/H3K27me3.tsv","ChIP-seq/H3K4me3-human/H3K4me3.tsv","ChIP-seq/H3K4me1-human/H3K4me1.tsv","ChIP-seq/H3K4me2-human/H3K4me2.tsv","ChIP-seq/H3K9ac-human/H3K9ac.tsv"]
	noH4K20me1 = ["ChIP-seq/H3K27ac-human/H3K27ac.tsv","ChIP-seq/H3K36me3-human/H3K36me3.tsv","ChIP-seq/H3K79me2-human/H3K79me2.tsv","ChIP-seq/H3K9me3-human/H3K9me3.tsv","ChIP-seq/H3K27me3-human/H3K27me3.tsv","ChIP-seq/H3K4me3-human/H3K4me3.tsv","ChIP-seq/H3K4me1-human/H3K4me1.tsv","ChIP-seq/H3K4me2-human/H3K4me2.tsv","ChIP-seq/H3K9ac-human/H3K9ac.tsv"]
	noH3K79me2 = ["ChIP-seq/H3K27ac-human/H3K27ac.tsv","ChIP-seq/H4K20me1-human/H4K20me1.tsv","ChIP-seq/H3K36me3-human/H3K36me3.tsv","ChIP-seq/H3K9me3-human/H3K9me3.tsv","ChIP-seq/H3K27me3-human/H3K27me3.tsv","ChIP-seq/H3K4me3-human/H3K4me3.tsv","ChIP-seq/H3K4me1-human/H3K4me1.tsv","ChIP-seq/H3K4me2-human/H3K4me2.tsv","ChIP-seq/H3K9ac-human/H3K9ac.tsv"]
	noH3K36me3 = ["ChIP-seq/H3K27ac-human/H3K27ac.tsv","ChIP-seq/H4K20me1-human/H4K20me1.tsv","ChIP-seq/H3K79me2-human/H3K79me2.tsv","ChIP-seq/H3K9me3-human/H3K9me3.tsv","ChIP-seq/H3K27me3-human/H3K27me3.tsv","ChIP-seq/H3K4me3-human/H3K4me3.tsv","ChIP-seq/H3K4me1-human/H3K4me1.tsv","ChIP-seq/H3K4me2-human/H3K4me2.tsv","ChIP-seq/H3K9ac-human/H3K9ac.tsv"]


	folders = glob("../00_epigenomas/encode_reference_epigenome/*/")
	folders.remove("../00_epigenomas/encode_reference_epigenome/pythonScripts/")

	for fragment in fragments:
		for folder in folders:
			cell = folder.split("/")[-2]
			command = "python3.6 ../01_make_central_vectors/makeCentralVector.py "
			command += "-g ../00_epigenomas/encode_reference_epigenome/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta "
			command += "-f "+fragment+" "
			command += "-n 23 "
			command += "-C CTCF "
			command += "-cd /data_1/scontreras/predictores/00_epigenomas/geneFeature_withFimo/ctcf_regulatory_build.tsv "
			command += "-o ../02_central_vectors/CTCF/"+cell+"/"+fragment+" "
			command += "-ds -dsf "+folder+"DNase-seq/DNase-seq.tsv "
			command += "-dm -dmf "+folder+"whole-genome\\ shotgun\\ bisulfite\\ sequencing/meth.tsv "
			command += "-dc "
			command += "-pol -pFile "+folder+"ChIP-seq/POLR2A-human/POLR2A.tsv "
			command += "-r -rf "+folder+"RNA-seq/rnaseq.tsv "
			command += "-gen -gg ../00_epigenomas/encode_reference_epigenome/ENCFF824ZKD.gtf "
			if cell == "H1":
				command += "-cf paths_ctcf/path_h1 -hm -hmf "
				for hm in all:
					command += folder+hm+" "
			elif cell == "GM12878":
				command += "-cf paths_ctcf/path_gm12878 -hm -hmf "
				for hm in all:
					command += folder+hm+" "
			elif cell == "K562":
				command += "-cf paths_ctcf/path_k562 -hm -hmf "
				for hm in noH4K20me1:
					command += folder+hm+" "
			elif cell == "HeLa-S3":
				command += "-cf paths_ctcf/path_hela -hm -hmf "
				for hm in noH3K36me3:
					command += folder+hm+" "
			elif cell == "HepG2":
				command += "-cf paths_ctcf/path_hepg2 -hm -hmf "
				for hm in noH3K79me2:
					command += folder+hm+" "			
			s(command)