---
cls: MTNote
uid: 01982606-9b64-70cc-8018-bf12c7cdd60c
cid: 01982606-d238-7016-b655-fe35f389f1eb
lang: zh
---

演示在UNIX环境下，用C语言列出某个目录下的所有文件

### 测试环境

在Ubuntu 24.04环境下测试通过，其它类UNIX环境下应该也可以运行，Windows下理论不支持

### 源码片段

```c
#include <stdio.h>
#include <dirent.h>

int main(int argc, char *argv[]) {
  printf("hello %s\n", "world");

  DIR *dp;
  struct dirent *dirp;

  if (argc != 2) {
    return 1;
  }

  if ((dp = opendir(argv[1])) == NULL) {
    fprintf(stderr, "can't open %s", argv[1]);
    return 2;
  }

  while((dirp = readdir(dp)) != NULL) {
    printf("%s\n", dirp->d_name);
  }

  closedir(dp);
  return 0;
}
```

完整源码地址：[pnnh/apue-listfile](https://github.com/pnnh/apue-listfile.git)

### 源码解释

```dirent.h```是一个POSIX标准提供的头文件，广泛用于Unix-like系统。它主要用于操作目录，包括读取目录内容、遍历目录、获取文件或目录信息等。

调用```opendir```将返回一个```DIR*```，它是一个指向具体目录的不透明指针，后续其它对目录的操作函数需要传递该指针。

调用```readdir```将返回```dirent*```，它指向目录中的一个条目，可能是文件或文件夹，其中包含文件名称。

目录操作完成后，需要调用```closedir```关闭目录以避免资源泄漏。


### 编译

进入源码目录执行以下命令：

```bash
mkdir cmake-build && cd cmake-build
cmake ..
make
```

在构建目录下将生成```ApueListfile```可执行文件

如果编译出错请根据错误信息重复以上编译步骤

### 运行

通过```./ApueListfile <directory>```的方式运行

其中```<directory>```需要是绝对目录，比如执行以下命令列表都可以运行成功

```bash
./ApueListfile /tmp
./ApueListfile /home
./ApueListfile /var
```

**注意：** 当前用户需要有对参数目录的访问权限
