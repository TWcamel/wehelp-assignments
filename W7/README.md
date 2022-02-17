- [宗旨](#宗旨)
	- [About](#about)
		- [TODOs](#todos)
	- [How to use](#how-to-use)
		- [Dependencies](#dependencies)
	- [Ref](#ref)
	- [搞死人的 flask-mysql with docker](#搞死人的-flask-mysql-with-docker)

<hr>

# 宗旨

## About

-   使用 Docker 開發，並支援 hot reload，
-   請看 [這裡](#how-to-use) 來使用 containerized docker application
-   開發方式採用前後端分離
-   會員驗證方式使用 session


### TODOs

-   [ ] mysql with replicaset
-   [x] understand event loop
-   [x] async await with asyncio
-   [x] mysql with connection pool
-   [x] backend
-   [x] frontend page

## How to use

1.  clone this project
2.  `cd W7`
3.  `mv client ./server` ( suffer COPY constrains in Docker )
4.  edit `./server/db/db.example.py` and `./env.example` and set environment variables
5.  make sure your local machine has [dependencies](#dependencies)
6.  `make start`

### Dependencies

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker-compose](https://docs.docker.com/compose/)
-   [Watchman](https://facebook.github.io/watchman/docs/install.html)

## Ref

1.  Flask hot reload: [ref](https://medium.com/hootsuite-engineering/hot-reloading-on-a-dockerized-flask-app-4e87b88ea303)
2.  Node with react app: [ref](https://xiaolishen.medium.com/develop-in-docker-a-node-backend-and-a-react-front-end-talking-to-each-other-5c522156f634)

## 搞死人的 flask-mysql with docker

-   遇到問題: `Can't connect to MySQL server on '172.17.0.3' ( 111 )`
-   [解法](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/docker-mysql-more-topics.html) : `ENV MYSQL_ROOT_HOST=%`
