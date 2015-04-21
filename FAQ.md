## List of frequently used commands / options in EMAN2

#### e2proc2d.py / e2proc3d.py

  * normalize 2D: avg = 0, stdev = 1
`--process=normalize.edgemean`

  * remove Xray pixels
`--process=threshold.clampminmax.nsigma:nsigma=4`

  * threshold from both sides
`--process=threshold.clampminmax:maxval=${UpperThres}:minval=${LowerThres}`

  * invert contrast
`--mult -1`

  * shrink
`--meanshrink 2`

  * calculate power spectrum
`--process=math.realtofft`

  * apply soft Gaussian mask 
`--process=mask.soft:inner_radius=20`

  * low-pass Gaussian filter: 10A
`--process=filter.lowpass.gauss:apix=1.71:cutoff_freq=0.1`

  * high-pass Gausiian filter: 50A
 `--process=filter.highpass.gauss:apix=1.71:cutoff_freq=0.5`

  * apply a soft circle/sphere of 30px radius
 `--process=testimage.circlesphere:fill=1:radius=30 --process=mask.soft:inner_radius=30`

  * convert mrc SerialEM stack to tifs
`e2proc2d.py ${i}.mrc ${i}.tif --unstacking --threed2twod`

-----

