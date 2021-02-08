### 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   User.obejects.all()
   
   
   users = User.objects.all()
   type(users)
   #=> django.db.models.query.QuerySet
   print(users.query) 
   # queryset만 sql문 출력 가능
   #=> SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user"
   
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(
   	first_name='구름',
       last_name='김',
       age=100,
       country='제주도',
       phone='010-1234-1234',
       balance=10000000000000
   )
   ```

   ```sql
   -- sql
   INSERT INTO users_user ('first_name', 'last_name', 'age', 'country', 'phone', 'balance') VALUES ('근제', '성', 20, '서울', '010-1243-1345', 99999999999)
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류 발생

3. 해당 user 레코드 조회

   ```python
   # orm
   User.objects.get(id=100)
   ```

   - `get`은 쿼리 결과가 반드시 하나여아 한다. 이외에는 모두 오류를 반환한다.

      ```sql
   -- sql
   SELECT * FROM users_user WHERE id = 100;
      ```

4. 해당 user 레코드 수정

   ```python
   # orm
   user = User.objects.get(id=100)
   user.last_name = '성'
   user.save()
   ```

      ```sql
   -- sql
   UPDATE users_user SET last_name = '최' WHERE id = 100;
      ```

5. 해당 user 레코드 삭제

   ```python
   # orm
   User.objects.get(id=101).delete()
   ```

      ```sql
   -- sql
   DELETE FROM users_user
   WHERE id = 102;
      ```

### 조건에 따른 쿼리문

1. 전체 인원 수

   ```python
   # orm
   User.objects.count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
      ```

2. 나이가 30인 사람의 이름

   ```python
   # orm
   User.objects.filter(age=30).values('first_name')
   # dict으로 반환해준다.
   ```

      ```sql
   -- sql
   SELECT first_name FROM users_user WHERE age = 30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   > 대소관계
   >
   > `__gte` : >= 
   >
   > `__gt`  : >
   >
   > `__lte` : <=
   >
   > `__lt` : <

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age >= 30;
   ```

4. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30).filter(last_name='김').count()
   
   User.objects.filter(age=30, last_name='김').count()
   ```

   ```python
   # 만약 OR을 쓰고 싶을 땐
   from django.db.models import Q
   
   User.objects.filter(Q(age=30) | Q(last_name='김')).count()
   ```

   

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age = 30 AND last_name = '김';
      ```

5. 지역번호가 02인 사람의 인원 수

   > https://docs.djangoproject.com/en/2.2/topics/db/queries/#escaping-percent-signs-and-underscores-in-like-statements

   ```python
   # orm
   User.objects.filter(phone__startswith='02-').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
      ```

6. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT first_name FROM users_user WHERE country = '강원도' AND last_name = '황';
      ```



### 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람 10명

   ```python
   # orm
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY age DESC LIMT 10;
      ```

2. 잔액이 적은 사람 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY balance ASC LIMT 10;
      ```

3. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.order_by('-last_name', '-first_name')[4]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user 
   ORDER BY last_name DESC first_name DESC
   LIMIT 1 OFFSET 4;
      ```



### 표현식

> 표현식을 위해서는 [aggregate]([https://docs.djangoproject.com/en/2.2/topics/db/aggregation/](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/)) 를 알아야한다.
>
> 개별 object CRUD를 django 쿼리를 통해서 가능하다.
>
> 만약, QuerySet의 요약된 정보를 얻고 싶다면, aggregate 메서드를 써야 한다.

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   SELECT Avg(age) FROM users_user WHERE last_name = '김';
      ```

3. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   from django.db.models import Max
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

4. 계좌 잔액 총액

   ```python
   # orm
   from django.db.models import Sum
   User.objects.aggregate(Sum('balance'))
   ```

      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```



### Group by

> annotate는 개별 item에 추가 필드를 구성한다.
> 추후 1:N 관계에서 활용된다.

1. 지역별 인원 수

   ```python
   # orm
   from django.db.models import Count
   User.objects.values('country').annotate(Count('country'))
   ```

   ```sql
   -- sql
   SELECT country, COUNT(country) FROM users_user GROUP BY country;
   ```

