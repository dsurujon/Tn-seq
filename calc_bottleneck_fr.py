## Defne Surujon
## Aug 2017

#input a dirrectory of raw fitness files, read all csv
#files in the directory and compute the new bottleneck
#value by first filtering positions by selecting all
#positions with >50 insertions at time 1 (count1)
#and then computing the ratio of sites where no reads
#were recovered at time 2 (count2==0)

import os
import glob
from optparse import OptionParser

options = OptionParser(usage='%prog input output',
                       description="Specify input directory and output file")

options.add_option("-i","--indir",dest="inputdir",
                   help="Input directory)")
options.add_option("-o","--outfile",dest="outputfile",
                   help="output file (.txt)")


def read_csv(filename):
    f=open(filename)
    lines=f.readlines()
    f.close()
    lines_parsed=[line.strip().split(',') for line in lines]
    header=lines_parsed[0]
    return(header,lines_parsed[1:])

def write_filtered_csv(header,data,outfilename):
    gx=open(outfilename,'w')
    headercsv=",".join(header)+"\n"
    gx.write(headercsv)
    for row in data:
        rowcsv=",".join(row)+"\n"
        gx.write(rowcsv)
    gx.close()

#read csv fitness file and filter out rows with count1<50
#return the new bottleneck value (proportion of sites
#remaining wiht count2==0)
#also write the filtered data set to file <filename>_FILTERED.csv
def compute_bn(filename):
    bn_fr=0
    header,data=read_csv(filename)
    count1_ix=header.index('count_1')
    count2_ix=header.index('count_2')
    data_filtered=[]
    zeros=0
    for row in data:
        if float(row[count1_ix])>50:
            data_filtered.append(row)
            if float(row[count2_ix])==0:
                zeros+=1
    old_len=len(data)
    new_len=len(data_filtered)
    num_pos_removed=old_len-new_len
    proportion_pos_removed=float(num_pos_removed)/old_len
    bn_fr=float(zeros)/new_len

    #write the filtered set to file
    newfilename=filename[:-4]+"_FILTERED.csv"
    write_filtered_csv(header,data_filtered,newfilename)
    
    return(old_len,new_len,proportion_pos_removed,bn_fr)


def main():
    opts, args = options.parse_args()
    indir = opts.inputdir
    outfile = opts.outputfile
    #only get csvfiles from the input directory
    inputfiles=glob.glob(indir+"/*.csv")

    g=open(outfile,'w')
    g.write('\t'.join(['File','Num_sites_original','Num_sites_new','Proportion_removed','BN_FR'])+'\n')
    for thisfile in inputfiles:
        l1,l2,p,bn=compute_bn(thisfile)
        thisline=[os.path.split(thisfile)[-1],str(l1),str(l2),str(p),str(bn)]
        g.write('\t'.join(thisline)+'\n')
        print(os.path.split(thisfile)[-1],"done")
	
    g.close()
if __name__ == '__main__':
    main()
		
