#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.
import os

import shutil


class Tools(object):

    @staticmethod
    def is_empty(string):
        if string is None:
            return True
        elif string == "":
            return True
        elif string.strip() == "":
            return True
        else:
            return False

    @staticmethod
    def remove_file(path):
        """ param <path> could either be relative or absolute. """
        if not os.path.exists(path):
            return
        if os.path.isfile(path):
            os.remove(path)  # remove the file
        elif os.path.isdir(path):
            shutil.rmtree(path)  # remove dir and all contains
