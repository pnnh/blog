---
cls: MTNote
uid: 01955eec-d1f6-757f-8afc-cbff95f39990
image: cover.png
---

```bash
# 构建镜像
docker build -t custom-mysql -f Dockerfile .
# 执行容器
docker run -p 3306:3306 --name custom-mysql -d custom-mysql:latest
```