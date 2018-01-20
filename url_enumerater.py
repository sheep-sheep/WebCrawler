import getpass
import urllib
from urllib import request
from urllib.request import Request
import concurrent.futures
from datetime import datetime
from functools import wraps


url = 'http://www.xiuren.org/xiuren/XiuRen-N00{episode}/{imgnum}.jpg'

episodes = ['{0:0=2d}'.format(n) for n in range(553, 600)]
imgnums = ['{0:0=4d}'.format(n) for n in range(1, 100)]
username = getpass.getuser()
path = 'C:\\Users\\%s\\Downloads\\Images\\'%username



def timeit(func):

    @wraps(func)
    def timed(*args, **kwargs):
        startTime = datetime.now()
        res = func(*args, **kwargs)
        endTime = datetime.now()
        print('%r EpiSode %r with %s images took %2.2f sec' % (func.__name__, args, res, (endTime - startTime).total_seconds()))
        return res

    return timed

@timeit
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
    return imgnum


@timeit
def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        res = executor.map(getImages, episodes)
        list(res)


if __name__ == '__main__':
    main()
