 # Django model





## Model 



### model 정의

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- `models.Model`을 상속받는 클래스 생성
- 구성하고 싶은 테이블의 속성 이름을 지정하고, 각각 데이터 타입에 맞춰 필드를 정의
- `id (pk)`값은 자동 생성
- 필드 값
  - `CharField`
    - `max_length` 필수
  - `DateTimeField`
    - `auto_now_add` (선택) 생성시에만 자동으로 해당 시간 값 설정
    - `auto_now` (선택) 수정시마다 자동으로 해당 시간 값 설정
  - 많은 필드들은 공식 문서 확인





### migration

> 마이그레이션은 model의 변경 사항을 데이터베이스 스키마에 반영하기 위한 방법이다.

- 정의된 모델을 데이터베이스에 반영하기 위해 마이그레이션 파일을 생성

  ```bash
  $ python manage.py makemigrations
  Migrations for 'articles':
  articles\migrations\0001_initial.py
      - Create model Article
  ```
  
- 모델의 변경사항을 기록하여 app별 `migrations/` 폴더에 저장된다.

- 생성된 파일을 데이터베이스에 반영

  ```bash
  $ python manage.py migrate
  Operations to perform:
    Apply all migrations: admin, articles, auth, contenttypes, sessions
  Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying articles.0001_initial... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying sessions.0001_initial... OK
  ```

  - django가 기본적으로 활용하는 데이터베이스 마이그레이션 파일들이 있기에, 프로젝트 생성시 migrate를 하는 습관을 들이자

- 관련 명령어

  ```bash
  $ python manage.py makemigrations
  $ python manage.py showmigrations
  $ python manage.py migrate
  $ python manage.py sqlmigrate article 0001
  ```

  - 특정 app만 마이그레이션 할 수 있음





### Django ORM

> Django에서는 Django ORM (object relational mapper) 을 이용하여 python으로 데이터베이스를 조작할 수 있다.

-  기본적인 데이터베이스 조작을 CRUD operation이라고 한다.



#### django shell

- 먼저, 추가적인 패키지 설치가 필요하다

  ```bash
  $ pip install django-extensions ipython
  ```

  - `django-extensions`는 django 개발에 유용한 기능들을 제공한다. 자세한 사항은 구글링

  - `ipython`은 쉘을 조금 더 편하게 활용할 수 있게 해준다.

```bash
$ python manage.py shell_plus
```

- 종료는 exit, ctrl+d를 통해 할 수 있다.



#### Create (생성)

```python
# 1
article = Article()
article.title = '제목'
article.content = '내용'
article.save()

# 2
Article.objects.create(title='제목', content='내용')

# 3
article = Article(title='제목', content='내용')
article.save()
```



### Read (조회)

```python
# 전체 데이터 조회
Article.objects.all()

# 단일 데이터 조회
Article.objects.get(id=1)
```



### Update (수정)

```python
article = Article.objects.get(id=1)
article.title = '수정'
article.save()
```



### Delete (삭제)

```python
article = Article.objects.get(id=1)
article.delete()
```





### Admin 페이지

> Django에서는 기본 url + /admin으로 쉽게 관리자 페이지에 접속할 수 있다.



#### admin 등록

```python
# admin.py

from django.conrtib import admin
from .models import Article

admin.site.register(Article)
```



#### 계정 생성

```bash
$ python manage.py createsuperuser
사용자 이름 (leave blank to use 'kkarl'): admin
이메일 주소:      
Password: 
Password (again):
```

