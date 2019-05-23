#!/usr/bin/python3

import subprocess

#process_radtags
#requirement is to demultiplex, or sort, the raw data to recover the individual

p = "/media/hugo/1TB/Luiz/fastq" # p: path to a directory of files.
P = "" # P,--paired: files contained within the directory are paired. (y or n)
I = "" # I,--interleaved: specify that the paired-end reads are interleaved in single files.
i = "fastq" # i: input file type, either 'fastq', 'gzfastq' (gzipped fastq), 'bam', or 'bustard' (default: guess, or gzfastq if unable to).
b = "/media/hugo/1TB/Luiz/barcodes/barcodes_radtags.txt" # b: path to a file containing barcodes for this run, omit to ignore any barcoding.
out_dir = "/media/hugo/1TB/Luiz/output_process_radtags" # o: path to output the processed files.
# f: path to the input file if processing single-end sequences.
# 1: first input file in a set of paired-end sequences.
# 2: second input file in a set of paired-end sequences.
c = " -c " # c,--clean: clean data, remove any read with an uncalled base.
q = " -q " # q,--quality: discard reads with low quality scores.
r = " -r " # r,--rescue: rescue barcodes and RAD-Tags.
t = "80" # t: truncate final read length to this value.
D = "" # D: capture discarded reads to a file.
E = "phred33"# E: specify how quality scores are encoded, 'phred33' (Illumina 1.8+/Sanger, default) or 'phred64' (Illumina 1.3-1.5).
w = "0.15" # w: set the size of the sliding window as a fraction of the read length, between 0 and 1 (default 0.15).
s = "10" # s: set the score limit. If the average score within the sliding window drops below this value, the read is discarded (default 10).
y = "fastq" # y: output type, either 'fastq', 'gzfastq', 'fasta', or 'gzfasta' (default: match input type).
enz1 = "apeKI" #provide the restriction enzyme used (cut site occurs on single-end read)
enz2 = "" #if a double digest was used, provide the second restriction enzyme used (cut site occurs on the paired-end read).

#verify enzyme digestion(s)
def defineenz(enz1,enz2):
    if enz2 != "":
        enzymes = " --renz-1 " + enz1 + " --renz-2 " + enz2
    else:
        if enz1 != "":
            enzymes = " -e " + enz1
        else:
            print ("Missing enzyme parameter")
            sys.exit()
    return enzymes

#verify if paired and interleaved
def paired_or_single(P,I):
    if P == "y":
        if I == "y":
            paired = " --paired --interleaved"
        else:
            paired = " --paired"
    else:
        paired = ""
    return paired


#run pipeline
process_radtags = subprocess.Popen("process_radtags -p " + p + " -b " + b + " -o " +
                                    out_dir + " " + defineenz(enz1,enz2) + paired_or_single(P,I) + " -t " + t +
                                    " -E " + E + " -w " + w + " --inline_null  -s " + s + " -y " + y +
                                    c + r + q + D, shell=True)
process_radtags.wait()
