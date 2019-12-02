from glob import glob
from os import system as s
import os
"""
script basado en datos obtenidos de 
https://www.encodeproject.org/matrix/?type=Experiment&status=released&assay_slims=DNA+accessibility&assay_slims=DNA+methylation&assay_slims=DNA+binding&assay_slims=Transcription&assay_title=TF+ChIP-seq&assay_title=Histone+ChIP-seq&assay_title=DNase-seq&assay_title=polyA+plus+RNA-seq&assay_title=WGBS&award.project=ENCODE&assembly=GRCh38&replicates.library.biosample.treatments.treatment_term_name%21=ethanol&replicates.library.biosample.treatments.treatment_term_name%21=dexamethasone&replicates.library.biosample.treatments.treatment_term_name%21=doxycycline+hyclate&replicates.library.biosample.treatments.treatment_term_name%21=Activin+A&replicates.library.biosample.treatments.treatment_term_name%21=Bone+morphogenetic+protein+4&replicates.library.biosample.treatments.treatment_term_name%21=Fibroblast+growth+factor+2&replicates.library.biosample.treatments.treatment_term_name%21=interferon+alpha&replicates.library.biosample.treatments.treatment_term_name%21=dimethyl+sulfoxide&replicates.library.biosample.treatments.treatment_term_name%21=Interferon+gamma&replicates.library.biosample.treatments.treatment_term_name%21=afimoxifene&replicates.library.biosample.treatments.treatment_term_name%21=all-trans-retinoic+acid&replicates.library.biosample.treatments.treatment_term_name%21=erythropoietin&replicates.library.biosample.treatments.treatment_term_name%21=hydrocortisone+succinate&replicates.library.biosample.treatments.treatment_term_name%21=interleukin-3&replicates.library.biosample.treatments.treatment_term_name%21=kit+ligand&replicates.library.biosample.treatments.treatment_term_name%21=17%CE%B2-estradiol&replicates.library.biosample.treatments.treatment_term_name%21=estradiol&replicates.library.biosample.treatments.treatment_term_name%21=bisphenol+A&replicates.library.biosample.treatments.treatment_term_name%21=genistein&replicates.library.biosample.treatments.treatment_term_name%21=17%CE%B2-hydroxy-5%CE%B1-androstan-3-one&replicates.library.biosample.treatments.treatment_term_name%21=tamoxifen&replicates.library.biosample.treatments.treatment_term_name%21=17%CE%B2-hydroxy-17-methylestra-4%2C9%2C11-trien-3-one&replicates.library.biosample.treatments.treatment_term_name%21=Sendai+virus&replicates.library.biosample.treatments.treatment_term_name%21=UT189&replicates.library.biosample.treatments.treatment_term_name%21=cisplatin&replicates.library.biosample.treatments.treatment_term_name%21=doxycycline&replicates.library.biosample.treatments.treatment_term_name%21=lactate&replicates.library.biosample.treatments.treatment_term_name%21=retinoic+acid&replicates.library.biosample.treatments.treatment_term_name%21=sodium+butyrate&replicates.library.biosample.treatments.treatment_term_name%21=vorinostat&replication_type=isogenic&audit.ERROR.category%21=extremely+low+read+depth&audit.ERROR.category%21=missing+control+alignments&audit.ERROR.category%21=control+extremely+low+read+depth&audit.ERROR.category%21=extremely+low+spot+score&audit.ERROR.category%21=extremely+low+read+length&audit.ERROR.category%21=inconsistent+genetic+modification+reagent+source+and+identifier&audit.ERROR.category%21=inconsistent+genetic+modification+tags&audit.ERROR.category%21=inconsistent+read+count&audit.NOT_COMPLIANT.category%21=insufficient+read+depth&audit.NOT_COMPLIANT.category%21=control+insufficient+read+depth&audit.NOT_COMPLIANT.category%21=severe+bottlenecking&audit.NOT_COMPLIANT.category%21=poor+library+complexity&audit.NOT_COMPLIANT.category%21=partially+characterized+antibody&audit.NOT_COMPLIANT.category%21=insufficient+read+length&audit.NOT_COMPLIANT.category%21=insufficient+replicate+concordance&audit.NOT_COMPLIANT.category%21=missing+spikeins&audit.NOT_COMPLIANT.category%21=missing+possible_controls&audit.NOT_COMPLIANT.category%21=insufficient+coverage
"""
def download(data):
#	print(data)
	folder = data[6]+"/"+data[4]+"/"+data[18]
	try:
		os.makedirs(folder)
	except:
		pass
	toDown = data[42]
	nameDown = data[42].split("/")[-1]
	s("wget "+toDown+" -P "+folder)
	s("gunzip "+folder+"/"+nameDown)
	
	
if __name__ == "__main__":
	files = glob("*.tsv")
	for file in files:

		f = open(file,"r")
		for line in f:
			if "File accession" not in line:
				line = line.split("\t")
				if line[4] == "ChIP-seq" and line[43] == "GRCh38" and line[2] == "optimal IDR thresholded peaks" and line[47] == "released" and line[1] == "bed narrowPeak":
					download(line)
				elif line[4] == "whole-genome shotgun bisulfite sequencing" and line[43] == "GRCh38" and line[1] == "bed bedMethyl" and line[2] == "methylation state at CpG" and line[47] == "released" :
					download(line)
				elif line[4] == "RNA-seq" and line[43] == "GRCh38" and line[1] == "tsv" and line[2] == "gene quantifications" and line[47] == "released":
					download(line)
				elif line[4] == "DNase-seq" and line[43] == "GRCh38" and line[2] == "peaks" and line[1] == "bed narrowPeak" and line[47] == "released":
					download(line)
				else:
					pass
				
		f.close()
		
	
