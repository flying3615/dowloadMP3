__author__ = 'centling'

import urllib
from bs4 import BeautifulSoup

dir_download = 'E:\project\dowloadMP3\MP3\\'
percentage = 0

def reporthook(block_read,block_size,total_size):
    global percentage
    percentage_new = block_read*block_size*100/total_size
    if percentage!=percentage_new:
        percentage = percentage_new
        print 'Read %d blocks,or %d/100' %(block_read,percentage);

def rename_download(url,name):
    print "download %s %s"%(url,name)
    urllib.urlretrieve(url, name,reporthook)


# for i in range(1,10):
#     url = 'http://www.lizhi.fm/57252/p/%s.html'%i
#     wp = urllib.urlopen(url)
#     content = wp.read()
#     soup = BeautifulSoup(content, 'html.parser')
#     for link in soup.find_all('a'):
#         if link.get('data-url'):
#             title = link.get('data-url')
#             download_url = link.get('data-url')
#             rename_download(download_url,title+'.mp3')
if __name__ == "__main__":
    for i in range(1,10):
        url = 'http://www.lizhi.fm/57252/p/%s.html'%i
        wp = urllib.urlopen(url)
        content = wp.read()
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('data-url'):
                title = link.get('title')
                download_url = link.get('data-url')
                rename_download(download_url,dir_download+title+'.mp3')