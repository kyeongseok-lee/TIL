# Django Template 



## Django Template Languages (DTL)

> Django의 Template(html)은 DTL로 구성된다.



### 기초

1. 출력 `{{  }}`

   ```html
   {{ name }} 
   
   // views.py의 context로 넘겨준 변수를 {{ }}에 담아 출력
   ```

2. 문법 `{% %}`

   ```html
   {% for comment in comments %}
   {% endfor %}
   ```

3. 주석 `{# #}`

   ```html
   {# 주석 #}
   ```

   

### 반복문

```html
{% for reply in replies %}
	<li>{{ reply }}</li>
{% endfor %}
```

- `{{ forloop.counter }}` 번호 매기기
- `{{ forloop.counter0 }}` 0부터 카운팅
- `{% empty %}` 비었다면..





### 조건문

```html
{% if user == 'admin' %}
	<p>
        관리자 입니다.
	</p>
{% else %}
    <p>
        권한이 없습니다.
    </p>
{% endif %}
```





### built-in tag, filter

- 공식문서 확인

```html
{{ content|length }}
{{ content|truncatechars:10 }}
```





## Template



### template 확장

##### `base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  {% block css %}
  {% endblock %}
  
</head>
<body>
  <h1>Django 기초 문법 학습</h1>
  {% block body %}
  {% endblock %}
</body>
</html>
```

##### `lunch.html`

```html
{% extends 'base.html' %}

{% block css %}
<style>
  h1 {
    color: green;
  }
</style>
{% endblock %}

{% block body %}
  <h1>오늘 점심 메뉴 추천</h1>
  <h3>{{ reco_menu }}!!</h3>
  <hr>
  <p>{{ menu }}</p>
  <ul>
    {% for food in menu %}
    <li>{{ food }}</li>
    {% endfor %}
  </ul>
{% endblock %}
```



### template 설정

```python
# settings.py

TEMPLATES = [
    {
        # DTL 엔진 사용. jinja2 등으로 변경 가능하다.
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # INSTALLED_APPS에 등록된 app들의 templates을 활용한다.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```





## Form 요청 처리

> 1. 사용자들로부터 값을 받는다.
> 2.  단순 출력하는 페이지 구성



### url 지정

```python
path('new/', views.new)
```



### view 함수 생성

```python
def new(request):
    return render(request, 'boards/new.html')
```



### templete

```html
<form action="/boards/complete">
    <input type="text" name="title">
</form>
```

- form 태그에는 action 정의
  - 사용자로부터 내용을 받아서 처리하는 url
- input 태그에는 `name` 속성을 통해 사용자가 입력한 내용을 담을 변수 이름을 지정한다.
- `/boards/complete/?title='제목'`



### templete 경로 설정

- app 별 urls.py 정의
- app templete 폴더

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



## 사용자 요청 처리



### urls.py 정의

```python
path('/boards/complete', views.complete)
```



### views.py

```python
def complete(request):
    title = request.GET.get('title')
    context = {
        'title': title
    }
    return render(request, 'boards/complete.html', context)
```

- request에는 요청과 관련된 정보들이 저장되어 있음



### template

```html
<h1>
    제목 : {{ title }}
</h1>
```

