# -*- coding: utf-8 -*-
import urllib

import pymysql
import scrapy


class JinyongSpider(scrapy.Spider):
    name = 'jinyong'
    # allowed_domains = ['http://www.jinyongshuwu.com/data/renwu/index.html']
    start_urls = ['http://www.jinyongshuwu.com/data/renwu/index.html']

    def parse(self, response):
        boxes=response.xpath("//div[@class='datapice']")
        db = pymysql.connect(host="39.108.139.175", user="lannister", port=3306, passwd="lannister",
                             db="web_jy", charset='utf8')
        cursor = db.cursor()
        for boxs in boxes:
            boxe=boxs.xpath("./a")
            for box in boxe:

                    print("=="*30)
                    try:
                        img=box.xpath(".//img/@src").get().replace("../../","http://www.jinyongshuwu.com/")
                    except:
                        print("无头像")
                    print(img)
                    name=box.xpath(".//text()").get()
                    print(name)
                    detail=box.xpath(".//@href").get().replace("../","http://www.jinyongshuwu.com/data/")
                    print(detail)
                    print("==" * 30)
                    work_path="picture/"+name+".jpg"
                    urllib.request.urlretrieve(img, work_path)

                    # sql = ''' UPDATE TestModel_persons SET img='''+'"'+img+'"'+'''WHERE name='''+'"'+name+'"'+";"
                    # print(sql)
                    # UPDATE
                    # Websites
                    # SET
                    # alexa = '5000', country = 'USA'
                    # WHERE
                    # name = '菜鸟教程';

                        # 执行sql语句
                    cursor.execute(sql)
                        # 提交到数据库执行
                    db.commit()


