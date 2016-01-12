#!/bin/bash -x
echo "This script will change box files: box size / coarse factor / remove boxes too close to micrograph edge"
[ -d new_boxes ] && rm -rf new_boxes
mkdir new_boxes
#get original box size, mic size, blow factor and distance
echo -n "Micrograph size for input boxes (px): [default 1024] "
read micSize
: micSize=${micSize:=1024}
boxFile=`ls *.box | head -1`
[ ! -f $boxFile ] && echo "No box files found!" && exit 1
boxSize=`awk 'NR==2{print $3}' $boxFile`
echo -n "Blow factor to apply (e.g., use -2 to coarse twice or +4 to increase boxes 4 times): [default +2] "
read blowFactor
: blowFactor=${blowFactor:="+2"}
factor=`echo "$blowFactor" | sed 's/[^1-9]//g'`
(echo $blowFactor | grep "+") && blow=1 || blow=0
[ $blow -eq 1 ] && newBoxSizeDef=$((boxSize*factor)) || newBoxSizeDef=$((boxSize/factor))
echo -n "Choose new box size (px): [default $newBoxSizeDef] "
read newBoxSize
: newBoxSize=${newBoxSize:=$newBoxSizeDef}
echo -n "Min distance from box edge to micrograph boundary (px): [default 2] "
read boxDist
: boxDist=${boxDist:=2}
#calculate new mic edges
[ $blow -eq 1 ] && newMicSize=$((micSize*factor)) || newMicSize=$((micSize/factor))
micEdge=$((newMicSize-boxDist))
#check box files
for filename in `ls *.box`
do
        awk -v micEdge=$micEdge -v boxDist=$boxDist -v boxSize=$boxSize -v newBoxSize=$newBoxSize -v blow=$blow -v factor=$factor '{
        #calculate old box center
        centerX=$1+boxSize/2
        centerY=$2+boxSize/2

        #blow/coarse box size
        if ( blow==1 )
                {
                newcenterX=centerX*factor;
                newcenterY=centerY*factor;
                }
        else
                {
                newcenterX=centerX/factor;
                newcenterY=centerY/factor;
                }

        #calculate new bottom left coordinates
        newCoordX=newcenterX-newBoxSize/2
        newCoordY=newcenterY-newBoxSize/2

        #calculate new box edges
        topEdge=newCoordY+newBoxSize
        bottomEdge=newCoordY
        leftEdge=newCoordX
        rightEdge=newCoordX+newBoxSize

        #check edges
        if( leftEdge>boxDist && rightEdge<micEdge && topEdge<micEdge && bottomEdge>boxDist )
                {
                $1=newCoordX;
                $2=newCoordY;
                $3=newBoxSize;
                $4=newBoxSize;
                print;
                }
        }' $filename > new_boxes/${filename}
done
echo "Done!"
