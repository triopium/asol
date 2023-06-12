import logging
import os
import sys

# LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
logging.basicConfig(level=LOGLEVEL)
logging.getLogger().handlers.clear()

### stderr
handler_stderr = logging.StreamHandler(sys.stderr)
formatter_stderr = logging.Formatter(
    "%(levelname)s - %(name)s:%(funcName)s:%(lineno)d - %(message)s"
)
handler_stderr.setFormatter(formatter_stderr)
