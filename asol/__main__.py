import logging
from . import logger
logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)

import sys
import os
from . import params
from . import runner
from . import grapher
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

    if pars.graph_count_files_week:
        logerr.info("graphing count files per week")
        get_files(pars.input)
        sys.exit(0)

    ### Finally run
    run.simulate()
    sys.exit(0)


if __name__ == '__main__':
    main()
