EMAN
====

EMAN conventions can be found here: https://github.com/azazellochg/3DEM-conventions/blob/master/eman2.md

### Scripts for EMAN2

##### FAQ

My list of frequently used commands / options in EMAN2.

---

##### calculate_avg_std.py

Calculate average and standard deviation images for a stack of images (stack.hdf). I usually use it on a random set of 50-100 (non-)gain-corrected movies to check if gain reference was done properly.

---

##### change_box.sh

The script will change box coordinates: apply coarse factor to downscale/upscale coordinates, change box size if requested, remove boxes too close to the mictrograph edge. New box files are in new_boxes folder.

---

##### clean_boxes.sh

This script simply removes boxes that are too close to the micrograph edge.

---

##### norm_corr.py

A simple script to do camera normalization correction (see Afanasyev et al., Scientific Reports 5, 2015), given a known avg and std images for the uncorrected movie stack

---

##### xmipp3_to_eman_boxes

Simple script for coordinate conversion from XMIPP3 to EMAN (.pos to .box)
