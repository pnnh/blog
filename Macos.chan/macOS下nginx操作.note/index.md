---
cls: MTNote
uid: 01955f00-a8b0-72b9-b2d2-9c8df528e3e5
image: cover.webp
---

适用于M1系统

配置文件位于以下路径
```bash
vim /opt/homebrew/etc/nginx/nginx.conf
```

重启nginx服务
```bash
brew services restart nginx
```

查看错误日志

```bash
tail -f /opt/homebrew/var/log/nginx/error.log
```