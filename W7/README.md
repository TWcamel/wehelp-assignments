- [宗旨](#宗旨)
	- [About](#about)
	- [How to use](#how-to-use)
		- [Dependencies](#dependencies)
		- [TODOs](#todos)
	- [Ref](#ref)
		- [搞死人的 flask-mysql with docker](#搞死人的-flask-mysql-with-docker)

<hr>

# 宗旨

## About

-   使用 Docker 開發，並支援 hot reload，
-   請看 [這裡](#how-to-use) 來使用 containerized docker application
-   開發方式採用前後端分離
-   會員驗證方式使用 session
-   TODO: 測試影片： [Week7 流程測試 - with Docker ( Flask/Nginx/Mysql ) By 黃上科 Samuel]()

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

### TODOs

-   [ ] mysql with [replicaset](#ref)
-   [x] mysql with [connection pool](#ref)
-   [ ] make my API is [CORS able](#ref)

## Ref

1.  Flask hot reload: [ref](https://medium.com/hootsuite-engineering/hot-reloading-on-a-dockerized-flask-app-4e87b88ea303)
2.  Node with react app: [ref](https://xiaolishen.medium.com/develop-in-docker-a-node-backend-and-a-react-front-end-talking-to-each-other-5c522156f634)
3.  MySql connection pooling: [ref-1](https://pynative.com/python-database-connection-pooling-with-mysql/#:~:text=Connection%20pooling%20means%20connections%20are,a%20middle%2Dtier%20server%20environment.)
4.  MySql connection pooling: [ref-2](https://dev.mysql.com/doc/connector-python/en/connector-python-connection-pooling.html)
5.  CORS: [intro by productioncoder](https://www.youtube.com/watch?v=woXBXJgGQvQ)
6.  CORS: [test link](http://www.test-cors.org/)
7.  event loop (JS): [ref](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/EventLoop)
8.  event loop (Python): [ref](https://docs.python.org/3/library/asyncio-eventloop.html#:~:text=The%20event%20loop%20is%20the,asyncio%20functions%2C%20such%20as%20asyncio.)
9.  MySql replicaset: [ref](https://dev.mysql.com/blog-archive/setting-up-mysql-group-replication-with-mysql-docker-images/)


### 搞死人的 flask-mysql with docker

-   遇到問題: `Can't connect to MySQL server on '172.17.0.3' ( 111 )`
-   [解法](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/docker-mysql-more-topics.html) : `ENV MYSQL_ROOT_HOST=%`
