#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.


def is_empty(string):
    if string is None:
        return True
    elif string == "":
        return True
    elif string.strip() == "":
        return True
    else:
        return False
