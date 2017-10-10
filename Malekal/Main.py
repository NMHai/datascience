# Author: NMHai
# Version: 1
# Description: The project of downloading the database of the website Malekai.com
import downloadFile
import extractFileName

def normalFileURL(x):
    return "http://malwaredb.malekal.com/files/" + x + ".zip";

if __name__ == '__main__':
    print "Begin";
    webURL = "http://malwaredb.malekal.com";
    numIndex = 1;

    for x in range(0, numIndex):
        url = webURL + "/index.php?page=" + str(x);
        print "Dowload and parse from " + url;
        content = extractFileName.downloadHTML(url)
        fileList = extractFileName.parseHTML(content)
        fileList = map(normalFileURL, fileList)
        map(downloadFile.downloadWithWget, fileList)

    url2 = "http://malwaredb.malekal.com/files/940df2a16d8f5223dcfef58c134d46a0.zip";
    downloadFile.downloadWithWget(url2);
    print "End !"