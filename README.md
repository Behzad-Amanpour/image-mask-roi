# Extracting Medical Image Values Inside ROI / Binary Mask (Python) 

In **code.py** you will see how to extract a medical image values which are placed inside a mask ro an ROI

- A medical image usually has the folowing formats:

  - DICOM for 2D images
  
  - NIfTI for 3D images

- And the mask usualy has the following formats

  - JPG / PNG for 2D mask (You can draw it with ImageJ software on DICOM Images)

  - NIfTI for 3D mask (You can draw it with ITKSNAP software on NIfTI images)



# DICOM-to-NIfTI Conversion (dicom2nifti in Python)

- A DICOM file is a 2D image plus a lot of information in its header. A 3D volume is stored as a sequence of DICOM images (2D slices)

- A NIfTI file is a 3D image (a volume) plus a simpler header than DICOM.

- In **code.py** you will see:

     - Converting a folder of DICOM images to a NIfTI file

     - Converting multiple DICOM folders to NIfTI images simultaneously
     
- There are some software packages for converting DICOM to NIfTI if you do not want to use Python code, such as **dcm2niigui** and **mricron**


