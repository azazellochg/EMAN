#!/usr/bin/env python
# simple script to calculate avg and std for an image stack (c) Steve Ludtke

from EMAN2 import *
import numpy as np

stack = "stack.hdf"
count = EMUtil.get_image_count(stack)

# initialize averager
std_img=EMData(stack,0)         # need to initialize with empty image same size as inputs
std_img.to_zero()
avg=Averagers.get("mean",{"sigma":std_img})

# note we only need to keep one image in memory at a time
for i in xrange(count):
    image = EMData(stack,i)
    avg.add_image(image)

avg_img=avg.finish()            # also produces std_img
avg_img.write_image("stack_avg.hdf")
std_img.write_image("stack_std.hdf")
