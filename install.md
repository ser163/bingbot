# install

schtasks /create /sc minute /mo 240 /tn "Bing Bot Wallpaper" /tr %~dp0bb.cmd&&pause

