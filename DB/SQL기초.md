# SQL



### SQL (Structured Query Language)

> 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어. RDBMS에서 자료의 검색과 관리, 데이터베이스 스키마 생성과 수정, 데이터베이스 접근 관리 등을 위해 고안됨.



### SELECT

> SELECT문은 데이터를 읽어올 수 있으며, 특정한 테이블을 반환한다.






### 테이블 생성

```sql
CREATE TABLE table (
	column1 datatype [constraints],
    column2 datatype [constraints],
);
```



### 테이블 삭제

```sql
DROP TABLE table;
```





## CRUD



### 추가

> 특정 테이블에 새로운 행을 추가하여 데이터를 추가

```sql
INSERT INTO table (column1, column2) VALUES (value1, value2)
```



> 모든 열에 데이터를 넣을 때에는  column을 명시할 필요가 없음

```sql
ISERT INTO classmates Values (2, 'lee', 30, 'Seoul')
```





### 읽기

> 특정 테이블에 특정 레코드를 조회

```sql
SELECT * FROM table WHERE condition;
# SELECT * FROM classmates WHERE id=1;
```



> 특정 테이블에 특정 레코드의 특정 column 조회

```sql
SELECT column1, column2 FROM table WHERE condition;
```



> 중복없이 가져오기

```sql
SELECT DISTINCT name FROM classmates;
```



> 특정 테이블에 특정 레코드의 개수

```sql
SELECT COUNT(column) FROM table;
```



> 특정 테이블에 특정 레코드의 평균

```sql
SELECT AVG(column) FROM table;
```



> 특정 테이블에 특정 레코드의 합

```sql
SELECT SUM(column) FROM table;
```



> 특정 테이블에 특정 레코드의 최대 / 최소값

```sql
SELECT MAX(column) FROM table;
SELECT MIN(column) FROM table;
```







### 삭제

> 특정 테이블에 특정 레코드를 삭제

```sql
DELETE FROM table WHERE condition;
```







### 수정

> 특정 테이블에 특정 레코드를 수정

```sql
UPDATE table SET column1=value1, column2=value2 WHERE condition;
```







### 기본 구문

```sql
SELECT column FROM table
[WHERE condition] 
[GROUP BY column]
[ORDER BY column (ASC/DESC)]
[LIMIT integer]
```





### LIKE문 활용

```sql
SELECT * FROM classmates WHERE phone LIKE '010-%';
```

- 와일드카드

  | `%`  | 2%                 | 2로 시작하는 값                             |
  | ---- | ------------------ | ------------------------------------------- |
  |      | %2                 | 2로 끝나는 값                               |
  |      | %2%                | 2가 들어가는 값                             |
  | `_`  | _2%                | 아무값이나 들어가고 2번째가 2로 시작하는 값 |
  |      | 1_ _ _             | 1로 시작하고 4자리인 값                     |
  |      | 2 _ % _ % / 2_ _ % | 2로 시작하고 적어도 3자리인 값              |





### ORDER BY

> 정렬, 특정 기준으로 정렬할 수 있음

```sql
SELECT * FROM classmates ORDER BY age ASC name DESC;
# 나이를 기준으로 오름차순 정렬하고, 이름을 기준으로 내림차순
```





###  LIMIT

> 특정 table에서 원하는 개수만큼 가져오기

```sql
SELECT column FROM table LIMIT num;

SELECT name FROM classmates LIMIT 1 OFFSET 2;
# 3번째 있는 이름
```





### GROUP BY

> 특정 컬럼을 기준으로 그룹화 하기

```sql
SELECT sex, COUNT(name) FROM classmates GROUP BY sex;
```

