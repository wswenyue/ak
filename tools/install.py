#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wswenyue on 2018/4/8.


import io
import os
import shutil
import subprocess
import sys
import zipfile

import requests


class AkInstaller(object):

    def __init__(self):
        self._config = None

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

    def get_remote_config(self):
        if self._config is None:
            from urllib import request
            import json
            url = "https://raw.githubusercontent.com/wswenyue/ak/install/config"
            data = request.urlopen(url).read().decode('utf8')
            self._config = json.loads(data)
        return self._config

    def get_remote_version(self):
        config = self.get_remote_config()
        version_main = config.get('version_main', 0)
        version_minor = config.get('version_minor', 0)
        return version_main, version_minor

    def get_target_url(self):
        config = self.get_remote_config()
        target = config.get('target', "")
        return target

    @staticmethod
    def download_extract_zip(zip_url, path):
        response = requests.get(zip_url)
        the_zip = zipfile.ZipFile(io.BytesIO(response.content))
        for name in the_zip.namelist():
            file_name = name[name.find("/") + 1:]
            if AkInstaller.is_empty(file_name):
                continue
            target_file_path = os.path.join(path, file_name)
            save_file = open(target_file_path, "wb")
            save_file.write(the_zip.read(name))
            save_file.close()
        the_zip.close()

    @staticmethod
    def build_ak_home():
        home = os.path.expanduser("~")
        ak_home = os.path.join(home, ".ak")
        AkInstaller.remove_file(ak_home)
        os.makedirs(ak_home)
        return ak_home

    @staticmethod
    def link_ak_script(ak):
        AkInstaller.remove_file("/usr/local/bin/ak")
        link = ['ln', '-s', ak, '/usr/local/bin/ak']
        try:
            subprocess.Popen(link, stdout=subprocess.PIPE)
        except OSError as e:
            print(e)
            raise e

    @staticmethod
    def set_ak_script_exe(ak):
        if not os.path.exists(ak):
            return
        exe = ['chmod', '+x', ak]
        try:
            subprocess.Popen(exe, stdout=subprocess.PIPE)
        except OSError as e:
            print(e)
            raise e

    @staticmethod
    def delete_ak(ak_home):
        AkInstaller.remove_file(ak_home)
        AkInstaller.remove_file("/usr/local/bin/ak")


def main(orig_args):
    ak = AkInstaller()
    ak_path = ak.build_ak_home()
    if ("uninstall" in orig_args) or ("delete" in orig_args):
        print("uninstall ak begin")
        ak.delete_ak(ak_path)
    else:
        print("install ak")
        url = ak.get_target_url()
        ak.download_extract_zip(url, ak_path)
        ak_script = os.path.join(ak_path, 'ak')
        ak.link_ak_script(ak_script)
        ak.set_ak_script_exe(ak_script)
    print("over !!!")


if __name__ == '__main__':
    main(sys.argv[1:])
