---
cls: MTNote
uid: 01955eeb-87fd-743c-896d-6bd7e7932021
image: cover.jpg
---


wt c++ web framework

https://www.webtoolkit.eu/wt/

```bash
cd ~/Library
git clone https://github.com/emweb/wt.git
git checkout 4.10.4
mkdir cmake-build && cd cmake-build
cmake -DCMAKE_INSTALL_PREFIX=/opt ..
make
sudo make install

```