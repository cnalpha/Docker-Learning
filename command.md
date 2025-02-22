# Docker 筆記

## 1. 基本指令

### 拉取鏡像
```
docker pull alpine:latest
```

### 查看本地所有鏡像
```
docker images
```

### 執行容器
```
docker run alpine echo "Hello Docker"
docker run alpine df
docker run alpine ls /
```

### 進入交互式 Shell
```
docker run alpine /bin/sh
```

### 以交互模式運行容器
```
docker run -it alpine /bin/sh
```

### 以後台模式運行交互式容器
```
docker run -d -it alpine /bin/sh
```

## 2. 容器管理

### 查看運行中的容器
```
docker container ls 或叫 docker ps 
```

### 停止容器
```
docker container stop <container_id>
```

### 查看所有容器（包括已停止的）
```
docker container ls -a
```

### 刪除容器
```
docker container rm <container_id>
```

## 3. 鏡像管理

### 查看所有鏡像
```
docker images
```

### 刪除鏡像
```
docker rmi <image_id>
```

## 4. 建立自訂鏡像

### 撰寫 Dockerfile
```Dockerfile
FROM alpine:latest
ENTRYPOINT ["httpd", "-D", "FOREGROUND"]
```

### 建立鏡像
```
docker build -t cnimage .
```

### 執行自訂鏡像並映射端口
```
docker run -d -p 81:80 cnimage
```
### 成果展示
![建立image](Pic1.png)
## 5. Docker Hub 操作

### 登入/登出 Docker Hub
```
docker logout
docker login
```

### 推送鏡像到 Docker Hub
```
docker build -t cnmichael/cnimage .
docker push cnmichael/cnimage
```

### 成果展示
![推送至Docker Hub](Pic2.png)


