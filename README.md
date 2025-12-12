# Visualizing Nuclease Cutting Patterns Around TF Binding Sites

This repository contains a small analysis workflow for visualizing nuclease-derived DNA fragment patterns around transcription factor (TF) binding sites using a V-plot. 
The goal is to observe how fragment lengths vary with distance from the protein–DNA binding region, revealing the characteristic "V" pattern associated with DNA protection footprints.

## Introduction

Nuclease-based assays (like ATAC-seq, DNase-seq, MNase footprinting) provide insights into chromatin accessibility by cutting open or unprotected regions of DNA. 
When a transcription factor binds to DNA, the protein physically shields a small region of the genome from nuclease cleavage.
As a result, fragments close to the protein-bound region tend to be shorter, because cuts cannot occur inside the footprint.
And fragments farther away tend to be longer, because nucleases can cut at both ends beyond the protein boundary.
By plotting fragment length against distance from the TF binding center, we observe a characteristic V-shaped pattern, widely used in footprinting studies.
This repository shows how to compute such a plot from basic BED-like mapped data.

## Dataset Description
| File | Description |
|------|-------------|
| mapped_sample.bed | A small sample of the original raw BED data (large raw dataset excluded due to GitHub size limits) |
| XYZ_matrix.tsv | The processed table containing final computed values for each fragment |
| plot.py | Python script to generate a V-plot from the matrix |
| vplot.png | Output figure produced by the script |


The dataset (mapped_sample.bed) used in this assignment contains two types of genomic information.
Below are the first few lines of mapped_sample.bed:
```
2       chr1    90919   91937   chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA   16.2951   +   chr1    90838   91006   IH02_00.pairs@15152   168   +
2       chr1    90919   91937   chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA   16.2951   +   chr1    90846   90998   IH02_04.pairs@4163    152   +
2       chr1    90919   91937   chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA   16.2951   +   chr1    90851   91000   IH02_04.pairs@4164    149   +
2       chr1    90919   91937   chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA   16.2951   +   chr1    90850   91014   IH02_00.pairs@15153   164   +
2       chr1    90919   91937   chr1:91382-91550|carroll_ctcf_mcf7_v45m`2_GTGGCACCAGGTGGCAGCA   16.2951   +   chr1    90900   90965   IH02_00.pairs@15164   65    +
```

The first part describes where a DNA-binding protein (such as CTCF) is located on the genome. 
These regions come from a ChIP-seq–type experiment, so Columns 3 and 4 show the start and end of each protein binding site on genome. 
The second part of the dataset lists DNA fragments that were cut by a nuclease enzyme. 
These fragments appear in Columns 9 and 10, which give the genomic start and end of each piece of DNA produced after digestion.

## Workflow Summary
 The analysis consists of two main steps:
 1] Processed the raw mapped BED file :-
 Calculated TF binding center, fragment center and fragment length. calculated the distance between TF binding center and fragment center. 
 Paired the distance with fragment length. Sorted the pair and also counted the occurences of each pair, then stored in file XYZ_matrix.tsv

 ```
Input:
  awk '{C1= ($3+$4)/2; C2=($9+$10)/2; X= C2-C1; Y=$10-$9; print(X, Y) }' mapped.bed | sort -k1,1n -k2,2n| uniq -c | awk '{print $2, $3, $1}' | tr ' ' '\t'> XYZ_matrix.tsv
```

```
Output:

 XYZ_matrix.tsv
-509    44      7
-509    46      10
-509    48      7
-509    50      21
-509    52      17
```

Column 1 > Distance between fragment center and TF binding center

Column 2 > Fragment length

Column 3 > Occurances for Column_1 - Column_2 pair

2] Generated a V-plot using matplotlib (code provided in plot.py)

 Command > python plot.py
 
 Output figure > vplot.png
  
  The generated V-plot displays:
  
  X-axis: Distance from TF binding center
  
  Y-axis: Fragment length
  
  Color: Frequency of fragments (higher = stronger signal)
  

## Interpretation of the V-plot

  The file `vplot.png` included in this repository is an example of the V-shaped pattern generated from the processed matrix. 
  This shape reflects the biological principle that DNA near a bound protein is protected and therefore produces shorter fragments,
  while DNA farther away is more accessible and produces longer fragments. 
  This dataset therefore allows us to visualize the local DNA-protection footprint created by protein binding.

