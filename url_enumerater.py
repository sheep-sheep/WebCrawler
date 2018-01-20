import getpass
import urllib
from urllib import request
from urllib.request import urlretrieve, Request
import concurrent.futures

url = 'http://www.xiuren.org/xiuren/XiuRen-N00{episode}/{imgnum}.jpg'

episodes = ['{0:0=2d}'.format(n) for n in range(630, 650)]
imgnums = ['{0:0=4d}'.format(n) for n in range(1, 70)]
username = getpass.getuser()
path = 'C:\\Users\\%s\\Downloads\\Images\\'%username


#TODO: add a timeit decorator

def getImages(episode):
    n = 1
    for imgnum in imgnums:
        req = Request(url.format(episode=episode, imgnum=imgnum), headers={'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'})
        try:
            r = urllib.request.urlopen(req)
            if n%20==0:
                print('checking %s'%req.full_url)
            response = urllib.request.urlopen(req)
            the_page = response.read()
            n += 1
            with open(path + '_'.join(req.full_url.split('/')[-2:]), 'wb') as f:
                f.write(the_page)
        except urllib.error.HTTPError as e:
            break
    return 'Episode %s ends at %s' % (episode, imgnum)


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        res = executor.map(getImages, episodes)
        for sentence in res:
            print(sentence)


if __name__ == '__main__':
    main()
