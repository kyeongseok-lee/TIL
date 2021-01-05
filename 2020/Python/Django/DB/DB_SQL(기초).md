# DB

### 데이터베이스(Database, DB)

- `데이터베이스`는 여러 사람이 공유하여 사용할 목적으로 체계화해 통합, 관리하는 <strong>데이터</strong>의 <strong>집합</strong>이다.



### DBMS

- `데이터베이스(DB)`를 관리하는 시스템
- 계층형 데이터베이스, 관계형 데이터베이스, 객체지향 데이터베이스 등 존재
- <strong>RDBMS</strong>
  - 가장 많이 활용하는 `DBMS`
  - 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템
  - `MySQL`, `SQLite` , `ORACLE` 등이 있다.



### 관계형 데이터베이스

- 관계형 데이터베이스는 관계를 열과 행으로 이루어진 <strong>테이블</strong> 집합으로 구성
- 각 열을 특정 종류의 데이터를 기록
- 테이블의 행은 각 객체/엔터티와 관련된 값의 모음



### 기본 용어

- <strong>스키마</strong>
  - 데이터베이스에서 자료의 구조와 제약 조건

- <strong>테이블(관계)</strong>

  - 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

- <strong>Column(열), 속성</strong>

  - 각 열에는 고유한 데이터 형식이 있다.
  - ex) `name`, `age`, `phone`, `email` 등

- <strong>Row(행), 레코드</strong>

  - 테이블의 데이터는 행으로 저장된다.

- <strong>PK(Primary Key / 기본키)</strong>

  - 각 행의 고유값으로 저장된 레코드를 고유하게 식별할 수 있는 값
  - ex) `학번`, `주민등록번호`, `군번`과 같이 고유한 값으로 생각하면 된다.



<hr>

### SQL

- `Structured Query Language`

- `RDBMS`의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

- `RDBMS`에서 자료의 검색과 관리, 데이터베이스 스키마 생성과 수정, 데이터베이스 접근 관리 등을 위해 고안됨.

- 데이터베이스 시스템에서 어떠한 작업을 하기 위해 질문을 던지기 위한 프로그래밍 언어라고 생각하면 된다.

  

#### 기본 데이터베이스 활용법

- SQLite3 생성/접근
  - `sqlite3 <filename>`
- 테이블 목록 조회
  - `.tables`
- 특정 테이블 스키마 조회
  - `.schema <table>`



#### 기본구조

```sqlite
# ex) SELECT문

SELECT * FROM(키워드) articles_article;
```

- `SELECT`문은 데이터를 읽어올 수 있으며, 특정한 `테이블`을 반환한다.
  - `SELECT` * `FROM` 테이블



#### 테이블 생성

```sqlite
CREATE TABLE table(
	column1 datatype [constraints],
    column2 datatype [constraints],
);

# constraints => PRIMARY KEY, NOT NULL, UNIQUE, DEFAULT 등
```

- <strong>Ex</strong>

  ```sqlite
  CREATE TABLE classmates(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL
      age INTEGER,
      address TEXT
  );
  ```

- <strong>Datatype(SQLite)</strong>

  ![Datatype(SQLite)](Datatype(SQLite).JPG)



#### 추가 

- `INSERT INTO table (column1, ''') VALUES (value1, ''');`

- 특정 테이블에 새로운 행을 추가하여 데이터를 추가

  ```sqlite
  INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
  ```

- 모든 열에 데이터를 넣을 때에는 `column`을 명시할 필요가 없음

  ```sqlite
  INSERT INTO classmates VALUES (2, '홍길동', '30', '서울');
  ```



#### 읽기

- 특정 테이블에 특정 레코드를 조회

  ```sqlite
  SELECT * FROM table WHERE condition;
  ```

- 특정 테이블에 특정 레코드의 특정 `column` 조회

  ```sqlite
  SELECT column1, '' FROM table WHERE condition;
  ```

- 중복 없이 가져오기

  ```sqlite
  SELECT DISTINCT column FROM table;
  ```

- 특정 테이블에 특정 레코드의 개수

  ```sqlite
  SELECT COUNT(column) FROM table;
  ```

- 최대, 최소, 평균

  ```sqlite
  SELECT MAX(column) FROM table;
  SELECT MIN(column) FROM table;
  SELECT AVG(column) FROM table;
  ```





#### 삭제

- 특정 테이블에 특정 레코드를 삭제

  ```sqlite
  DELETE FROM table WHERE condition;
  ```

  ```sqlite
  DELETE FROM classmates WHERE id=4;
  ```



#### 수정

- 특정 테이블에 특정 레코드를 수정

  ```sqlite
  UPDATE table SET column1=value1, '' WHERE condition;
  ```

  ```sqlite
  UPDATE table SET name='홍길동', address='제주' WHERE id=4;
  ```



#### WHERE

- AND, OR

- LIKE

  ```sqlite
  SELECT * FROM classmates WHERE phone LIKE '010-%';
  
  # 010- 으로 시작하는 phone 선택
  ```

  와일드 카드

  - % : 문자열이 있을 수도 있다.
  - _ : 반드시 한 개의 문자가 있다.

  ![LIKE(와일드카드)](LIKE(와일드카드).JPG)



#### ORDER

- 특정 column을 기준으로 정렬

  ```sqlite
  SELECT columns FROM table ORDER BY column1, column2 ASC|DESC;
  ```

  - ASC(default) : 오름차순

  - DESC : 내림차순

    ```sqlite
    SELECT * FROM classmates ORDER BY age ASC name DESC;
    
    # 나이를 기준으로 오름차순으로 정렬하되, 나이가 같으면 이름으로 내림차순으로 정렬한다.
    ```



#### LIMIT

- 특정 table에서 원하는 개수만큼 가져오기

  ```sqlite
  SELECT name FROM classmates LIMIT 10;
  
  # 열개만 가져오기
  ```

  ```sqlite
  SELECT name FROM classmates LIMIT 1 OFFSET 2;
  
  # 3번째 있는 사람
  ```



#### GROUP

- 특정 컬럼을 기준으로 그룹화 하기

  ```sqlite
  SELECT sex, COUNT(name) FROM classmates GROUP BY sex;
  
  # 성별로 그룹화한다.
  남 : 30
  여 : 35
  이런식으로 나온다.
  ```





