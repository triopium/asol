import argparse
import logging
import os
import sys
from typing import Dict

from . import logger

logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)


def args_read() -> Dict[str, any]:
    # logerr.info("parsing params")
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--input",
        required=False,
        type=str,
        help="Input filename",
        default=get_default_sourcedir(),
    )

    parser.add_argument(
        "-o",
        "--output",
        required=False,
        type=str,
        help="output filename",
        default=get_default_targetdir(),
    )

    parser.add_argument(
        "-w",
        "--write",
        required=False,
        help="actually write the files",
        action="store_true",
    )

    parser.add_argument(
        "-f",
        "--force",
        required=False,
        help="force overwrite data in target directory",
        action="store_true",
    )

    parser.add_argument(
        "--date-priority",
        required=False,
        help="Specify priority of date string for new filename",
        default="filename",
        choices=["filename", "json"],
    )

    parser.add_argument(
        "--ammend-date",
        required=False,
        help="Ammend date string in json field according to filename",
        action="store_true",
    )

    parser.add_argument(
        "-v",
        "--version",
        required=False,
        help="version of program",
        action="store_true",
    )

    parser.add_argument(
        "-pd",
        "--params-debug",
        required=False,
        help="print parameters",
        action="store_true",
    )

    parser.add_argument(
        "-pc",
        "--params-check",
        required=False,
        help="check parameters validity",
        action="store_true",
    )

    parser.add_argument(
        "--graph-count-files-week",
        required=False,
        help="Graph number of files (posts) in individual weeks. Generates a file inside source dir given by -i",
        action="store_true",
    )

    params = parser.parse_args()
    params.input = os.path.abspath(params.input)
    params.output = os.path.abspath(params.output)
    return params


def get_default_sourcedir() -> str:
    dirpath = os.environ.get("SOURCE_DIRECTORY")
    if dirpath is None or dirpath == "":
        ### from current dirpath
        dirpath = os.getcwd()
    return os.path.abspath(dirpath)


def get_default_targetdir() -> str:
    dirpath = os.environ.get("TARGET_DIRECTORY")
    if dirpath is None or dirpath == "":
        ### from current dirpath
        dirpath = os.getcwd()
        # dirpath=os.path.join(dirpath,"target")
    return os.path.abspath(dirpath)


def ParamsPrepare():
    """
    Check that parametrs are valid
    """
    pars = args_read()
    # parss=pars.Namespace()
    srcdir = GetPathCmdEnvCwd(pars.input)
    dstdir = GetPathCmdEnvCwd(pars.output)
    
    ### Maybe automatically create dstdir/target directory if target is same as source.
    # if srcdir == dstdir:
    # dstdir=os.path.join(dstdir,"target")

    ### validate srcdir
    if not os.access(srcdir, os.R_OK):
        raise ValueError(f"source dir not readable: {srcdir}")

    ### validate dstdir
    if not os.path.exists(dstdir):
        raise ValueError(f"path does not exists: {dstdir}")
    if not os.path.isdir(dstdir):
        raise ValueError(f"path is not directory: {dstdir}")
    if not os.access(dstdir, os.W_OK):
        raise ValueError(f"directory not writable: {dstdir}")
    pars.input = srcdir
    pars.output = dstdir
    return pars


