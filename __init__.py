#-----------------------------------------------------------------
# zeus: __init__.py
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import sys
from zeus._version import __version__, __version_info__

__author__ = "Christophe Fauchard <christophe.fauchard@gmail.com>"

if sys.version_info < (3, 5):
    raise RuntimeError('You need Python 3.5+ for this module.')

from zeus.file import Log
from zeus.parser import ConfigParser
from zeus.exception import FileNotFoundException, InvalidConfigurationFileException

__all__ = [ 'Log',
            'ConfigParser',
            'FileNotFoundException',
            'InvalidConfigurationFileException' ]
