# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:34:32 2020

@author: Fabian
"""


import requests
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")
data = b""

    
    
r = requests.post("http://www.flyland.ch/fl_php/fl_php_Downloader.php?case=4001", data = {
  'cbGG': '1',
  'cbSZ': '0',
  'cbBB': '1',
  'cbHI': '0',
  'cbAWY': '1',
  'cbCTR': '1',
  'cbCTA': '1',
  'cbTMA': '1',
  'cbD': '1',
  'cbR': '1',
  'cbFIR': '1',
  'cbFIZ': '1',
  'cbTSA': '1',
  'cbFLF': '1',
  'cbHPO': '1',
  'cbVZ': '1',
  'cbAIRSPACE': '0',
  'cbHI-CABLE': '1',
  'cbHI-CABLE_CRANE': '1',
  'cbHI-CABLE_RAILWAY': '1',
  'cbHI-ROPEWAY_CABLE': '1',
  'cbHI-AERIAL_RAILWAY': '1',
  'cbHI-POWER_LINE': '1',
  'cbHI-SKI_LIFT': '1',
  'cbHI-CHAIR_LIFT': '1',
  'cbHI-SUSPENSION_BRIDGE': '1',
  'cbHI-TELEPHONE_LINE': '1',
  'cbHI-USER_DEFINED': '0',
  'AltType': '0',
  'cbAkzeptieren': 'on'
})
data += r.content

with open('./raw/Schweiz_%s.txt' % timestr, "wb") as f:
    f.write(data)
    
    
