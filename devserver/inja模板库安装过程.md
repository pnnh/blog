安装过程

```bash
git clone https://github.com/pantor/inja.git
cd inja
git checkout v3.4.0  # 安装指定版本
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/opt ..  # 安装到/opt目录
sudo make install
```