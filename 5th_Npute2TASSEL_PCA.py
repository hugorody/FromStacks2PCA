#!/usr/bin/python
#This script is the part 5th of "From Stacks to PCA" pipeline

import sys
import os

path1 = sys.argv[1]
file1 = sys.argv[2] # NPUTE imputation output
file2 = sys.argv[3] # _isolate_order.csv [order of individuals space delimited generated by 4th_Concater2Npute.py]
outputname = sys.argv[4]

os.chdir( path1 )

output1 = open(outputname,"w")
output2 = open(outputname+".imputationfailed.txt","w")

#write first line
with open(file2,"r") as set2:
    for i in set2:
        i = i.rstrip()
        i = i.replace(" ","\t")
        output1.write("rs#\talleles\tchrom\tpos\tstrand\tassembly#\tcenter\tprotLSID\tassayLSID\tpanel\tQCcode\t"+i+"\n");

with open(file1,'r') as set1:
    count = 0
    seqs = {}
    for i in set1:
        i = i.rstrip()
        i = i.split(",")
        count += 1

        if "" not in i:
            output1.write("NA\tNA\t1\t"+str(count)+"\t+\tseq\tNA\tNA\tNA\tNA\tNA\t"+"\t".join(i)+"\n");

        if "" in i: #if imputation has failed
            output2.write(str(count)+"\n");
output1.close()
output2.close()
