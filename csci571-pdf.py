import base64
import requests
import urllib2
from bs4 import BeautifulSoup
import re
import os
newpath = os.getcwd()+'\\csci571_lecture'
if not os.path.exists(newpath):
    os.makedirs(newpath)
USERNAME = 'csci571' # put correct usename here
PASSWORD = 'notes1' # put correct password here
url ="http://cs-server.usc.edu:45678/slides/"
base64string = base64.encodestring('%s:%s' % (USERNAME, PASSWORD)).replace('\n', '')
r = requests.get(url, auth=(USERNAME, PASSWORD))
soup = BeautifulSoup(r.text)
pdf_link =soup.findAll(name='a',attrs={'href':re.compile("pdf$")})
for download_link in pdf_link:
    link = url+download_link["href"]
    print link
    request = urllib2.Request(link)
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    file = open(newpath+"\\"+download_link["href"], 'wb')
    file.write(result.read())
