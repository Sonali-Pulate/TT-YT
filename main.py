"""
████████╗████████╗          ██╗   ██╗████████╗
╚══██╔══╝╚══██╔══╝          ╚██╗ ██╔╝╚══██╔══╝
   ██║      ██║    ██████╗   ╚████╔╝    ██║   
   ██║      ██║    ╚═════╝    ╚██╔╝     ██║   
   ██║      ██║                ██║      ██║   
   ╚═╝      ╚═╝                ╚═╝      ╚═╝   

By voletro

Downloads a trending TikTok video and uploads it to YouTube. This will happen every half an hour (30 mins).

Requirements:
Firefox - https://www.mozilla.org/en-US/firefox/new/
GeckoDriver - https://github.com/mozilla/geckodriver/releases

Setup:
1. Extract downloaded zip file to a folder. Go to that folder in a terminal.
2. Run "pip install -r requirements.txt" inside the downloaded folder.
3. Sign into YouTube on Firefox with the account you want to upload the videos to.
4. Install the EditThisCookie extension on Firefox, open it, and click the export button to export login cookies to clipboard.
5. Open the file called login.json in a text editor. Paste the exported login cookies into the file and save.
6. Run the main.py script!

Special thanks to these people for making this project possible:
davidteather - TikTokApi - https://github.com/davidteather/TikTok-Api
SeleniumHQ - selenium - https://github.com/SeleniumHQ/selenium
"""


import urllib.request
import logging
from typing import Dict, List
import logging
import re
from datetime import datetime
from time import sleep
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import randint
import os
import subprocess

from upload_video import get_authenticated_service, initialize_upload
from video_downloader import downloader

currentpath = os.getcwd()



def main():
    
    while "n" not in input("Do you want to continue (y/n):"):
        option = input('''
    Choose Option from below :
        1: Testing (Uploading only)
        2: Downloading & Uploading
    : ''')
        if int(option) == 2:  
            youtube = get_authenticated_service()

            for list in downloader(False):
                try:
                    print("Starting upload...")
                    initialize_upload(youtube, dict(
                        file="videos/"+list,
                        privacyStatus="public",
                        category="22",
                        keywords="",
                        description=list.replace(".mp4", ""),
                        title=list.replace(".mp4", "")
                    ))
                    print(list, list.replace(".mp4",""))
                    # os.remove("abc.mp4") #f'{username}-{id}.mp4')
                except:
                    print(231)
                    raise
        elif int(option) == 1: 
            youtube = get_authenticated_service()

            for list in downloader(True):
                try:
                    print("Starting upload...")
                    initialize_upload(youtube, dict(
                        file="videos/"+list,
                        privacyStatus="public",
                        category="22",
                        keywords="",
                        description=list.replace(".mp4", ""),
                        title=list.replace(".mp4", "")
                    ))
                    print(list, list.replace(".mp4",""))
                    # os.remove("abc.mp4") #f'{username}-{id}.mp4')
                except:
                    print(231)
                    raise
        else:
            print("Invalid option, please select")
            
    print("Finished.")
            

os.system('cls' if os.name in ('nt', 'dos') else 'clear')
texttitle = """
████████╗████████╗          ██╗   ██╗████████╗
╚══██╔══╝╚══██╔══╝          ╚██╗ ██╔╝╚══██╔══╝
   ██║      ██║    ███████   ╚████╔╝    ██║   
   ██║      ██║    ╚═════╝    ╚██╔╝     ██║   
   ██║      ██║                ██║      ██║   
   ╚═╝      ╚═╝                ╚═╝      ╚═╝   
"""
print(texttitle)
while True:
    main()
    break