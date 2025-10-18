---
cls: MTNote
uid: 01955eed-a101-73e3-a5ea-cf1853206180
image: cover.jpg
---

# 构建 
dotnet build --configuration Release  
  
# 打包 
dotnet pack --configuration Release -o .packages/ 
  
# 推送
dotnet nuget push ./.packages/Molecule.0.1.2.nupkg  --api-key <your-api-key> --source https://api.nuget.org/v3/index.json 
