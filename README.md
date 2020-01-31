# Tn-seq
 Tn-seq data processing scripts
 
 --------------------
 ## Bottleneck calculation
 
```calc_bottleneck_fr.py``` takes an input directory, containing fitness files, and for each file, computes a bottleneck value. The bottleneck is defined as the proportion of TA insertion sites that had positive counts at time 1, but 0 counts at time 2. For robustness, only positions with >50 counts at time 1 are considered.     
This script will generate a tab separated table which contains the bottleneck value for each input file.     
Example usage:     
```python calc_bottleneck_fr.py -i [inputdirectory] -o [outputfile]```    
Where ```[inputdirectory]``` is a directory containing Fitness files, and ```[outputfile]``` is the name of a tab separated file to be generated. This file will have the bottleneck value corresponding to each of the files in the ```[inputdirectory]```.     

## Single experiment data processing
```process_single_expt.R``` is a function that takes in an aggregate file, and performs a 2-sample t-test with B-H correction on each gene. The observed fitness of each gene is compared to an expected fitness for the experiment (which is the median fitness across all genes). In the output, dW (difference in fitness) is real-expected fitness. This script will produce a ```[name]_discovery.csv``` table that contains the dW and associated statistical comparison, as well as a volcano plot.      
Example usage:     
```process_single_expt(inputfilename, essentialsfile, N, outputdirectory)```    
```inputfilename``` is the input aggregate file    
```essentialsfile``` is a csv file that contains gene essentiality data for the strain that is being processed. In the TvO lab, we use the ```Essentials.csv``` file, which contains gene essentiality data for 2 *Streptococcus pneumoniae* strains     
```N``` is a threshold for the number of insertions in a given gene. Genes with fewer than ```N``` insertions (after bottleneck correction) will be filtered out and excluded from the analysis. Higher ```N``` would be more conservative. For *in vitro* experiments, ```N=3``` can be suitable, but experiments with high variability might require ```N=6``` or higher.     
```outputdirectory``` is the name of the output directory where output tables and figures will be saved. If the directory doesn't already exist, it will be created. 

## Comparison of two experiments 
```compare_two_expts.R``` takes in two aggregate files, and performs a 2-sample t-test with B-H correction on each gene. In the output, dW (difference in fitness) is the difference in fitness between experiment 1 and 2 (fitness1-fitness2). This script will produce a ```[name1]_[name2]_discovery.csv``` table that contains the dW and associated statistical comparison, a volcano plot, and a scatter plot showing fitness values for each gene in both experiments.     
Example usage:     
```compare_two_expts(inputfilename1, inputfilename2, essentialsfile, N, outputdirectory)```    
```inputfilename1``` is the input aggregate file for experiment 1     
```inputfilename2``` is the input aggregate file for experiment 2     
```essentialsfile``` is a csv file that contains gene essentiality data for the strain that is being processed. In the TvO lab, we use the ```Essentials.csv``` file, which contains gene essentiality data for 2 *Streptococcus pneumoniae* strains     
```N``` is a threshold for the number of insertions in a given gene. Genes with fewer than ```N``` insertions (after bottleneck correction) will be filtered out and excluded from the analysis.     
```outputdirectory``` is the name of the output directory where output tables and figures will be saved. If the directory doesn't already exist, it will be created.    
