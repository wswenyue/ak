#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.
# version(1,1) 版本依次是：主版本，次版本
# 远端主版本大，强制升级
# 远端主版本一致，次版本大，推荐升级


def check_upgrade():
    remote_ver = _get_remote_version()
    local_ver = _get_local_version()
    if remote_ver[0] > local_ver[0]:
        print("强制升级")
    elif remote_ver[1] > local_ver[1]:
        print("建议升级")
    else:
        print("不升级")


def _get_remote_version():
    from urllib import request
    import json
    url = "https://raw.githubusercontent.com/wswenyue/ak/master/config"
    data = request.urlopen(url).read().decode('utf8')
    config = json.loads(data)
    version_main = config.get('version_main', 0)
    version_minor = config.get('version_minor', 0)
    return version_main, version_minor


def _get_local_version():
    return 0, 0


def _is_debug():
    return True


check_upgrade()
