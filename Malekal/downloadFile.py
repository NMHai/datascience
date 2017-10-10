# Author: NMHai
# Desription: download the file from URL
# https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests

#!/usr/bin/python
import requests
from StringIO import StringIO
from PIL import Image
import profile
import wget

def testRequest():
    image_name = 'test1.jpg'
    url = 'http://example.com/image.jpg'

    r = requests.get(url, stream=True)
    with open(image_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

def testRequest2():
    image_name = 'test2.jpg'
    url = 'http://example.com/image.jpg'

    r = requests.get(url)

    i = Image.open(StringIO(r.content))
    i.save(image_name)

def downloadWithWget(url):
    filename = wget.download(url);
    print "\n Finished downloading " + filename;

#def downloadWithWget(url, file):
#    filename = wget.download(url + file);
#    print "\n Finished downloading " + filename;


if __name__ == '__main__':
    # profile.run('testUrllib()')
    # profile.run('testUrllib2()')
    # profile.run('testRequest()')
    url = "http://malwaredb.malekal.com/files/86927f4d92665747679ab72a9be87b05.zip";
    downloadWithWget(url);
    
