---
cls: MTNote
uid: 01955efd-b994-748b-a3f3-2964390d6ca9
image: cover.jpg
---

Git常用命令列表

### 基本操作

```shell
# 克隆代码库
git clone git@github.com:pnnh/ebase58shared.git

# 克隆代码库到指定目录
git clone git@github.com:pnnh/ebase58shared.git ebase58shared

# 查看当前状态
git status

# 查看本地变更
git diff --cached

```

### 子模块

```shell
# 添加子模块
git submodule add git@github.com:pnnh/ebase58shared.git pnnh/ebase58shared

# 查看子模块状态
git submodule status

# 递归同步子模块
git submodule sync —recursive 

# 递归初始化子模块
git submodule update --init —recursive
```

移除Git子模块的步骤

```shell
# 移除.git/config配置文件中的子模块配置
git submodule deinit -f path/to/submodule

# 移除.git/modules下的子模块目录
rm -rf .git/modules/path/to/submodule

# 移除.gitmodules文件中的子模块配置，并移除path/to/submodule目录
git rm -f path/to/submodule
```

### 特殊操作

```shell
# 获取当前分支的修订版本号
git rev-parse HEAD

# 强制撤销本地修改
git reset --hard
```

### 推送命令

```bash
# 仅推送所有标签
git push origin --tags

# 推送代码同时推送标签
git push --follow-tags
```