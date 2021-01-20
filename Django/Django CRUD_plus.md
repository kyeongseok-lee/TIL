# Django CRUD

- [기본 CRUD](./Django_model.md)





### urls.py 이름 정의

- 기존

  ```python
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index)
  ]
  ```

- 이름 정의

  ```python
  from django.urls import path
  from . import views
  
  app_name = 'articles'	# 여러가지 앱을 사용할 경우 지정한 url 이름이 겹칠 수가 있으므로, app name도 지정해주어 에러를 방지한다.
  
  urlpatterns = [
      path('', views.index, name='index'), # 이름 지정
  ]
  ```

- 사용

  ```html
  <!-- 아래와 같은 문법으로 사용한다. app이름:url이름 -->
  <a href="{% url 'articles:index' %}">게시글 목록 보기</a>
  
  <!-- variable routing이 있다면 띄어쓰고 변수를 넣어준다. -->
  <a href="{% url 'articles:detail' article.pk %}">글 보러가기</a>
  ```





### get_object_or_404

- 예를 들어, 게시글의 100번째 글의 상세정보를 보기 위해 주소창에서 `도메인 + /articles/100`을 입력하였다. 현재 게시글은 50번째 글까지만 있었고 100번째 글은 존재하지 않았다.  그런데 500 error가 발생했다.
- 이것이 서버 에러인것인가? 100번째 글을 작성하지 않아서 발생한 오류였으니, 404 error가 맞지 않나?
- 이를 방지하기 위하여 `get_object_or_404`를 사용한다.

```python
from django.shortcuts import get_object_or_404
# article = Article.objects.get(id=pk)
article = get_object_or_404(Article, id=pk)
```





### form

- method
  - GET : 정보를 얻어올 때 사용
  - POST : 데이터에 입력할 때 사용
    - `{% csrf_token %}` 정보 보호를 위하여 사용, 입력하지 않으면 error 발생





### static 폴더 지정

```python
# serving 되는 url 앞에 붙음
STATIC_URL = '/static/'
# app 디렉토리가 아닌 static 폴더 지정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

