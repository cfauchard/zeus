#!/usr/bin/env python3
# coding: utf8
# -----------------------------------------------------------------
# zeus: zeus_nose2.py
#
# run all unit tests with nose2
#
# Copyright (C) 2016-2018, Christophe Fauchard
# -----------------------------------------------------------------

import sys

if __name__ == '__main__':
  import nose2
  sys.argv.append("test_zeus")
  sys.argv.append("-v")
  nose2.discover()
