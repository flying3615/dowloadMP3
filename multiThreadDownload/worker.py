import threading
import urllib
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('gbk')



root_dir='E:\project\dowloadMP3\MP3\\'
url_prefix = 'http://www.lizhi.fm/17248/p'
page = 7


target={}
percentage = 0
def reporthook(block_read,block_size,total_size):
    global percentage
    percentage_new = block_read*block_size*100/total_size
    if percentage!=percentage_new:
        percentage = percentage_new
        print 'Read %d blocks,or %d/100' %(block_read,percentage);

def rename_download(dic):
    for name,url in dic.items():
        print "download %s %s"%(url,name.encode('gbk','ignore'))
        urllib.urlretrieve(url, root_dir+name+".mp3",reporthook)


for i in range(1,page+1):
    url = url_prefix+'/%s.html'%i
    wp = urllib.urlopen(url)
    content = wp.read()
    soup = BeautifulSoup(content, 'html.parser')
    for link in soup.find_all('a'):
        if link.get('data-url'):
            title = link.get('title')
            download_url = link.get('data-url')
            target[title] = download_url


rest = len(target)%10
size = len(target)/10
keys = target.keys()

print "rest %s size %s"%(rest,size)


threads = []
for batch_count in range(1,size+1):
    batch = {}
    print '-'*40
    for k in range((batch_count-1)*10,batch_count*10):
        targetKey = keys[k]
        targetValue = target.pop(keys[k])
        batch[targetKey] = targetValue
        print "ke=%s | value=%s"%(targetKey.encode('gbk','ignore'),targetValue)
    print "start to down load batch %s"%batch_count
    t = threading.Thread(target=rename_download,args=(batch,))
    threads.append(t)
t = threading.Thread(target=rename_download,args=(target,))
threads.append(t)


for t in threads:
    print t
    t.start()
for t in threads:
    t.join()






