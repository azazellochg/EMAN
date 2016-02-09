#!/usr/bin/env python
# simple script to do camera normalization correction (see Afanasyev et al., Scientific Reports 5, 2015),
# given known average and std images for the uncorrected stack

from EMAN2 import *

stack = "stack_uncorr.hdf"
average = EMData("average.mrc")
sigma = EMData("sigma.mrc")

count = EMUtil.get_image_count(stack)

# note we only need to keep one image in memory at a time
for i in xrange(count):
    image = EMData(stack,i)
    corr_image = (image - average) / sigma
    corr_image.write_image("stack_corr.hdf",-1) 
