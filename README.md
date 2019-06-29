# bingbot
## 介绍
   一个python scrapy 框架写的爬虫可以实现,同步bing搜索的背景.
## 安装环境
  ```
     pip install -r requirements.txt
  ```
## 运行
```
   scrapy crawl binbot
```

## pyinstaller 打包:
```shell
    pyinstaller --add-data="scrapy\mime.types;scrapy" --add-data="scrapy\VERSION;scrapy" --add-data="scrapy.cfg;." --add-data="bing;bing" --add-data="bb.cmd;." --add-data="install.cmd;." -i bing.ico -c bb.py
```
## 安装自动运行
 右键install.cmd,用管理员权限打开,设置windows计划任务,自动修改壁纸,4小时运行一次.
