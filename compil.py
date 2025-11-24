#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import subprocess
import os

folder_1 = os.getcwd()
subprocess.call(f'python -m PyInstaller --onefile --icon=icon/icon.ico --noconsole --name MEASControl {folder_1}\\main.py')
