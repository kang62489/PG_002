---
Established: 2024-12-21
Last Updated: 2025-06-21
Description: This python program is used to concatenate discrete tiff files exported by PCO.camware
tags:
  - python
  - imaging
---
# Use
## 1. Activate the virtual environment
### Anaconda
```powershell
conda activate <env_name>
```

## 2. Run the python script
```powershell
python concatenate_TIFFs.py
```

## 3. Select directory containing .rec files (necessary)
## 4. Determine if you want to include subfolder (also need to contain .rec files)

# Results
The program will automatically generate a folder "merged" (if it is exist, the program would delete it first) contains merged files start with prefix "m_".
![600](<The auto-generated output folder.png>)
![600](<merged files.png>)

# MEMO
- If the size of a single imaging file recorded during experiments over 2GB, the acquisition software -- pco.camware, would automatically divide the file into segments. To concatenate the discrete files, the python program "concatenate_TIFFs.py" were made to solve the issue.
- The .rec files with the same prefix name of the discrete files must be at same directory so that the python program can detect.

# Log
## 2025-Jun-21
- PG_002_concatenate_Tiff.md removed.
- Function of printing messages in the code is changed from icecream to rich.
- Code structure is optimized by Augment Code.
> [!note]
> The latest version in my GUI for experiments doesn't need the .rec files.
