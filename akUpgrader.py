#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.
# version(1,1) 版本依次是：主版本，次版本
# 远端主版本大，强制升级
# 远端主版本一致，次版本大，推荐升级
import config


def check_upgrade():
    remote_ver = config.get_remote_version()
    local_ver = config.get_local_version()
    if remote_ver[0] > local_ver[0]:
        print("强制升级")
    elif remote_ver[1] > local_ver[1]:
        print("建议升级")
    else:
        print("不升级")
