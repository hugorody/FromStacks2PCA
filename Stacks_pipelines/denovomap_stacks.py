#!/usr/bin/python3

import subprocess

#denovo_map
T = "2" #the number of threads/CPUs to use (default: 1).
samples = "/media/hugo/1TB/Luiz/output_process_radtags" #path to the directory containing the samples (FASTq) reads files.
pop_map = "/media/hugo/1TB/Luiz/population_map.txt" #path to a population map file (format is "<name> TAB <pop>", one sample per line).
out_dir = "/media/hugo/1TB/Luiz/output_denovomap" #path to an output directory.
M = "5" #number of mismatches allowed between stacks within individuals (for ustacks).
n = "2" #number of mismatches allowed between stacks between individuals (for cstacks).

#run pipeline
denovo_map = subprocess.Popen("denovo_map.pl --samples " + samples + " -T " + T +
                                " --popmap " + pop_map + " -o " + out_dir +
                                " -M " + M + " -n " + n, shell=True)
denovo_map.wait()
