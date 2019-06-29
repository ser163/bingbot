# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
import platform
from . import settings
from scrapy.pipelines.images import ImagesPipeline

if platform.system() == 'Windows':
    import win32file, win32api, win32gui
from PIL import Image
import win32con
import hashlib

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

from scrapy.utils.python import to_bytes


class BingPipeline(ImagesPipeline):
    def get_media_requests(self, item, spider):
        print('=======================================================================================================')
        print(item['imgurl'])
        print('=======================================================================================================')
        yield Request(item['imgurl'], callback=self.set_wall)

    def set_wall(self, response):
        baseroot = settings.IMAGES_STORE
        fullpath = baseroot + '/' + response['path']
        os_type = platform.system()
        if os_type == 'Windows':
            self.os_win(fullpath)
        else:
            pass

    def os_win(self, path):
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
        # 2拉伸适应桌面,0桌面居中
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1 + 2)

    def file_path(self, request, response=None, info=None):
        # start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        # end of deprecation warning block

        image_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        return 'bg/%s.bmp' % (image_guid)

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
