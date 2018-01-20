import getpass
import urllib
from urllib import request
from urllib.request import urlretrieve

url = ''

episodes = ['{0:0=2d}'.format(n) for n in range(623, 650)]
imgnums = ['{0:0=4d}'.format(n) for n in range(1, 70)]
username = getpass.getuser()
path = 'C:\\Users\\%s\\Downloads\\Images\\'%username

for episode in episodes:
    for imgnum in imgnums:
        target = url.format(episode=episode, imgnum=imgnum)
        try:
            r = urllib.request.urlopen(target)
            print('checking %s'%target)
            urlretrieve(target, path + '_'.join(target.split('/')[-2:]))
        except urllib.error.HTTPError as e:
            print('Episode %s ends at %s' % (episode, imgnum))
            break
