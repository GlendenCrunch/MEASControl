#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import subprocess
import os

folder_1 = os.getcwd()
subprocess.call('python -m PyInstaller --onefile --icon=icon/icon.ico --noconsole --name MEASControl {}\MEASControl.py'.format(folder_1))
