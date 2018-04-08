#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.


def check_upgrade():
    if _get_remote_version() > _get_local_version():
        print("update")
    else:
        print("none")


def _get_remote_version():
    from urllib import request
    import json
    url = "https://raw.githubusercontent.com/wswenyue/ak/master/config"
    data = request.urlopen(url).read().decode('utf8')
    config = json.loads(data)
    version = config.get('version', 0)
    return version


def _get_local_version():
    return 1


check_upgrade()
