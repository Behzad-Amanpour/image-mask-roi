# Extracting Medical Image Values Inside ROI / Binary Mask (Python) 

A medical image usually has the folowing formats:

  - DICOM for 2D images
  
  - NIfTI for 3D images

And the mask usualy has the following formats:

  - JPG / PNG for 2D mask (You can draw it with ImageJ software on DICOM Images)

  - NIfTI for 3D mask (You can draw it with ITKSNAP software on NIfTI images)

In **code.py** you will see how to extract a medical image values which are placed inside a mask ro an ROI
