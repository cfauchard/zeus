#!/usr/bin/env python3
# coding: utf8
# -----------------------------------------------------------------
# zeus: zeus_unittest.py
#
# run all module unit tests
#
# Copyright (C) 2016-2018, Christophe Fauchard
# -----------------------------------------------------------------

import argparse
import zeus
import unittest

parser = argparse.ArgumentParser(
    description='run all unit tests of zeus module')
parser.add_argument("--version", action='version', version='%(prog)s ' +
                    ' - zeus version ' + zeus.__version__)
args = parser.parse_args()

loader = unittest.TestLoader()
all_tests = loader.discover('zeus.test')
unittest.TextTestRunner(verbosity=2).run(all_tests)
