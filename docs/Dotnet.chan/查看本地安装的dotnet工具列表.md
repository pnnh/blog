---
cls: MTNote
uid: 01955eed-6632-75bc-8726-0551107a7c29
image: cover.png
---



```bash
# 查看本地安装的dotnet工具列表
dotnet tool list
# 查看全局安装的dotnet工具列表
dotnet tool list --global

# 安装dotnet工具
dotnet tool install dotnet-outdated-tool --global -a arm64   # 全局安装arm64版本，mac m1芯片下需要

# 卸载全局安装的dotnet工具
dotnet tool uninstall dotnet-ef --global

```