---
cls: MTNote
uid: 0f5fd59f-0bc5-b0b5-b298-ca54bf2e76f4
---


安装Hyper-V特性
需要服务器支持虚拟化
Install-WindowsFeature -Name Hyper-V -IncludeManagementTools

安装Windows容器特性
Install-WindowsFeature -Name Containers -IncludeManagementTools

重启计算机
Restart-Computer -Force

启动服务
Start-Service docker 

设置服务启动类型
Set-Service docker -StartupType Automatic

查看系统包的安装源
Get-PackageSource

导入包仓库提供者
Install-Module -Name DockerMsftProvider -Repository PSGallery -Force

查看Powershell Gallery仓库
Get-PSRepository

检查当前安装的版本
Get-Package -Name Docker -ProviderName DockerMsftProvider

搜索模块包
Find-Module -Repository PSGallery -Name "包名关键词"
Find-Package -Name Docker -ProviderName DockerMsftProvider

搜索脚本包
Find-Script -Repository PSGallery -Name "脚本名关键词"

搜索DSC包
Find-DscResource -Repository PSGallery -Name "DSC资源名"

升级包
Install-Package -Name Docker -ProviderName DockerMsftProvider -Update -Force

