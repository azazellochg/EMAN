## List of frequently used commands / options in EMAN2

#### e2proc2d.py / e2proc3d.py

  * normalize 2D: avg = 0, stdev = 1

`--process=normalize.edgemean`

  * flip the hand of a 3D map: x-y plane

`e2proc3d.py map.mrc map_flip.mrc --process xform.flip:axis=z`

----
##### Test objects

  * ellipsoid
 
`e2proc3d.py :80:80:80 ellipsoid.mrc --process=testimage.ellipsoid:a=10:b=30:c=5` will create an ellipsoid in a 80px box

----
##### Thresholding

  * remove Xray pixels

`--process=threshold.clampminmax.nsigma:nsigma=4`

  * threshold from both sides

`--process=threshold.clampminmax:maxval=${UpperThres}:minval=${LowerThres}`

  * binarize image (all pixels below threshold are set to 0)

`--process=threshold.binary:value=0.7`

----

  * invert contrast

`--mult -1`

  * shrink in Fourier space

`--process math.fft.resample:n=2`

  * calculate power spectrum

`--process=math.realtofft`

  * mean average of images

`--average`

  * rotational average of images

`--process=math.rotationalaverage`

----
##### Masks and filters

  * apply soft Gaussian mask 

`--process=mask.soft:inner_radius=20`

  * low-pass Gaussian filter: 10A (1.71/10 = 0.171)

`--process=filter.lowpass.gauss:apix=1.71:cutoff_freq=0.171`

  * high-pass Gausiian filter: 50A (1.71/50 = 0.0342)

 `--process=filter.highpass.gauss:apix=1.71:cutoff_freq=0.0342`

  * create a soft circular mask of 60px radius, image 80x80px, filling 1

 `e2proc2d.py :80:80:1 mask.mrc --process=mask.soft:outer_radius=60`

  * create a soft spherical mask of 60px radius, image 80x80x80px, filling 1

 `e2proc3d.py :80:80:80:1 mask.mrc --process=mask.soft:outer_radius=60`

Mask center can be shifted from the box center by dx/dy/dz, e.g.: 

`--process=mask.soft:dx=25:dy=25:dz=25:outer_radius=20`

  * create a threshold-based mask (expand 3px) with soft edge (3px) and values [0-1]:
 
 ```bash
e2proc3d.py volume.mrc mask.mrc --process=mask.auto3d:nmaxseed=12:nshells=3:nshellsgauss=3:return_mask=1:threshold=0.0186:verbose=9 --process=threshold.clampminmax:maxval=1:minval=0
```

----
##### File conversions

  * convert mrc SerialEM stack to tifs

`e2proc2d.py ${i}.mrc ${i}.tif --unstacking --threed2twod`

  * extract several images from a file

`--first=2 --last=4`

  * create a montage (e.g., 5 images per row) from a stack file

`sxmontage.py stack.mrcs montage.mrc --N 5`
