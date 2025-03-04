---
cls: MTNote
uid: 01955f00-f757-77b5-8332-cad68fe5886d
image: cover.webp
---

```bash

# 查看xcode项目配置
xcodebuild -project target/quantum.xcodeproj -list

# 编译xcode项目
xcodebuild -project target/quantum.xcodeproj -scheme quantum -configuration Release build

# 编译iOS项目
xcodebuild -project target/quantum.xcodeproj -scheme quantum_native -configuration Release -destination generic/platform=iOS build
```
