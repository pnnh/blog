---
cls: MTNote
uid: 01955eef-43fc-72a5-b19a-898c1881cb51
image: cover.png
---

首先在```pubspec.yaml```中添加```ffigen```依赖：

```yaml

ffigen:
  output: 'lib/gen/bindings.dart'
  headers:
    entry-points:
      - 'native/quantum_native.h'

```

之后运行ffi生成器命令：

```bash
dart run ffigen 
```

也可以在独立配置文件中配置，如```ffigen.yaml```，然后运行：

```bash
dart run ffigen --config ffigen.yaml
```