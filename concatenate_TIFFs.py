## Author: Kang
## Last Update: 2024-10-16
## Usage: To concatenate discrete tiff files. e.g 20240827.tiff, 20240827@0001.tiff, 20240827@0002.tiff...

## Modules
import os, glob
import skimage.io as skio
import numpy as np
from time import time
from icecream import ic
ic.configureOutput(prefix="debug | ", includeContext=False)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFileDialog, QApplication, QMessageBox
        

## Functions
# 1. Generate a dialog to request file directory
def get_folder():
    caption = 'Please choose a directory of expdata which contains both ".tif" and ".rec" files.'
    init_dir = ""
    dialog = QFileDialog()
    dialog.setWindowTitle(caption)
    dialog.setDirectory(init_dir)
    dialog.setFileMode(QFileDialog.FileMode.Directory)
    check = dialog.exec()
    if check:
        return dialog.selectedFiles()[0]

# 2. Generate a dialog to ask if include subfolders in the designated file directory
def inCludeSubFolders():
    font = QFont()
    font.setFamily("Microsoft Yahei")
    font.setPointSize(12)
    dialog = QMessageBox()
    dialog.setWindowTitle("Question Dialog")
    dialog.setFont(font)
    dialog.setText('Do you want to include the subfolders in the chosen directory?')
    dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dialog.setIcon(QMessageBox.Question)
    answer = dialog.exec()

    if answer == QMessageBox.Yes:
        print("subfolders are included!")
        return "Yes"
    else:
        print("subfolders are ignored!")
        return "No"

# Set event handler
app = QApplication()

# Get a directory of experiment data
dir_expdata = get_folder()

# Request path of files
if dir_expdata != None:
    print("<Dir Selected>", dir_expdata)
    # Check if include subfolers in the designate directory
    includeSubDirs = inCludeSubFolders()
    if includeSubDirs == "Yes":      
        subFolders = next(os.walk(os.path.join(dir_expdata)))[1]
        subFolders.insert(0,"")
        if "merged" in subFolders:
            subFolders.remove("merged")
        print("subfolders: ",subFolders)
        for d in subFolders:
            # Scan tifs and recs which need to be merged in each subfolder
            dir_subfolders = os.path.join(dir_expdata,d)
            list_of_tifs = [os.path.basename(i) for i in glob.glob(os.path.join(dir_subfolders,'*.tif'))]
            list_of_recs_toBeMerged = [item.split("@")[0] for item in list_of_tifs if "@0001" in item]
            
            print('Files to be merged: ',list_of_recs_toBeMerged)

            if list_of_recs_toBeMerged == []:
                print("No tif file in", dir_subfolders, "needs to be merged.")
            else:
                # Check if output folder exist
                if os.path.isdir(os.path.join(dir_subfolders,"merged")):
                    print("Output folder exist.")
                else:
                    os.mkdir(os.path.join(dir_subfolders,"merged"))
                    print("Output folder is created.")
                
                # Start to concatenate discrete tif files
                for idx, file in enumerate(list_of_recs_toBeMerged):
                    t_start = time()
                    print("merging "+ file + ".tif " + f'[{idx+1:02d}/{len(list_of_recs_toBeMerged):02d}]')
                    # Load the first segment of the file
                    tif_segment_0 = skio.imread(os.path.join(dir_subfolders, file + ".tif"))
                    
                    # The counter of the segment, start from 0001
                    order_of_tif_segment = 1
                    
                    # Keep load and merge file@000X to file
                    while(os.path.isfile(os.path.join(dir_subfolders, file+"@"+"{:04d}".format(order_of_tif_segment) + ".tif"))):
                        tif_segment = skio.imread(os.path.join(dir_subfolders, file+"@"+"{:04d}".format(order_of_tif_segment) + ".tif"))
                        tif_segment_0 = np.append(tif_segment_0, tif_segment, axis=0)
                        order_of_tif_segment += 1
                    
                    skio.imsave(os.path.join(dir_subfolders,"merged", "m_"+file+".tif"), tif_segment_0.astype('uint16'), check_contrast=False)
                    print("Time elapsed: ", round(time()-t_start,2), "s")    
        print("Merging Completed!!")
        # prompt = input("\n<<Press Enter to exit>>")
    else:
        # Scan tifs and recs which need to be merged in the directory
        list_of_tifs = [os.path.basename(i) for i in glob.glob(os.path.join(dir_expdata,'*.tif'))]
        list_of_recs_toBeMerged = [item.split("@")[0] for item in list_of_tifs if "@0001" in item]
        
        print('Files to be merged: ',list_of_recs_toBeMerged)

        if list_of_recs_toBeMerged == []:
            print("No tif file in", dir_expdata, "needs to be merged.")
        else:
            # Check if output folder exist
            if os.path.isdir(os.path.join(dir_expdata,"merged")):
                print("Output folder exist.")
            else:
                os.mkdir(os.path.join(dir_expdata,"merged"))
                print("Output folder is created.")
            
            # Start to concatenate discrete tif files
            for idx, file in enumerate(list_of_recs_toBeMerged):
                t_start = time()
                print("merging "+ file + ".tif " + f'[{idx+1:02d}/{len(list_of_recs_toBeMerged):02d}]')
                # Load the first segment of the file
                tif_segment_0 = skio.imread(os.path.join(dir_expdata, file + ".tif"))
                
                # The counter of the segment, start from 0001
                order_of_tif_segment = 1
                
                # Keep load and merge file@000X to file
                while(os.path.isfile(os.path.join(dir_expdata, file+"@"+"{:04d}".format(order_of_tif_segment) + ".tif"))):
                    tif_segment = skio.imread(os.path.join(dir_expdata, file+"@"+"{:04d}".format(order_of_tif_segment) + ".tif"))
                    tif_segment_0 = np.append(tif_segment_0, tif_segment, axis=0)
                    order_of_tif_segment += 1
                
                # tifftools.write_tiff(tif_segment_0,os.path.join(dir_expdata,"merged", "m_"+file+".tif"), tif_segment_0.astype('uint16'), check_contrast=False)
                skio.imsave(os.path.join(dir_expdata,"merged", "m_"+file+".tif"), tif_segment_0.astype('uint16'), check_contrast=False)
                print("Time elapsed: ", round(time()-t_start,2), "s")
                    # bar_current()
            print("Merging Completed!!")
            # prompt = input("\n<<Press Enter to exit>>")
else:
    print('Selected directory = ',dir_expdata)
    print("Process cancelled!")
    # prompt = input("\n<<Press Enter to exit>>")

            
