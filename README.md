# ASOL
- soulution to assignment at 
# Installation
# Usage
## usage examples
 
# Treating errors
Errors are written to stderr. Stderr can be piped to file.
Errors can be filtered by type. Errors also contains filename. 

The filtered list can than be used to further process source directory:
1. Run again if files were locked.
2. Run again after changing permissions.
3. Run again after ammending invalid json.
4. If filename date differs from json field:
-there can be commandline switch to specify preference
a) ammend filename date acording to json field
b) ammend json field acording to filename
c) ammend dates according to other logic
Best option would be to look at process which is generating the source files.







