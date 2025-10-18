---
cls: MTNote
uid: 01955eea-bd1d-74ad-9ede-9f14538bb42e
image: cover.webp
---

安装过程

```bash
cd ~/Library
git clone https://github.com/HowardHinnant/date.git
cd date
git checkout v3.0.1
mkdir _build && cd _build
cmake -GNinja -DCMAKE_INSTALL_PREFIX=/opt -DBUILD_TZ_LIB=ON -DBUILD_SHARED_LIBS=ON ..
ninja
sudo ninja install
```