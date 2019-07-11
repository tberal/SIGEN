import json
import requests
import datetime

from SIGEN.configs import receituario, entrada, saida

def UpdateFile(data, mtype):
    file = open('../configs/maps.py', 'w')
    
    
    
