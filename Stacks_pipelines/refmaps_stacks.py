#!/usr/bin/python3

import subprocess

#denovo_map
T = "2" #the number of threads/CPUs to use (default: 1).
samples = "/media/hugo/1TB/Luiz/output_process_radtags" #path to the directory containing the samples (FASTq) reads files.
pop_map = "/media/hugo/1TB/Luiz/population_map.txt" #path to a population map file (format is "<name> TAB <pop>", one sample per line).
out_dir = "/media/hugo/1TB/Luiz/output_denovomap" #path to an output directory.
var_alpha = "0.05" #significance level at which to call variant sites (for gstacks; default: 0.05).
gt_alpha = "0.05" #significance level at which to call genotypes (for gstacks; default: 0.05).

#run pipeline
ref_map = subprocess.Popen("ref_map.pl --samples " + samples + " -T " + T +
                                " --popmap " + pop_map + " -o " + out_dir +
                                " --var-alpha " + var_alpha + " --gt-alpha " + gt_alpha, shell=True)
ref_map.wait()
