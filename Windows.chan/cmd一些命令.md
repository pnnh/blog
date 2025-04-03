---
cls: MTNote
uid: fec54329-e34a-15e9-59bf-c73f9a3b8ec7
---

永久设置环境变量
setx MyVariable HelloWorld

在现有变量基础上附加内容
setx PATH "%PATH%;C:\NewPath" /M

验证修改后是否生效/打印环境变量
echo %PATH%

