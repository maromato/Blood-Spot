import os
import re
import random
import matplotlib.pyplot as plt
import cv2
import numpy as np
import urllib.request
from urllib.parse import quote
import httplib2
import pynder
import time
import random
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import selenium
import cssutils
from bs4 import BeautifulSoup
from selenium.webdriver.common.alert import Alert

#Define the path for webdriver
chro = webdriver.Chrome('/Users/USERNAME/Desktop/chromedriver_win32/chromedriver')

#Go to Blood Spot
chro.get("http://servers.binf.ku.dk/bloodspot/")

#define the list of gene IDs
search=["ADA","IGFBP2","CLIP2","NR4A2", "LHX6", "RUNX1","SMAD1"]

for search_word in search:
        try:
            # Get the element of the BloodSpot's search window 
            search_input=chro.find_element_by_id("gene_input")
            # Erace old keyword (gene id) in the search window
            search_input.clear()
            # Put a new keyward (gene id) in the search window and submit
            search_input.send_keys(search_word)
            print(search_word)
            chro.find_element_by_id("gene_input_button").click()
            # Download the csv file for expression data
            datatxt = chro.find_element_by_id("export_text")
            datatxt.click()  
            
            time.sleep(1)
           
            
        except:
            #Erace the alert window
            print("GENE ID does not exist")
            Alert(chro).accept()
           
