#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.

import json
import urllib2

import const
from tools import fileUtil


def get_remote_version():
    config = __get_remote_config()
    version_main = config.get(const.AK_VERSION_MAIN, 0)
    version_minor = config.get(const.AK_VERSION_MINOR, 0)
    return version_main, version_minor


def get_local_version():
    config = __load_local_config()
    version_main = config.get(const.AK_VERSION_MAIN, 0)
    version_minor = config.get(const.AK_VERSION_MINOR, 0)
    return version_main, version_minor


def get_target_url():
    config = __get_remote_config()
    target = config.get(const.AK_TARGET_URL, "")
    return target


__CONFIG = {}
__CONFIG_LOCAL = {}


def __get_remote_config():
    global __CONFIG
    if not __CONFIG:
        print("config empty")
        url = const.AK_REMOTE_CONFIG_URL
        data = urllib2.urlopen(url).read().decode('utf8')
        __CONFIG = json.loads(data)
    else:
        print("config not empty")

    print(__CONFIG)
    return __CONFIG


def __load_local_config():
    global __CONFIG_LOCAL
    if not fileUtil.file_exists(const.AK_LOCAL_CONFIG):
        print("local config file not exists")
        return __CONFIG_LOCAL

    if not __CONFIG_LOCAL:
        print("load local config")
        with open(const.AK_LOCAL_CONFIG, "r") as f:
            data = f.read()
            __CONFIG_LOCAL = json.loads(data)
            print("load local config succeed")
    print("load local config")
    return __CONFIG_LOCAL


def __save_local_config():
    global __CONFIG_LOCAL
    if not __CONFIG_LOCAL:
        return False
    fileUtil.make_file_not_exists(const.AK_LOCAL_CONFIG)
    with open(const.AK_LOCAL_CONFIG, "w") as f:
        f.write(json.dumps(__CONFIG_LOCAL))
        f.flush()
    return True
