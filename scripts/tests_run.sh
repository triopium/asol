#!/bin/bash
### current script directory
SSRCD="${BASH_SOURCE%/*}"
curdir=$PWD
tests_dir="$(realpath "${SSRCD}/../tests/")"

run_withlogs(){
# pytest --capture=tee-sys "$@"
pytest -o log_cli=true "$@"
}
"$@"
