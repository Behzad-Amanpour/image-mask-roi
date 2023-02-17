"""
Inputs:
    You can use "Image.dcm" which I uploaded as a file
"""

import numpy as np

# 2D DICOM Image & 2D png or jpg Mask ================== Behzad Amanpour ======================= 
from pydicom import dcmread
import cv2

Im = dcmread('address on your drive/Image.dcm').pixel_array
mask = cv2.imread('address on your drive/mask.dcm') 
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)         # png/jpg image is colorful and you need to convert it to gray scale image
mask[mask!=0] = 1         # the mask image should be binary (zero value for the background and value '1' inside the ROI )

# 3D NIfTI Image & Mask ================================ Behzad Amanpour ======================= 
import nibabel as nib

Im_file = nib.load('Image.nii')
Im = Im_file.get_fdata()
mask_file = nib.load('mask3D.nii')
mask = mask_file.get_fdata()
mask[mask!=0] = 1

# Extracting Values Inside ROI ========================= Behzad Amanpour =======================
data = Im[mask!=0]

# Writing the Masked Image ============================= Behzad Amanpour =======================
Im_masked=Im*mask



Im_file2 = nib.Nifti1Image(Im_masked, Im_file.affine, Im_file.header)
nib.save(Im_file2, 'Image_masked.nii')
