# 宗旨

## About

-   開發方式採用前後端分離
-   會員驗證方式使用 session
-   使用 Docker 開發，並支援 hot reload，若第一次 clone 此 project，請看 [這裡](#how-to-use) 來使用 docker container
-   測試影片： [Week4 流程測試 - with Docker (Flask/Nginx/Hot reload) By 黃上科 Samuel](https://youtu.be/eV6get0Nw_M)

## How to use

1.  clone this project
2.  `cd W4`
3.  `mv client ./server` ( suffer COPY constrains in Docker )
4.  make sure your local machine have [dependencies](#dependencies) installed
4.  `make start`

### Dependencies

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker-compose](https://docs.docker.com/compose/)
-   [Watchman](https://facebook.github.io/watchman/docs/install.html)

## Ref

1.  Flask hot reload: [ref](https://medium.com/hootsuite-engineering/hot-reloading-on-a-dockerized-flask-app-4e87b88ea303)
2.  Node with react app: [ref](https://xiaolishen.medium.com/develop-in-docker-a-node-backend-and-a-react-front-end-talking-to-each-other-5c522156f634)
