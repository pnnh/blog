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

```
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -yq install mysql-server && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /data

RUN echo "DELETE FROM mysql.user WHERE user = 'root' AND host = '%';" > init-file.sql
RUN echo "CREATE USER 'root'@'%' IDENTIFIED BY '1234';" >> init-file.sql
RUN echo "GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION;" >> init-file.sql
RUN echo "FLUSH PRIVILEGES;" >> init-file.sql

EXPOSE 3306

ENTRYPOINT ["mysqld", "--bind-address", "0.0.0.0", "--init-file", "/data/init-file.sql"]

```