# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from . import  settings
from scrapy.pipelines.images import ImagesPipeline
import win32file, win32api,win32gui
from PIL import Image
import win32con

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO


class BingPipeline(ImagesPipeline):
    def get_media_requests(self, item, spider):
        print('=======================================================================================================')
        print(item['imgurl'])
        print('=======================================================================================================')
        yield Request(item['imgurl'], callback=self.set_wall)

    def set_wall(self, response):
        baseroot = settings.IMAGES_STORE
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
        # 2拉伸适应桌面,0桌面居中
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,baseroot + response['path'], 1 + 2)
        print(response['path'])

    def file_path(self, request, response=None, info=None):
        return 'bg/bg.bmp'

    def convert_image(self, image, size=None):
        if image.format == 'PNG' and image.mode == 'RGBA':
            background = Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode == 'P':
            image = image.convert("RGBA")
            background = Image.new('RGBA', image.size, (255, 255, 255))
            background.paste(image, image)
            image = background.convert('RGB')
        elif image.mode != 'RGB':
            image = image.convert('RGB')

        if size:
            image = image.copy()
            image.thumbnail(size, Image.ANTIALIAS)

        buf = BytesIO()
        image.save(buf, 'bmp')
        return image, buf
