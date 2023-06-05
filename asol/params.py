import argparse
import os
import sys
from typing import Dict
import logging
from . import logger
log = logging.getLogger(__name__)
log.addHandler(logger.handler)

def args_read() -> Dict[str, any]:
    # log.info("parsing params")
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=False, type=str, help="Input filename",default=get_default_sourcedir())

    parser.add_argument("-o", "--output", required=False, type=str, help="output filename",default=get_default_targetdir())

    parser.add_argument("-w", "--write", required=False, help="actually write the files",action='store_true')

    parser.add_argument("-v", "--version", required=False, help="version of program",action='store_true')

    parser.add_argument("-dp", "--debug-params", required=False, help="print parameters",action='store_true')
    return parser.parse_args()

def get_default_sourcedir() -> str:
    dirpath=os.environ.get('SOURCE_DIRECTORY')
    if dirpath is None or dirpath == "":
        #### from current dirpath
        dirpath=os.getcwd()
    return os.path.abspath(dirpath)

def get_default_targetdir() -> str:
    dirpath=os.environ.get('TARGET_DIRECTORY')
    if dirpath is None or dirpath == "":
        #### from current dirpath
        dirpath=os.getcwd()
    return os.path.abspath(dirpath)

def GetPathCmdEnvCwd(dirpath: str) -> str:
    """
    Get path from commandlie input, env variable, or current dir. In order of decreasing preference
    """
    if dirpath is None or dirpath == "":
        #### from environ
        dirpath=os.environ.get('SOURCE_DIRECTORY')
        if dirpath is None or dirpath == "":
            #### from current dirpath
            dirpath=os.getcwd()

        # dstdir=os.path.join(dstdir,"target")
    return os.path.abspath(dirpath)


def ParamsPrepare():
    """
    Check that parametrs are valid
    """
    pars=args_read()
    # print(pars)
    # parss=pars.Namespace()
    srcdir=GetPathCmdEnvCwd(pars.input)
    dstdir=GetPathCmdEnvCwd(pars.output)
    
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
    pars.input=srcdir
    pars.output=dstdir
    return pars

    # pars=ParamsPrepare()

# def ParamsCheck():
    # pars=ParamsPrepare()
