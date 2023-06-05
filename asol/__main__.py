import logging
from . import logger
logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)

import sys
import os
from . import params
from . import runner
from . import __version__

"""
The command line interface.
"""

def main ():
    # pars=params.ParamsPrepare()
    pars=params.args_read()
    # logerr.debug("hello_jekl")
    if pars.version:
        print(__version__)
        sys.exit(0)

    run=runner.Runner(pars)
    if pars.params_debug:
        run.params_debug()
        sys.exit(0)

    if pars.params_check:
        run.params_check()
        sys.exit(0)

    if pars.simulate:
        run.simulate()
        sys.exit(0)

    # logerr.info("")
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
