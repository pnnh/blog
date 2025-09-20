---
cls: MTNote
uid: 0199667e-dfe8-73ce-9d88-67dbfdd02ae3
---


powershell一些命令

返回上一个命令的执行状态
$?

修改命令提示符
默认只对当前回话有效
function prompt {"PS [$Env:username@$Env:computername] $($PWD.ProviderPath)> "}

解压zip文件到指定路径
Expand-Archive -Path "C:\Files\example.zip" -DestinationPath "C:\Files\Extracted"

以静默方式安装msi安装包
msiexec /i example.msi /quiet

以静默方式安装exe安装包
Start-Process -FilePath "C:\path\to\your\example.exe" -ArgumentList "/silent" -NoNewWindow -Wait

删除文件
Remove-Item -Path "C:\path\to\your\file.txt"

通配符方式删除多个文件
Remove-Item -Path "C:\path\to\your\*.txt"

下载并保存文件
Invoke-WebRequest -Uri https://github.com/vim/gvim_9.1.0_x64_signed.zip -OutFile gvim_9.1.0_x64_signed.zip


创建单个目录
New-Item -Path "C:\path\to\your\directory" -ItemType Directory

递归创建多级目录
New-Item -Path "C:\path\to\your\directory\subdirectory" -ItemType Directory

检查目录是否存在
if (-Not (Test-Path "C:\path\to\your\directory")) {
    New-Item -Path "C:\path\to\your\directory" -ItemType Directory
}

移动文件夹
Move-Item -Path "C:\source\folder" -Destination "C:\destination"

移动文件夹并重命名
Move-Item -Path "C:\source\folder" -Destination "C:\destination\newfoldername"

移动文件夹里的内容而不是文件夹本身
Move-Item -Path "C:\source\folder\*" -Destination "C:\destination"
