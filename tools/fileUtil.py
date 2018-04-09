#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/9.
import errno
import os

import shutil


def make_dir_not_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def make_file_not_exists(path):
    if os.path.exists(path):
        return
    dir_path = os.path.dirname(path)
    make_dir_not_exists(dir_path)
    file(path, "w").close()


def file_exists(path):
    return os.path.exists(path) and os.path.isfile(path)


def remove_file(path):
    """ param <path> could either be relative or absolute. """
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
