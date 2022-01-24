- [How to use](#how-to-use)
- [Assignments](#assignments)
	- [REQ3: SQL CRUD](#req3-sql-crud)
		- [使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料](#使用-insert-指令新增一筆資料到-member-資料表中這筆資料的-username-和-password-欄位必須是-test接著繼續新增至少-4-筆隨意的資料)
		- [使用 SELECT 指令取得所有在 member 資料表中的會員資料](#使用-select-指令取得所有在-member-資料表中的會員資料)
		- [使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序](#使用-select-指令取得所有在-member-資料表中的會員資料並按照-time-欄位由近到遠排序)
		- [使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序](#使用-select-指令取得-member-資料表中第-2--4-共三筆資料並按照-time-欄位由近到遠排序)
		- [使用 SELECT 指令取得欄位 username 是 test 的會員資料](#使用-select-指令取得欄位-username-是-test-的會員資料)
		- [使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料](#使用-select-指令取得欄位-username-是-test且欄位-password-也是-test-的資料)
		- [使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。](#使用-update-指令更新欄位-username-是-test-的會員資料將資料中的-name-欄位改成-test2)
	- [REQ4: SQL Aggregate Functions](#req4-sql-aggregate-functions)
		- [取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )](#取得-member-資料表中總共有幾筆資料--幾位會員-)
		- [取得 member 資料表中，所有會員 follower_count 欄位的總和](#取得-member-資料表中所有會員-follower_count-欄位的總和)
		- [取得 member 資料表中，所有會員 follower_count 欄位的平均數](#取得-member-資料表中所有會員-follower_count-欄位的平均數)
	- [REQ5: SQL JOIN](#req5-sql-join)
		- [在資料庫中，建立新資料表，取名字為 message, 資料表中必須包含以下欄位設定](#在資料庫中建立新資料表取名字為-message-資料表中必須包含以下欄位設定)
		- [使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名](#使用-select-搭配-join-語法取得所有留言結果須包含留言者會員的姓名)
		- [使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。](#使用-select-搭配-join-語法取得-member-資料表中欄位-username-是-test-的所有留言資料中須包含留言者會員的姓名)

# How to use
1.  clone this repo
2.  `mv .env.exampe .env`
3.  edit `.env`
3.  ` docker compose-up `
4.  `mysql -u ${your_user_name} -p website < website.sql`

# Assignments
## REQ3: SQL CRUD

### 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料

-   ![picture 1](images/fc442e1f82a84c576f89538e2e3ed9169911feafa1b20df57acc7fff76e1102c.png)
-   ![picture 2](images/9eb54c7b368359ad9deafa57e9c108de38860f4d44e2ab5386c87325c82e790a.png)

### 使用 SELECT 指令取得所有在 member 資料表中的會員資料

-   ![picture 3](images/f580ab246b453809a36e68fd93766ccbc3f29e7b2b09a9f51bf29278763cf65b.png)

### 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序

-   ![picture 4](images/a750d489248a381517fa6745aad07f7f025daa10f19659c62d4ca525fc96e365.png)

### 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序

-   ![picture 19](images/f1a97df85f79e2870ad8d2d142bb60940f993d51f0e0b85addbf258367710429.png)

### 使用 SELECT 指令取得欄位 username 是 test 的會員資料

-   ![picture 6](images/9f0d3b3c97b450e3fb17490a7c8df00065f2d3386ec1a0b329d9516d48acbb1e.png)

### 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料

-   ![picture 7](images/89968cb994501ea6cf0193f3d677cdbb84d2ffc0275ac459bb7f7e1867e2b9af.png)

### 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

-   ![picture 8](images/c7bd209ccf6fd6dca714b8adf66982d43cececbbaff17ce52d81d123eb4ba016.png)
-   ![picture 9](images/16ec91a7befdc2b34f2a42812849783437595d7d7f26f4df1bfa9ae3b48626f4.png)

## REQ4: SQL Aggregate Functions

### 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )

-   ![picture 10](images/232bbbbf3eac13e225036f0c9b2c8df17bf9ae30da60710aa7e877d497f14616.png)

### 取得 member 資料表中，所有會員 follower_count 欄位的總和

-   ![picture 11](images/63fcad92c1485a4b32a00262b2fc913e32a7be4a0bc0df154284095861478334.png)

### 取得 member 資料表中，所有會員 follower_count 欄位的平均數

-   ![picture 12](images/744fe4adbe340db1af3e52727047a99d125b937a16f300467a523d1032429fbf.png)

## REQ5: SQL JOIN

### 在資料庫中，建立新資料表，取名字為 message, 資料表中必須包含以下欄位設定

-   ![picture 14](images/d9c54e73c4ab0d22a7e6669b1302ffbb479346937566d097bf3849c97c6486d3.png)

-   ![picture 13](images/08f1fc9934742128605ad3aa2aad28f87ead7a1c6e055900f028efdbb8717272.png)

### 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名

-   ![picture 17](images/7e6e32db93056f23e0bd35312c645126713414d6ebe116d006bfa7a1ef7f0949.png)

### 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

-   ![picture 16](images/9247f569391bb0a8853ef7ae21061a27067da1fd5d4494f4295b4d0096784aee.png)
