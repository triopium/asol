import logging
import os
import sys
LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
logging.basicConfig(level=LOGLEVEL)
logging.getLogger().handlers.clear()

### stderr
handler_stderr = logging.StreamHandler(sys.stderr)
formatter_stderr = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_stderr.setFormatter(formatter_stderr)
