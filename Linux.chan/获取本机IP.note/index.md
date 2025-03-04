---
cls: MTNote
uid: 01955efe-88b7-74d3-b585-6f6a6bbd226a
image: cover.jpg
---

hostname -I | awk '{print $1}'
export EXTERNAL_IP=$(hostname -I | awk '{print $1}')