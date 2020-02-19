# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:31:33 2020

@author: Fabian
"""


import glob
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
read_files = glob.glob("./raw/*.txt")
with open("AirspaceCombined_%s.txt" % timestr , "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())