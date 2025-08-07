---
cls: MTNote
uid: 0197ab10-ac6d-74fb-99d6-0b048793be72
---

永久设置环境变量
setx MyVariable HelloWorld

在现有变量基础上附加内容
setx PATH "%PATH%;C:\NewPath" /M

验证修改后是否生效/打印环境变量
echo %PATH%

