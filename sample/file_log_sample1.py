#!/usr/bin/env python3
# coding: utf8
#-----------------------------------------------------------------
# zeus: parser_ini_sample.py
#
# process launcher
#
# Copyright (C) 2016, Christophe Fauchard
#-----------------------------------------------------------------

import sys
import zeus

print("version zeus: " + zeus.__version__)
print("Running tests for file.py...")

print("testing class Log...")

try:
    log_file = 'file_sample1.log'
    print("create log file: " + log_file)
    log = zeus.Log(log_file)
    print("writing datas in log file")
    log.print("data")
    print("closing log file")
    log.close()

    print("Class Log passed")

except:
    print("Class Log not passed, Unexpected error:", sys.exc_info()[0])
