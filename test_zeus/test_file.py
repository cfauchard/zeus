#!/usr/bin/env python3
# coding: utf8
# -----------------------------------------------------------------
# zeus: test_file.py
#
# Define zeus.file.* unittest nose2 format
#
# Copyright (C) 2016-2018, Christophe Fauchard
# -----------------------------------------------------------------

import zeus
import os
import nose2

def test_Path():
    """
    unittest for zeus.file.Path class
    """
    srcpath = "./tmp/test/test_Path"
    path = zeus.file.Path(srcpath)
    assert path.path == srcpath
    assert os.path.exists(path.path)
    path.delete()
    assert not os.path.exists(path.path)
    os.rmdir("./tmp/test")
    os.rmdir("./tmp")

if __name__ == '__main__':
    test_Path()
