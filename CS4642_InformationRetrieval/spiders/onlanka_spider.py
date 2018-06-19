import scrapy


class OnlankaSpider(scrapy.Spider):
    name = "onlanka"

    start_urls = [
        'https://www.onlanka.com/'
    ]

    def parse(self, response):
        for news_item in response.css('div.post.type-post'):
            yield {
                'title': news_item.css('a::attr(title)').extract_first(),
                'content': news_item.css('div.post-content p::text').extract(),
                'link': news_item.css('div.read-more a::attr(href)').extract_first(),
                'date_published': news_item.css('span.published::text').extract_first(),
                'category': news_item.css('div.post-category a::text').extract_first()
            }

        next_page = response.css('div.previous a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
