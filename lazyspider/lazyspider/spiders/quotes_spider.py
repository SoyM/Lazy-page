# -*- coding: utf-8 -*-

# sina weibo
#
#

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            # 'http://s.weibo.com/top/summary?cate=realtimehot',
            'http://127.0.0.1:8000/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'weibo_real_time_hot.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        # for tbody in response.css('tbody'):
        #     yield {
        #         'star_name': tbody.css('tr td.td_02 div.rank_content p.tar_name a::text').extract_first(),
        #     }

        for tbody in response.css('div.am-g'):
            yield {
                'star_name': tbody.css('div.am-u-lg-3 p.detail-p::text').extract_first(),
            }
