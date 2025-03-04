---
cls: MTNote
uid: 01955f22-57a6-774c-b3bf-045f437efb5b
image: cover.webp
---


wsl --export Ubuntu-20.04 f:\wsl2\ubuntu20.04.tar

wsl --unregister Ubuntu-20.04

wsl --import Ubuntu-20.04 f:\wsl2\ubuntu20.04 f:\wsl2\ubuntu20.04.tar --version 2

ubuntu2004 config --default-user larry

del f:\wsl2\ubuntu20.04.tar