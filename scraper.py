import scrapy
import getpass
import random
from urllib.request import urlretrieve



class ImageSpider(scrapy.Spider):
    name = "image_spider"
    start_urls = ['https://gravuresidol.com/zhao-wei-yi-03/']
    username = getpass.getuser()
    path = 'C:\\Users\\%s\\Downloads\\Images\\'%username
    visited = set()
    def parse(self, response):
        TITLE_SELECTOR = '.entry-title'
        if response.url in self.visited:
            return
        self.visited.add(response.url)
        for title in response.css(TITLE_SELECTOR):
            post_name = title.css('h1 ::text').extract()

        GALLERY_SELECTOR = '.justified-gallery'
        gallery = response.css(GALLERY_SELECTOR)
        tmp = []
        for image_url in gallery.css('img ::attr(src)').extract():
            tmp.append(image_url.replace('.jpg', '_b.jpg'))

        yield {'Title': post_name,
               'Image': tmp}

        for idx,url in enumerate(tmp):
            urlretrieve(url, self.path + "%s_%s.jpg"%(post_name[0].split(' ')[2]+post_name[0].split(' ')[3]+random.choice('abcdefghijklmnokpqrst'), idx))

        NEXT_PAGE_SELECTOR = '.wpp-post-title'
        next_page = response.css(NEXT_PAGE_SELECTOR)
        if next_page:

            for page in next_page.css('a ::attr(href)').extract():
                for i in range(1, 9):
                    try:
                        print(page[:-2] + str(i)+'/')
                        yield scrapy.Request(
                            response.urljoin(page[:-2] + str(i)+'/'),
                            callback=self.parse
                        )
                    except Exception:
                        yield {'error': page}