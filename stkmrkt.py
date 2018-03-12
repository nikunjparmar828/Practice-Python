from urllib import request
from math import pi 
import requests

def stock_download(csvurl):
	'''arg : string of any url'''
    r = request.urlopen(csvurl)
    csv = r.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    durl = r'Nike.csv'
    fo = open(durl, "w")
    for line in lines:
        fo.write(line + "\n")
    fo.close()

stock_download(str(input(goog_url))) #goog_url is anyfile with .csv extension.