---
cls: MTNote
uid: 0197ab0e-d7f1-76a2-a765-a361fe05d2d7
---


首先进入VS开发者命令提示工具


开始菜单进入：Developer Command Prompt for VS 2022


dumpbin /EXPORTS path\to\your\dll\my_library.dll 
结果将打印到控制台

或者
dumpbin /EXPORTS path\to\your\dll\my_library.dll > exports.txt

生成的结果在exports.txt文件里
