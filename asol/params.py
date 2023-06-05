import argparse
import os
import sys
from typing import Dict
import logging
from . import logger
logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)

def args_read() -> Dict[str, any]:
    # logerr.info("parsing params")
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", required=False, type=str, help="Input filename",default=get_default_sourcedir())

    parser.add_argument("-o", "--output", required=False, type=str, help="output filename",default=get_default_targetdir())

    parser.add_argument("-w", "--write", required=False, help="actually write the files",action='store_true')

    parser.add_argument("-v", "--version", required=False, help="version of program",action='store_true')

    parser.add_argument("-pd", "--params-debug", required=False, help="print parameters",action='store_true')

    parser.add_argument("-pc", "--params-check", required=False, help="check parameters validity",action='store_true')

    parser.add_argument("-s", "--simulate", required=False, help="check parameters validity",action='store_true')

    params=parser.parse_args()
    params.input=os.path.abspath(params.input)
    params.output=os.path.abspath(params.output)
    return params

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
        # dirpath=os.path.join(dirpath,"target")
    return os.path.abspath(dirpath)

# def GetPathCmdEnvCwd(dirpath: str) -> str:
    # """
    # Get path from commandlie input, env variable, or current dir. In order of decreasing preference
    # """
    # if dirpath is None or dirpath == "":
        #### from environ
        # dirpath=os.environ.get('SOURCE_DIRECTORY')
        # if dirpath is None or dirpath == "":
            # #### from current dirpath
            # dirpath=os.getcwd()

        # dstdir=os.path.join(dstdir,"target")
    # return os.path.abspath(dirpath)



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
