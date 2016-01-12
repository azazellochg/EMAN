#!/bin/bash
echo "This script will remove boxes that are too close to micrograph edge"
#get original box size, mic size and distance
echo -n "Original micrograph size (px): [default 1024] "
read micSize
: micSize=${micSize:=1024}
boxFile=`ls *.box | head -1`
[ ! -f $boxFile ] && echo "No box files found!" && exit 1
boxSize=`awk 'NR==2{print $3}' $boxFile`
echo -n "Min distance from box edge to micrograph boundary (px): [default 2] "
read boxDist
: boxDist=${boxDist:=2}
#calculate new mic edges
micEdge=$((micSize-boxDist))
#check box files
for filename in `ls *.box`
do
        awk -v micEdge=$micEdge -v boxSize=$boxSize '{
        topEdge=$2+boxSize
        bottomEdge=$2
        leftEdge=$1
        rightEdge=$1+boxSize
        if( leftEdge>0 && rightEdge<micEdge && topEdge<micEdge && bottomEdge>0 ){print}}' $filename > ${filename}.tmp
        mv ${filename}.tmp $filename
done
echo "Done!"
