#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.

import json
import urllib2


class Config(object):
    @staticmethod
    def get_remote_config():
        if not hasattr(Config, '_config'):
            print("config empty")
            url = "https://raw.githubusercontent.com/wswenyue/ak/install/config"
            data = urllib2.urlopen(url).read().decode('utf8')
            Config._config = json.loads(data)
        else:
            print("config not empty")

        print(Config._config)
        return Config._config

    @staticmethod
    def get_remote_version():
        config = Config.get_remote_config()
        version_main = config.get('version_main', 0)
        version_minor = config.get('version_minor', 0)
        return version_main, version_minor

    @staticmethod
    def get_target_url():
        config = Config.get_remote_config()
        target = config.get('target', "")
        return target

    @staticmethod
    def get_local_version():
        return 0, 0
