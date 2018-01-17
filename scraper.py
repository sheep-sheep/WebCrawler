import scrapy
import random

class ImageSpider(scrapy.Spider):
    name = "image_spider"
    start_urls = ['https://gravuresidol.com/liu-you-qi-05/']

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
        # # yield res
        #
        # NEXT_PAGE_SELECTOR = '.wpp-thumbnail wpp_featured_stock wp-post-image a ::attr(href)'
        # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         callback=self.parse
        #     )