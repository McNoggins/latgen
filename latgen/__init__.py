# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'Denis Gagnon'
__email__ = 'gagnon88@gmail.com'
__version__ = '0.1.0'

try:
    from .latgen import honeycomb
except ImportError as e:
    import sys
    print('''\
Could not import submodules (exact error was: {0}).
'''.format(e), file=sys.stderr)