# bingbot
## 介绍
   一个python scrapy 框架写的爬虫可以实现,同步bing搜索的背景.
## 安装环境
  ```
     pip -r requirements.txt
  ```
## 运行
```
   scrapy crawl binbot
```

## pyinstaller 打包为
```shell
    pyinstaller --add-data="scrapy\mime.types;scrapy" --add-data="scrapy\VERSION;scrapy" --add-data="scrapy.cfg;." --add-data="bing;bing" --add-data="bing.ico;." --add-data="bb.cmd;." -i bing.ico -c bb.py
```
## 用管理员权限打开cmd,设置windows计划任务,自动修改壁纸,4小时运行一次.
```
    schtasks /create /sc minute /mo 240 /tn "Bing Bot Wallpaper" /tr X:\bb\bb.cmd
```
/tr后的路径,就是打包后exe程序的路径 ,如: E:\bb\bb.cmd (后缀名是cmd.不是bb.exe)
