#!/usr/bin/env python3
# coding: utf8

import sys

if __name__ == '__main__':
  import nose2
  sys.argv.append("zeus")
  sys.argv.append("-v")
  nose2.discover()
