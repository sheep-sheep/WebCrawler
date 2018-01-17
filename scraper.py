import scrapy
import getpass
from urllib.request import urlretrieve



class ImageSpider(scrapy.Spider):
    name = "image_spider"
    start_urls = ['WEBSITE']
    username = getpass.getuser()
    path = 'C:\\Users\\%s\\Downloads\\Images\\'%username

    def parse(self, response):
        TITLE_SELECTOR = '.entry-title'
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
            urlretrieve(url, self.path + "%s_%s.jpg"%(post_name[0].split(' ')[2], idx))

        NEXT_PAGE_SELECTOR = '.wpp-post-title'
        next_page = response.css(NEXT_PAGE_SELECTOR)
        if next_page:
            for page in next_page.css('a ::attr(href)').extract_first():
                yield scrapy.Request(
                    response.urljoin(page),
                    callback=self.parse
                )