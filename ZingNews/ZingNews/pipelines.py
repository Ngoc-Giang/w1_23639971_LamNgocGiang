# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZingnewsPipeline:
    def process_item(self, item, spider):
        return item

import mysql.connector

class MySQLPipeline:
    def open_spider(self, spider):
        """Kết nối MySQL khi spider bắt đầu chạy"""
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root", 
            password="1234", 
            database="lamngocgiang", 
            port = 3307
        )
        self.cursor = self.conn.cursor()
    
    def close_spider(self, spider):
        """Đóng kết nối MySQL khi spider kết thúc"""
        self.conn.close()

    def process_item(self, item, spider):
        """Lưu dữ liệu vào MySQL"""
        self.cursor.execute(
            "INSERT INTO news (Title, Date, Time, Content, Link) VALUES (%s, %s, %s, %s, %s)",
            (item["Title"], item["Date"], item["Time"], item["Content"], item["Link"])
        )
        self.conn.commit()
        return item