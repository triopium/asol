#!/bin/bash
### current script directory
SSRCD="${BASH_SOURCE%/*}"
curdir=$PWD
tests_dir="$(realpath "${SSRCD}/../tests/")"

runecho(){
pytest --capture=tee-sys "$@"
}
"$@"
