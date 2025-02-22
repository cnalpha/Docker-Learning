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
docker run alpine echo "hey001"
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
docker container ls
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
```bash
docker build -t myimage .
```

### 執行自訂鏡像並映射端口
```bash
docker run -d -p 80:80 myimage
```

### 獲取 Docker 機器 IP
```bash
echo $(docker-machine ip)
```

## 5. Docker Hub 操作

### 登入/登出 Docker Hub
```bash
docker logout
docker login
```

### 推送鏡像到 Docker Hub
```bash
docker build -t uopsdod/myimage .
docker push uopsdod/myimage
```

## 6. 清理資源

### 停止所有容器
```bash
docker container stop $(docker container ls -a -q)
```

### 清除所有無用資源
```bash
docker system prune -y
```

### 刪除所有鏡像
```bash
docker rmi $(docker images -a -q)
```


