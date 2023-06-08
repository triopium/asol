import logging

from . import logger

logerr = logging.getLogger(__name__)
logerr.addHandler(logger.handler_stderr)

import os
import sys

from . import __version__, grapher, params, runner

"""
The command line interface.
"""


def main():
    # pars=params.ParamsPrepare()
    pars = params.args_read()
    if pars.version:
        print(__version__)
        sys.exit(0)

    run = runner.Runner(pars)
    if pars.params_debug:
        run.params_debug()
        sys.exit(0)

    if pars.params_check:
        run.params_check()
        sys.exit(0)

    if pars.graph_count_files_week:
        logerr.info("graphing count files per week")
        grapher.graph_count_files_week(pars.input)
        # print(files)
        sys.exit(0)

    ### Finally run
    run.simulate()
    sys.exit(0)


if __name__ == "__main__":
    main()
