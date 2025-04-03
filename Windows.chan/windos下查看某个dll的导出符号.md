---
cls: MTNote
uid: 55857f33-47bb-a345-055e-9d6871cf8cd7
---


首先进入VS开发者命令提示工具


开始菜单进入：Developer Command Prompt for VS 2022


dumpbin /EXPORTS path\to\your\dll\my_library.dll 
结果将打印到控制台

或者
dumpbin /EXPORTS path\to\your\dll\my_library.dll > exports.txt

生成的结果在exports.txt文件里
