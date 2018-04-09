#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/9.
# 常量
import os

USER_HOME = os.path.expanduser("~")
AK_HOME = os.path.join(USER_HOME, ".ak")
AK_LOCAL_CONFIG = os.path.join(AK_HOME, "config.json")
AK_SCRIPT = os.path.join(AK_HOME, "ak")

AK_REMOTE_CONFIG_URL = "https://raw.githubusercontent.com/wswenyue/ak/install/config"

AK_VERSION_MAIN = "version_main"
AK_VERSION_MINOR = "version_minor"
AK_TARGET_URL = "target"
