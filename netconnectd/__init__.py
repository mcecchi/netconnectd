from __future__ import (print_function, absolute_import)

from netconnectd.client import client
from netconnectd.server import server



from netconnectd._version import get_versions
__version__ = get_versions()['version']
del get_versions
