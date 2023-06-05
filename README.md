# ASOL
- soulution to assignment at 
# Usage
## Environment vars
SOURCE_DIRECTORY
TARGET_DIRECTORY
LOGLEVEL

## usage examples
python -m asol -i testwd/source -o testwd/target -s

# Build
-dynamic version from git tag
-using poetry
 
# Installation

# Treating errors
Errors are written to stderr. Stderr can be piped to file.
Errors can be filtered by type. Errors also contains filename. 
e.g.: 
python -m `asol -i inpuf -o outputf > errfile.log`
`cat errfile.log | grep "error type"`
or
python -m `asol -i inpuf -o outputf 2>&1 | grep "error type"`

The filtered list can then be used to further process source directory:
1. Run again if files were locked.
2. Run again after changing permissions.
3. Run again after ammending invalid json.
4. If filename date differs from json field:
-there can be commandline switch to specify preference
a) ammend filename date acording to json field
b) ammend json field acording to filename
c) ammend dates according to other logic
Best option would be to look at process which is generating the source files, quality of the data, and try to find a way to automate the process without manul editing.







