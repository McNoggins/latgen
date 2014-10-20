# -*- coding: utf-8 -*-

__author__ = 'Denis Gagnon'
__email__ = 'gagnon88@gmail.com'
__version__ = '0.1.0'

from __future__ import print_function
try:
    from .latgen import honeycomb
except ImportError as e:
    import sys
    print('''\
Could not import submodules (exact error was: {0}).
'''.format(e), file=sys.stderr)