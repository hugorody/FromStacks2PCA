#!/usr/bin/python3

#This script is part of FSTP pipeline
#Using the population map file used as input for Stacks pipelines
#to create the "population file" contaning both personal and Stacks
#annotation to run the FSTP pipeline.

import sys

population_map = sys.argv[1] #population map file used for Stacks pipelines

print ("Press Enter to repeat Sample name for Name")

samples = {}
count = 0
with open(population_map,"r") as set1:
	for i in set1:
		i = i.rstrip().split("\t")
		sample = i[0]
		pop = i[1]
		print ("Sample: ",sample,"Population: ",pop)
		name = input("Name: ")
		if name == "":
			name = sample
		count += 1
		samples[name] = [pop,sample,str(count)]
		
		
for i in samples.items():
	print (i[0]+"\t"+"\t".join(i[1]))
