当设置完.gitattributes文件后，Git会自动处理新添加的文件。但是对于旧的已经提交到Git仓库的文件不会自动转换为LFS存储。要将现有的文件迁移到Git LFS，可以使用以下命令：

```bash
cd blog

# Remove all files from index (won't delete working directory files)
git rm --cached -r .

# Re-checkout everything (now applying current .gitattributes)
git reset --hard

# Re-add everything → files matching LFS rules become pointers
git add --renormalize .

git commit -m "Convert existing image files to proper Git LFS pointers"

git push origin main
```