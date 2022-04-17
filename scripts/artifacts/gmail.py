# gmailActive: Get gmail account information
# Author: Joshua James {joshua@dfirscience.org}
# Date: 2021-11-08
# Artifact version: 0.0.1
# Android version tested: 11
# Requirements: none

import xml.etree.ElementTree as ET

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows, open_sqlite_db_readonly, does_table_exist
import sys
import os
import time
import re
import hashlib
import sqlite3 as sq
from json import loads
from binascii import hexlify
from datetime import datetime
from datetime import timedelta
from subprocess import check_output as co
from subprocess import call

# Check OS and define adb
download_adb = ' ERROR! \n\'./adb\' file is not present!\n Unzip, and place them into this directory;\n Run the program again.'

ADB = "adb.exe"
SEP = '\\'

class keyboard_event:
    def __init__(self, id, app, text, textbox_name, textbox_id, event_date, start_date='', end_date=''):
        self.id = id
        self.app = app
        self.text = text
        self.textbox_name = textbox_name
        self.textbox_id = textbox_id
        self.event_date = event_date
        self.start_date = start_date
        self.end_date = end_date

def get_gmailActive(files_found, report_folder, seeker, wrap_text):
    #logfunc("If you can read this, the module is working!")
    logfunc("Function Called")
    # A version
    BUILDPROP = co([ADB, 'shell', 'cat', '/system/build.prop']).decode('UTF-8')
    for aver in BUILDPROP.split('\n'):
        if 'ro.build.version.release' in aver:
            ANDROID_VER = aver.strip().split('=')[1]
    # try:
    #     print(" Android version: " + ANDROID_VER); REPORT.append(["Android version", ANDROID_VER])
    # except:
    #     pass

    logfunc(ANDROID_VER)
    activeAccount = ANDROID_VER
    file_found = "kush/home"
    # file_found = str(files_found[0])
    # xmlTree = ET.parse(file_found)
    # root = xmlTree.getroot()
    # for child in root:
    #     if child.attrib['name'] == "active-account":
    #         logfunc("Active gmail account found: " + child.text)
    #         activeAccount = child.text

    if activeAccount != '':
        report = ArtifactHtmlReport('Gmail - Active')
        report.start_artifact_report(report_folder, 'Gmail - Active')
        report.add_script()
        data_headers = ('Active Gmail Address',) # final , needed for table formatting
        data_list = []
        data_list.append((activeAccount, ''))# We only expect one active account
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()
            
        tsvname = f'Gmail - Active'
        tsv(report_folder, data_headers, data_list, tsvname)
    else:
        logfunc('No active Gmail account found')