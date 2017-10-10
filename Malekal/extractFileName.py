# Author: NMHai
# Version: 1
# Description: Download the HTML page. Then parse the content and extract the file name
# https://stackoverflow.com/questions/3949744/python-http-download-page-source
# https://stackoverflow.com/questions/9222106/how-to-extract-information-between-two-unique-words-in-a-large-text-file

import urllib2
import re

def downloadHTML(url):
    page =urllib2.urlopen(url)
    data=page.read()
    return data

def parseHTML(content):
    data = re.findall(r'file=(.*?)\"', content)
    return data

if __name__ == "__main__":
    url = "http://malwaredb.malekal.com/index.php?page=2"
    data = downloadHTML(url)
    print data
    files = parseHTML(data)
    print ("Parse data: ", files)