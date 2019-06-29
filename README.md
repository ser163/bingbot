# Bing Bot #



Bing Bot 是一个python scrapy 框架写的爬虫程序.可以实现同步bing搜索的背景图片.并且自动设置为Windows桌面的小程序.

* 部署方便.
* 无需配置即可使用.
* 自动化运行,每天自动换桌面
* 文艺气息浓郁,让桌面自动换起来.
## 快速安装 ##

### 运行环境 ###
- Windows 7/10 64bit
- Python 3.6
- Scrapy 1.6.0
- PyInstaller 3.4
### 安装依赖 ###
  ```
  pip install -r requirements.txt
  ```
### 手动运行 ###
 ```
 scrapy crawl binbot
 ```

### 打包 ###
使用pyinstaller 命令在Windows下打包为exe
```
  pyinstaller --add-data="scrapy\mime.types;scrapy" --add-data="scrapy\VERSION;scrapy" --add-data="scrapy.cfg;." --add-data="bing;bing" --add-data="bb.cmd;." --add-data="install.cmd;." -i bing.ico -c bb.py
```

### 安装自动运行 ###
如果你用pyinstaller编译为exe或者直接自动下载了releases版本,在程序目录下.

右键install.cmd,用管理员权限打开,设置windows计划任务,自动修改壁纸,4小时运行一次.

### 常见问题 ###
	* install.cmd 文件必须用管理员权限运行.

## Others ##

* [Bing Bot文档](https://www.ser163.cn/doc/)
* [设置Bing Bot](https://www.ser163.cn/doc/BingBot/startbingbot.html)
* <https://github.com/ser163/bingbot>
* Email: <l3478830@163.com>
* QQ:81212836