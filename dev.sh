#!/bin/bash


# 도커 컨테이너 실행
if [ $1 == 'up' ]; then
  docker-compose up

# 백엔드 컨테이너 접속
elif [ $1 == 'server' ]; then
  container_id=$(docker ps |grep cicd_study-server | awk '{print $1}')
  docker exec -it $container_id /bin/bash

# DB 컨테이너 접속
elif [ $1 == 'db' ]; then
  container_id=$(docker ps |grep mysql:8.0 | awk '{print $1}')
  docker exec -it $container_id /bin/bash

# 도커 컨테이너 삭제 & 볼륨 삭제
elif [ $1 == 'rm' ]; then
  echo "TODO..."
fi