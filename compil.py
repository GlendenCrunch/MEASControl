# -*- coding: utf-8 -*-
import subprocess

subprocess.call(r'python -m PyInstaller --onefile --icon=icon/icon.ico --noconsole --name MEASControl C:\ITL\MEASControl\MEASControl.py')