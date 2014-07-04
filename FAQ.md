## List of frequently used commands / options in EMAN2

#### e2proc2d.py

  * normalize 2D
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

  * low-pass Gaussian filter
`--process=filter.lowpass.gauss:apix=1.71:cutoff_abs=0.1`

  * convert mrc SerialEM stack to tifs
`e2proc2d.py ${i}.mrc ${i}.tif --unstacking --threed2twod`

-----

