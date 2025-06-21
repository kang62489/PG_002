## Author: Kang
## Last Update: 2024-10-16
## Usage: To concatenate discrete tiff files. e.g 20240827.tiff, 20240827@0001.tiff, 20240827@0002.tiff...

## Modules
import os, glob
import tifffile
import numpy as np
from time import time
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFileDialog, QApplication, QMessageBox
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme

# Initialize rich console with custom theme
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "red bold",
    "success": "green",
})
console = Console(theme=custom_theme)

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
        console.print("[success]Subfolders are included!")
        return "Yes"
    else:
        console.print("[warning]Subfolders are ignored!")
        return "No"

def process_directory(directory, files_to_merge):
    """Process files in a directory"""
    if not files_to_merge:
        console.print(f"[warning]No tif files in {directory} need to be merged.")
        return

    # Check/create output folder
    merged_dir = os.path.join(directory, "merged")
    if os.path.isdir(merged_dir):
        console.print("[info]Output folder exists.")
    else:
        os.mkdir(merged_dir)
        console.print("[success]Output folder created.")

    for idx, file in enumerate(files_to_merge, 1):
        t_start = time()
        console.print(f"[cyan]Processing {file}.tif [{idx}/{len(files_to_merge)}]")

        try:
            # Use tifffile to read all segments and concatenate at once
            segments = [tifffile.imread(os.path.join(directory, f"{file}.tif"))]
            order = 1
            
            while os.path.isfile(os.path.join(directory, f"{file}@{order:04d}.tif")):
                segments.append(tifffile.imread(os.path.join(directory, f"{file}@{order:04d}.tif")))
                order += 1
                
            # Concatenate all at once (faster than repeated appends)
            merged_tiff = np.concatenate(segments, axis=0)
            
            # Save merged file
            output_path = os.path.join(merged_dir, f"m_{file}.tif")
            tifffile.imwrite(output_path, merged_tiff.astype('uint16'))
            
            elapsed = round(time() - t_start, 2)
            console.print(f"[success]Time elapsed: {elapsed}s")

        except Exception as e:
            console.print(f"[error]Error processing {file}: {str(e)}")

def main():
    # Initialize Qt application
    app = QApplication()

    # Get directory of experiment data
    dir_expdata = get_folder()

    if dir_expdata is None:
        console.print("[error]No directory selected. Process cancelled!")
        return

    console.print(Panel(f"Selected Directory: {dir_expdata}", 
                       title="[bold cyan]Directory Selection",
                       border_style="cyan"))

    # Process directories based on user choice
    includeSubDirs = inCludeSubFolders()
    
    if includeSubDirs == "Yes":
        subFolders = next(os.walk(dir_expdata))[1]
        subFolders.insert(0, "")  # Include root directory
        if "merged" in subFolders:
            subFolders.remove("merged")
        
        console.print(Panel(
            "\n".join(subFolders) or "No subfolders found",
            title="[bold cyan]Subfolders to Process",
            border_style="cyan"
        ))

        for d in subFolders:
            dir_subfolders = os.path.join(dir_expdata, d)
            console.print(f"\n[bold cyan]Processing directory: {dir_subfolders}")
            
            # Get files to merge
            list_of_tifs = [
                os.path.basename(i) 
                for i in glob.glob(os.path.join(dir_subfolders, '*.tif'))
            ]
            files_to_merge = [
                item.split("@")[0] 
                for item in list_of_tifs 
                if "@0001" in item
            ]
            
            console.print(Panel(
                "\n".join(files_to_merge) or "No files to merge",
                title="[bold cyan]Files to Merge",
                border_style="cyan"
            ))
            
            process_directory(dir_subfolders, files_to_merge)
    else:
        # Process only main directory
        list_of_tifs = [
            os.path.basename(i) 
            for i in glob.glob(os.path.join(dir_expdata, '*.tif'))
        ]
        files_to_merge = [
            item.split("@")[0] 
            for item in list_of_tifs 
            if "@0001" in item
        ]
        
        console.print(Panel(
            "\n".join(files_to_merge) or "No files to merge",
            title="[bold cyan]Files to Merge",
            border_style="cyan"
        ))
        
        process_directory(dir_expdata, files_to_merge)

    console.print("\n[bold green]Merging Completed![/]")

if __name__ == "__main__":
    main()            
