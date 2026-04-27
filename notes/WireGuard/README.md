
尝试在macOS下配置Wireguard然后为windows电脑提供网络连接服务

场景是macOS通过有线联网，同时通过WiFi和windows链接到同一个局域网
macOS在网络中将有线网卡放到无线网卡前面这样它就会优先有线上网

然后再macOS中部署Wireguard服务器，windows电脑作为客户端连接到macOS的Wireguard服务器上

参考同目录的其它文件

NUC.conf是访问http://192.168.0.49:51821/ （通过浏览器访问输入docker-compose.yml里的密码）创建客户端之后下载的配置文件，windows客户端需要导入以链接

需要注意同时需要处理RDP链接问题，需要正确配置路由表以实现windows链接上Wireguard之后，macOS仍能够通过WiFi局域网地址远程到windows
主要设置是docker-compose.yml里的
- WG_ALLOWED_IPS=0.0.0.0/1,128.0.0.0/1,192.168.0.0/16 # 只代理公网，不走本地
和NUC.conf里的
AllowedIPs = 0.0.0.0/1,128.0.0.0/1,192.168.0.0/16
默认下载的NUC.conf里可能不是这样，需要手动修改之后再导入windows客户端


详细的安装部署对话在notion笔记里记录

https://www.notion.so/Grok-_11-2b0b49fd686e49cea0d1d0d466e0bb61#34f3d63b488d810787a8dcffd56949f3


 
docker run --rm -it ghcr.io/wg-easy/wg-easy wgpw "YVjKE0TIis:lo&syGH$"

PASSWORD_HASH='$2a$12$PRYBwD2POCU1Is4hXK8zY.H6/ucCCX7j8xNPvir9BslFRaQFmIgSK'

在输入docker-compose.yml时，PASSWORD_HASH的值需要加上$$进行转义