# Django 

> python web framework

- `Django`는 python 오픈소스 웹 어플리케이션 프레임워크로, MVC 모델 패턴을 따르고 있다.
- `MVC` 패턴은 `Model, View, Controller` 인데, `Django`에서는 `Model, Template, View`로 표현한다.
  - `Model` : 데이터 관리
  - `Template` : 인터페이스 (화면)
  - `View` : 중간관리 (상호 동작)



- `django` 매커니즘
  - HTTP Request  -> `URLS` (`urls.py`) : `URLS`에 요청을 보낸다
  - `URLS` -> `View` (`views.py`) : `View`에 요청을 전달한다
  - `View`는 `Model` (`models.py`) 에 data를 읽고 쓰게하여 받아오고, `Template` (`html`) 로부터 html을 전달 받는다.
  - `View` -> HTTP Response : 최종 HTML을 전달한다.





## django 시작하기



### 설치

```bash
$ pip install django=='버전'
```



### 프로젝트 시작

```bash
$ django-admin startproject '프로젝트명'
$ cd '프로젝트명'
$ python manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply 
the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 14, 2021 - 20:22:31
Django version 2.1.15, using settings 'django_intro.settings'
Starting development server at http://127.0.0.1:8000/ # url 클릭 시 실행
Quit the server with CTRL-BREAK. # ctrl + c 서버 끄기
```





### 리눅스 명령어 (basic)

- `cd` : change directory

  ```bash
  # '디렉토리명'으로 이동
  $ cd '디렉토리'
  
  # 상위 디렉토리로 이동
  $ cd ..
  ```

- `ls` :  현재 디렉토리내의 파일 목록

  ```bash
  $ ls
  db.sqlite3  django_intro  manage.py
  
  $ ls -al # 모든 정보
  total 5
  drwxr-xr-x 1 kkarl 197609   0  1월 14 20:14 .
  drwxr-xr-x 1 kkarl 197609   0  1월 14 20:14 ..
  -rw-r--r-- 1 kkarl 197609   0  1월 14 20:14 db.sqlite3
  drwxr-xr-x 1 kkarl 197609   0  1월 14 20:14 django_intro
  -rwxr-xr-x 1 kkarl 197609 559  1월 14 20:13 manage.py
  ```

  

### App 생성하기

> django는 여러가지 앱을 하나의 프로젝트안에 구성한다.
>
> ex) 회원 앱 -> account, 

```bash
$ python manage.py startapp '앱이름'
```

- 앱 생성 후 반드시 `settings.py`에 `INSTALLED_APPS`에 등록을 해주어야 한다.

  ```python
  INSTALLED_APPS = [
      # local apps
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      
      # third party apps
      '앱이름'
  ]
  ```

  



### 기본 흐름

> `django`에서의 기본 흐름은 `url`에 `path`를 작성하고, 해당 `views`에 `함수`를 작성하고 `렌더링`을 하고, 해당 `templates`에 `html`을 작성한다.

 #### urls.py

```python
# '프로젝트명'/urls.py
from django.contrib import admin
from django.urls import path
from '앱이름' import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url이름/', views.lotto), # 기본url/url이름 으로 접속할 시 해당 앱의 views의 lotto 함수를 실행한다. 'url이름' 뒤에 '/'는 반드시 해주어야 한다.
]
```



#### views.py

```python
def index(request):
    lotto_nums = random.sample(range(1, 46), 6)
    context = {
        'lotto_nums': lotto_nums
    }
    
    return render(request, 'lotto.html', context)
```

- 함수의 첫번 째 인자는 `request`로 작성한다.

- render를 통해 반환
  - 첫번째 : `request`
  - 두번째 : `template`
  - 세번째 : `template`에서 활용할 `dictionary` 값



#### templates / html 파일

```html
<!-- 반환 할 파일은 앱이름/templates/lotto.html(html파일) 로 생성한다.-->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>{{ lotto_nums }}</h1> <!-- context로 넘겨준 dictionary를 html에서 {{}}로 활용한다.-->
</body>
</html>
```

