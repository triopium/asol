# ASOL
- soulution to assignment at 
 
# Build
-dynamic version from git tag
-using poetry
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install poetry
poetry env use .venv/bin

-update version in pyproject.toml from git tags
poetry version $(git describe --tags --abbre=0)	
poetry build

%% /full/path/to/python
 
# Installation
pip install asol/dist/asol-(version)-whl

e.g.
pip install 'asol/dist/asol-0.1.2-py3-none-any.whl'

# Usage
- by default date from json object inside the file has higher priority than the date in filename

## Environment vars
SOURCE_DIRECTORY
TARGET_DIRECTORY
LOGLEVEL  'default INFO

## Options
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input filename
  -o OUTPUT, --output OUTPUT
                        output filename
  -w, --write           actually write the files
  -f, --force           force overwrite data in target directory
  --date-priority {filename,json}
                        Specify priority of date string for new filename
  --ammend-date         Ammend date string in json field according to filename
  -v, --version         version of program
  -pd, --params-debug   print parameters
  -pc, --params-check   check parameters validity
  --graph-count-files-week
                        Graph number of files (posts) in individual weeks. Generates
                        a file inside source dir given by -i

## Usage examples
* move files dryrun
python -m asol -i testwd/source -o testwd/target
 
* move files write
python -m asol -i testwd/source -o testwd/target -w

* move files write and ovewrite
python -m asol -i testwd/source -o testwd/target -w -f

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







