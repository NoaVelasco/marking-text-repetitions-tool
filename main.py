#!/usr/bin/env python3.10
# Python 3.10.2 UTF-8
# Copyright (c) 2023, Noa Velasco
# pylint: disable=C0103
"""Browses through the current path to choose a text file
and do amazing stuff with it."""


from pathlib import Path
import paths
import textfiles


if __name__ == "__main__":
    current = Path.cwd()
    content = paths.scan_dir(current)
    file = paths.looping(current, content)
    textfile = textfiles.Coinsidensias(file)
    textfile.writefiles()
