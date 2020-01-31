# Tn-seq
 Tn-seq data processing scripts
 
 --------------------
 ## Bottleneck calculation
 
```calc_bottleneck_fr.py``` takes an input directory, containing fitness files, and for each file, computes a bottleneck value. The bottleneck is defined as the proportion of TA insertion sites that had positive counts at time 1, but 0 counts at time 2. For robustness, only positions with >50 counts at time 1 are considered.     
This script will generate a tab separated table which contains the bottleneck value for each input file.     

## Single experiment data processing
```process_single_expt.R``` is a function that takes in an aggregate file, and performs a 2-sample t-test with B-H correction on each gene. The observed fitness of each gene is compared to an expected fitness for the experiment (which is the median fitness across all genes). In the output, dW (difference in fitness) is real-expected fitness. This script will produce a ```[name]_discovery.csv``` table that contains the dW and associated statistical comparison, as well as a volcano plot. 

## Comparison of two experiments 
```compare_two_expts.R``` takes in two aggregate files, and performs a 2-sample t-test with B-H correction on each gene. In the output, dW (difference in fitness) is the difference in fitness between experiment 1 and 2 (fitness1-fitness2). This script will produce a ```[name1]_[name2]_discovery.csv``` table that contains the dW and associated statistical comparison, a volcano plot, and a scatter plot showing fitness values for each gene in both experiments. 
