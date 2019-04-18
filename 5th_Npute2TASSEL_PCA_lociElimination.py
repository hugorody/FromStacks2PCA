#!/usr/bin/python
#This script is the part 5th of "From Stacks to PCA" pipeline

import sys
import os

path1 = sys.argv[1]
file1 = sys.argv[2] # NPUTE imputation output
file2 = sys.argv[3] # _isolate_order.csv [order of individuals space delimited generated by Concater2Npute.py]
outputname = sys.argv[4]
window = int(sys.argv[5]) #loci window size (80bp)

os.chdir( path1 )

output1 = open(outputname+"_eliminatedLOCI_PCAinput.csv","w")
output2 = open(outputname+".imputationfailed.txt","w")

#write first line
with open(file2,"r") as set2:
    for i in set2:
        i = i.rstrip()
        i = i.replace(" ",",")
        output1.write("rs#,alleles,chrom,pos,strand,assembly#,center,protLSID,assayLSID,panel,QCcode,"+i+"\n");

with open(file1,"r") as set1:
    nlines = 0
    filelist = []
    for i in set1:
        i = i.rstrip()
        filelist.append(i)
        nlines += 1

    nloci = nlines // window

count = 0
loci = {}
delloci = {}
for i in range(0,nlines,window):

    start = i+1
    end = i+window

    if any(",,," in s for s in filelist[start-1:end]):
        delloci[str(start-1)+"-"+str(end)] = filelist[start-1:end]
        output2.write("Loci "+str(start-1)+"-"+str(end)+"\n"+"\n".join(filelist[start-1:end])+"\n");
    else: #if imputation has not failed in loci
        loci[str(start-1)+"-"+str(end)] = filelist[start-1:end]
        for j in filelist[start-1:end]:
            j = j.split(",")
            count += 1
            output1.write("NA,NA,"+str(start)+"-"+str(end)+","+str(count)+",+,seq,NA,NA,NA,NA,NA,"+",".join(j)+"\n");

output1.close()
output2.close()
