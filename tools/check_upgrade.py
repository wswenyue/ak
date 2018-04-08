#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.
from urllib import request
url = ""
s = request.urlopen(url).read().decode('utf8')
