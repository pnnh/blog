---
cls: MTNote
uid: 01955f22-f396-77b9-85ea-2d8d5866f761
---

命令列表如下：

```powershell
# 输入以下命令查看已安装的 WSL 发行版列表以及默认发行版
wsl -l -v

# 删除发行版
wsl --unregister Ubuntu

# 设置默认发行版：
wsl --set-default Ubuntu-18.04

# 关闭 WSL
wsl --terminate Ubuntu-18.04

# 关闭所有 WSL 发行版
wsl --shutdown

# 启动 WSL
wsl

```

