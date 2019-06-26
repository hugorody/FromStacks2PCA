#!/usr/bin/sh
#This script uses samtools to convert alignment SAM files to BAM format.
#BAM files are then sorted.

#Convert SAM to BAM
for i in *.sam
do
mybam=`echo "$i" | sed "s/.sam//g"`
echo "Converting $i to $mybam.bam"
samtools view -S "$i" -u -b > "$mybam".bam
done

#Sort BAM files
for i in *.bam
do
echo "Sorting $i"
myprefix=`echo "$i" | sed "s/.bam//g"`
samtools sort "$i" "$myprefix"
done
