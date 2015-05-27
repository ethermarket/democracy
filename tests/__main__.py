from __future__ import print_function
import importlib
import sys
from __init__ import *

TESTRUNNERS = [
    ('pytest', ['tests/__init__.py']),
    ('nose', []),
    ('unittest', [])
]

for runner in TESTRUNNERS:
    try:
        module = importlib.import_module(runner[0])
        module.main(*runner[1])
        break

    except ImportError:
        if runner == TESTRUNNERS[-1]:
            print("ERROR: Unable to find any of the following test runners: %s"
                    % ', '.join(TESTRUNNERS), file=stderr)
