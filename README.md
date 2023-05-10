# 功能描述

使用docker搭建出三種容器，分別為：RabbitMQ、producer、consumer  
模擬出一個producer對RabbitMQ傳入資料，與多個consumer對RabbitMQ取出資料的過程    

# 使用說明

若想調整consumer的容器數量，可以調整 docker-compose.yml 內 consumer 服務的 deploy replicas 數量

```
git clone 此專案
cd 此專案
docker-compose up -d
```

```
RabbitMQ UI
http://localhost:15672/
```
