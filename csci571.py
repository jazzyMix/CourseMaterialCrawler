from docx import Document
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import urllib
import re
USERNAME = 'csci571' # put correct usename here
PASSWORD = 'notes1' # put correct password here
url ="http://cs-server.usc.edu:45678/slides/"
session = requests.session()

req_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

formdata = {
    'UserName': USERNAME,
    'Password': PASSWORD,
    'LoginButton' : 'Login'
}
r = requests.get(url, auth=(USERNAME, PASSWORD))

soup = BeautifulSoup(r.text)
pdf_link =soup.findAll(name='a',attrs={'href':re.compile("pdf$")})
out = pdf_link[0]["href"]
for download_link in pdf_link:
    link = url+download_link["href"]
    r = requests.get(url, auth=(USERNAME, PASSWORD))

    urllib.urlretrieve (link, download_link["href"])
