# About the project
DicomVisualizer is a simple DICOM file visualizer based on Python. It can visualize single slide or a sequence by simply indicating the DIR.  The code is written in python3. It is particularly useful for Radiomics operations, segmentation, and related tasks.

Usage:
There is a main file named DicomVisualizer.py placed in the Source dir. 
There are two DICOM files examples:
..\EXAMPLE\    		 <---- This DIR contains a set of slides related to a Brain RMN   
IMG-0003-0020.dcm  <---- A single DICOM slide
Source\DicomVisualizer.py   <---The SW

To run the sw you have only to run it with the following command directly in the source dir:
python3 DicomVisualizer.py 

It will ask the name of a DICOM file or a DIR containing a set of DICOM slides as follow:

Insert Filename or Dir that contain the DCM files:../EXAMPLE/     <--- If you want to visualize a sequence

Insert Filename or Dir that contain the DCM files:../IMG-0003-0020.dcm     <--- If you want to visualize a single slide.
 
on the terminal the SW will print the some DICOM  file information:

Press: ESC to exit, SPACE bar for the previous slide,
any other key for the next slide.
_______________________________________
X Res.       [mm]: 0.224609375
Y Res.       [mm]: 0.224609375
Slices Res.  [mm]: 1
Dimensions: 1024 X 1024
_______________________________________

License:
See LICENSE.txt for more information.

Contact: Massimo Donelli - massimo.donelli@unitn.it 

Project link: 