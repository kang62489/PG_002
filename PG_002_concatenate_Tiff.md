---
Established: 2024-12-21
Last Updated: 2024-12-28
Description: This python program is used to concatenate discrete tiff files exported by PCO.camware
tags:
  - python
  - img_process
---
# Results
The program will automatically generate a folder "merged" (if it is exist, the program would delete it first) contains merged files start with prefix "m_".
![](<The auto-generated output folder.png>)
![](<merged files.png>)

# MEMO
- If the size of a single imaging file recorded during experiments over 2GB, the acquisition software -- pco.camware, would automatically divide the file into segments. To concatenate the discrete files, the python program "concatenate_TIFFs.py" were made to solve the issue.
- The .rec files with the same prefix name of the discrete files must be at same directory so that the python program can detect.