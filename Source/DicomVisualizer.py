# -*- coding: utf-8 -*-
# .. Project DicomVisualizer, V1.0 March 8, 2026 - Massimo Donelli - Problem definitions and main routines ..
# .. Project DicomVisualizer is a simpler DICOM file visualizer based on python routines ..
# .. Copyright@2026
# .. Radiomic Laboratory Department of Economic and Management (DEM)
# .. University of Trento, 38100 Trento, Italy
#
import cv2
import time
import os
import pydicom
import numpy as np
# .. Subroutines definition ..
# .. This function provide the Pixel, Slices Resolution, and Array Dimensions of a Dicomfilename ..
# .. This function provide the Pixel, Slices Resolution, and Array Dimensions of a Dicomfilename ..
def DICOM_READ(DICOM_FILE_NAME):
    DATA_SET = pydicom.dcmread(DICOM_FILE_NAME,force='True')
    DATA_ARRAY = DATA_SET.pixel_array
    PIXEL_RES_X, PIXEL_RES_Y = DATA_SET.PixelSpacing
    SLICE_RES = DATA_SET.SliceThickness
    DIM_X, DIM_Y = DATA_ARRAY.shape
    return PIXEL_RES_X, PIXEL_RES_Y, SLICE_RES, DIM_X, DIM_Y, DATA_ARRAY
# .. This Function visualize a single image 
# .. Show Image ..
def PLOT_IMAGE(ARRAY_IMG,LEVELS,TITLE):
    DATA = ((ARRAY_IMG)/np.amax(ARRAY_IMG))*(LEVELS-1);
    GRAY_IMAGE = (DATA).astype('uint8')#
    cv2.imshow(TITLE,GRAY_IMAGE)
    KEY = cv2.waitKey(0)          # .. Wait the user to press a key ..
    if KEY%256 == 27:             # .. Press ESC to quit ..
        cv2.destroyAllWindows()
        return -1  
    elif KEY%256 == 32:           # .. Press Space to go back ..
        cv2.destroyAllWindows()
        return 1   
    else:
        return 0       
# .. This function transform a numpyarray into a grayscale image and visualize it ..
def SET_IMG_VISUALIZE(PATH,ARRAY_LIST,LEVELS):
    SLIDES_NUMBER = len(ARRAY_LIST)
    PIXEL_RES_X, PIXEL_RES_Y, SLICE_RES, DIM_X, DIM_Y, DATA_ARRAY = DICOM_READ(PATH+ARRAY_LIST[0])
    print("_______________________________________")
    print("X Res.       [mm]:",PIXEL_RES_X)
    print("Y Res.       [mm]:",PIXEL_RES_Y)
    print("Slices Res.  [mm]:",SLICE_RES)
    print("Dimensions:",DIM_X,"X",DIM_Y)
    print("_______________________________________")
    I_X_FOR = 0
    FLAG = 0 
    while(True):
        if(FLAG == -1):
            exit(0)
        elif(FLAG == 1):
            if(I_X_FOR > 0):
              I_X_FOR = I_X_FOR - 1
        elif(FLAG == 0):
            if(I_X_FOR < (SLIDES_NUMBER-1)):
                I_X_FOR = I_X_FOR + 1
        #      
        PIXEL_RES_X, PIXEL_RES_Y, SLICE_RES, DIM_X, DIM_Y, DATA_ARRAY = DICOM_READ(PATH+ARRAY_LIST[I_X_FOR])
        DUMMY_STRING = "Slide n:"+ str(I_X_FOR) + " " + ARRAY_LIST[I_X_FOR]
        FLAG = PLOT_IMAGE(DATA_ARRAY,LEVELS,DUMMY_STRING)            
# .. This funcion retrieve the files from a DIR ..
def EXTRACT_DIR_LIST(PATH):
    FILES = os.listdir(PATH)
    FILE_NAMES = [I_X_FOR for I_X_FOR in FILES if os.path.isfile(os.path.join(PATH,I_X_FOR))]
    for FILE in FILE_NAMES:
        if(FILE.startswith(".")):
            FILE_NAMES.remove(FILE)
    return sorted(FILE_NAMES)
# .. Main function ..
if __name__=="__main__":
    LEVELS = 256
    PATH_OR_FILE = input("Insert Filename or Dir that contain the DCM files:")
    if(os.path.isdir(PATH_OR_FILE)):
        print("Press: ESC to exit, SPACE bar for the previous slide,")
        print("any other key for the next slide.")
        SLIDES_LIST = EXTRACT_DIR_LIST(PATH_OR_FILE)
        SET_IMG_VISUALIZE(PATH_OR_FILE,SLIDES_LIST,LEVELS)
    elif(os.path.isfile(PATH_OR_FILE)):
        PIXEL_RES_X, PIXEL_RES_Y, SLICE_RES, DIM_X, DIM_Y, DATA_ARRAY = DICOM_READ(PATH_OR_FILE)
        print("_______________________________________")
        print("X Res.       [mm]:",PIXEL_RES_X)
        print("Y Res.       [mm]:",PIXEL_RES_Y)
        print("Slices Res.  [mm]:",SLICE_RES)
        print("Dimensions:",DIM_X,"X",DIM_Y)
        print("_______________________________________")
        PLOT_IMAGE(DATA_ARRAY,LEVELS,PATH_OR_FILE)
    else:
        print("No DICOM file!")