---
cls: MTNote
uid: 01990491-2db4-771f-bee3-83f063ef6ca7
lang: zh
---


在 macOS 中为 GUI 程序设置环境变量需通过系统级配置实现，以下为具体步骤及注意事项：


### 用户级永久配置

‌创建 environment.plist 文件‌
在 ~/Library/LaunchAgents/ 目录下新建名为 environment.plist 的 XML 文件，内容如下：

xml
Copy Code
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>user.environment</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/launchctl</string>
        <string>setenv</string>
        <string>VARIABLE_NAME</string>
        <string>VARIABLE_VALUE</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
替换 VARIABLE_NAME 和 VARIABLE_VALUE 为实际变量名和值，如需多个变量，需创建多个 <string> 元素56。

‌加载配置文件‌
终端执行以下命令使配置生效：

```bash
launchctl load ~/Library/LaunchAgents/environment.plist
```

重启 GUI 程序或系统后环境变量生效15
