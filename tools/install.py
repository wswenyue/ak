#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.


import io
import os
import subprocess
import sys
import zipfile

import requests

from tools.common_tools import Tools
from tools.config import Config


def download_extract_zip(zip_url, path):
    response = requests.get(zip_url)
    the_zip = zipfile.ZipFile(io.BytesIO(response.content))
    for name in the_zip.namelist():
        file_name = name[name.find("/") + 1:]
        if Tools.is_empty(file_name):
            continue
        target_file_path = os.path.join(path, file_name)
        save_file = open(target_file_path, "wb")
        save_file.write(the_zip.read(name))
        save_file.close()
    the_zip.close()


def build_ak_home():
    home = os.path.expanduser("~")
    ak_home = os.path.join(home, ".ak")
    Tools.remove_file(ak_home)
    os.makedirs(ak_home)
    return ak_home


def link_ak_script(ak):
    Tools.remove_file("/usr/local/bin/ak")
    link = ['ln', '-s', ak, '/usr/local/bin/ak']
    try:
        subprocess.Popen(link, stdout=subprocess.PIPE)
    except OSError as e:
        print(e)
        raise e


def set_ak_script_exe(ak):
    if not os.path.exists(ak):
        return
    exe = ['chmod', '+x', ak]
    try:
        subprocess.Popen(exe, stdout=subprocess.PIPE)
    except OSError as e:
        print(e)
        raise e


def main(orig_args):
    ak_path = build_ak_home()
    url = Config.get_target_url()
    download_extract_zip(url, ak_path)
    ak_script = os.path.join(ak_path, 'ak')
    link_ak_script(ak_script)
    set_ak_script_exe(ak_script)


if __name__ == '__main__':
    main(sys.argv[1:])
