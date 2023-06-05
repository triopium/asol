import logging
from . import logger
log = logging.getLogger(__name__)
log.addHandler(logger.handler)
import sys
import os
from . import params
from . import runner

"""
The command line interface.
"""

def main ():
    # log.info("Starting program")
    pars=params.ParamsPrepare()
    if pars.version:
        print("my version: {__version__}")
        sys.exit(0)
    # log.info("Parsed params")
    run=runner.Runner(pars)
    # runner.count_files_norecurse(pars.input)
    ###
    # file: YYYY-MMMM-DD_DW
    # date, text
    # date in filename should be same in atribute

    # runner.ActOnParams(pars)
    # print(runner.count_files_norecurse(pars.input))
    # files_count=runner.count_files(pars.input)
    # logroot.info(f"Processing {files_count} files")

if __name__ == '__main__':
    main()