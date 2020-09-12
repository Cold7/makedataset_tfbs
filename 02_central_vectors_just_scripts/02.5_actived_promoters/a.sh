#!/bin/bash
#SBATCH --job-name=K562
#SBATCH --output=K562.log
python3.6 ../01_make_central_vectors/active_promoters.py -g ../00_epigenomas/encode_reference_epigenome/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta -f 100 -Cb 1 -cd  ../00_epigenomas/genome_features/hocomoco_core/final_promoter -cf path_tfs/K562


#K562

