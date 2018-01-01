import requests
from bs4 import BeautifulSoup

url = 'https://www.facebook.com/'

def data(url_get):
    '''pdf file download ; with use of urllib.request
    '''
    source_code = requests.get(url_get)
    source_txt = source_code.text
    source = BeutifulSoup(source_txt)
    
    for lines in source.findAll('a'):
        print(lines + '\n')
        
    

data(url)
print(data.__doc__)
