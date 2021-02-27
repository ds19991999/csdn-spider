# 原创
：  Pycharm安装与汉化

# Pycharm安装与汉化

`一、Ubuntu 16.04  安装 PyCharm`

`通过第三方源安装PyCharm，好处是升级方便。<br/> 添加源：sudo add-apt-repository ppa:mystic-mirage/pycharm<br/> 安装收费的专业版：sudo apt update；sudo apt install pycharm`

`安装免费的社区版：sudo apt update；sudo apt install pycharm-community`

`卸载：sudo apt remove pycharm pycharm-community &amp;&amp; sudo apt autoremove<br/><br/>**二、汉化**<br/> 参考：[Ubuntu 16.04 安装 PyCharm－Python IDE – WTF Daily Blog](http://blog.topspeedsnail.com/archives/6723)`

汉化包：[https://github.com/pingfangx/TranslatorX](https://github.com/pingfangx/TranslatorX) ，拿走不谢

cd /tmp git clone https://github.com/ewen0930/PyCharm-Chinese cd Pycharm-Chinese bash package.cmd (若找不到jar命令，需安装配置java环境，ubuntu为apt install default-jdk) sudo cp resources_zh.jar /usr/lib/pycharm-community/lib

重启 pycharm 生效
