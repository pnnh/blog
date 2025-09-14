---
cls: MTNote
uid: 019947fd-8464-746f-9571-e9b1aa2d093c
---



默认Bash支持通过$RANDOM来生成随机数，范围是0-32767。

```bash
echo $RANDOM
```
如果需要更大的范围，可以使用$RANDOM的乘积来生成更大的随机数。

```bash
echo $((RANDOM * RANDOM))
```
如果需要生成一个范围在1到100之间的随机数，可以使用以下命令：

```bash
echo $((RANDOM % 100 + 1))
```
如果需要生成一个范围在1到100之间的随机数，并且不包含1和100，可以使用以下命令：

```bash
echo $((RANDOM % 98 + 2))
```

### 生成指定范围的随机数

假如要生成100到200的随机数可以使用以下命令：

```bash
echo $((RANDOM % 101 + 100))
```
如果要生成100到200之间的随机数，并且不包含100和200，可以使用以下命令：

```bash
echo $((RANDOM % 98 + 102))
```

### 使用awk生成随机数
awk也可以用来生成随机数，范围是0到1之间的浮点数：

```bash
awk 'BEGIN { srand(); print rand() }'
```
awk也可以用来生成指定范围的随机数：

```bash
awk 'BEGIN { srand(); print int(100 + rand() * 101) }'
```

### 使用date生成随机数

date也可以生成随机数，需要和其它命令搭配

```bash
date +%s%N  # 生成19位数
date +%s%N | cut -c6-13 # 取八位数字
date +%s%N | md5sum | head -c 8 # 八位字母和数字的组合
```

生成1到50的随机数

```bash
#!/bin/bash

function rand(){
    min=$1
    max=$(($2- $min + 1))
    num=$(date +%s%N)
    echo $(($num % $max + $min))
}

rnd=$(rand 1 50)
echo $rnd

exit 0
```

### 使用openssl生成随机数
openssl也可以生成随机数，范围是0到255之间的随机数：

```bash
openssl rand -hex 4
```