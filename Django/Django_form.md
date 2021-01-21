# Django form



### HTTP

>  HyperText Transfer Protocol

- 리소스를 가져올 수 있도록 해주는 프로토콜, 웹에서 이루어지는 모든 데이터 교환의 기초
- 클라이언트-서버 프로토콜로 클라이언트에 의해 전송된 메시지는 요청, 서버에서 전송되는 메시지를 응답
- HTTP/1.1, HTTP/2



### 요청

- URL (Uniform Resource Locators)
  - 웹에서 정해진 유일한 자원의 주소
- 프로토콜://도메인:포트/경로(path)/?파라미터#앵커





### HTTP 메서드

- 주어진 리소스에 수행하길 원하는 행동으로 HTTP verb 라고 부르기도 한다.
- `GET` : 특정 리소스 표시
  - \<a> 태그 \<form> 및 브라우저에서 주소창을 보내는 요청 등
  - URL을 활용하여 데이터를 전송함. 따라서, 크기 제한 및 보안 이슈가 있다.
- `POST` : 특정 리소스에 제출 (서버의 상태 변화)
  - 보통 HTML Form을 통해 서버에 전송하며, 서버의 변경사항을 만듬
  - HTTP 요청 메시지의 body에 데이터를 전송함





### ModelForm

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
```

```python
# forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 원하는대로 customize
    title = forms.CharField(
        max_length=100, 
        label='제목', 
        help_text='제목을 100자 이내로 작성하세요', 
        widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': '제목 입력'
            }
    ))
    content = forms.CharField(
        label='내용',
        help_text='자유롭게 작성해주세요',
        widget=forms.Textarea(
            attrs={
                'row': 5,
                'col': 50
            }
        )
    )
    class meta: # meta class를 활용하여 modelform 정의
        model = Article
        fields = ['title', 'content'] # 원하는 field만 
```

```python
# views.py

# 게시물 생성이나 수정을 할 때 method로 구분하여 한 함수내에서 요청을 해결한다.
def create(request):
    if request.method == 'POST': # POST 요청시
        form = ArticleForm(request.POST)
        if form.is_valid(): # 유효성 검사
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def update(request, pk):
    article = get_object_or_404(Article, id=pk) # article instance
    if request.method == 'POST': # POST 요청시
        form = ArticleForm(request.POST, instance=article) # instance를 지정해주어야 새로운 글이 생기는 것이 아닌 원래 글을 수정하게 된다.
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article) # 원래 글 보여주기
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)
```



### form 활용

```python
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block body %}
  <!-- 분기의 기준은 url_name이다. path로 하면 url이 바뀔 때마다 바꿔줘야 한다. -->
  {% if request.resolver_match.url_name == 'create' %}
    <h2>새 글쓰기</h2>
  {% else %}
    <h2>수정하기</h2>
  {% endif %}

  <!-- bootstrap4 활용 -->
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class="btn btn-primary">제출</button>
  </form>
  <hr>

  <!-- 그냥 활용 -->
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value='제출'>
  </form>
  <hr>


  <!-- loop 활용, 공식문서 확인-->
  <form action="" method="POST">
    {% csrf_token %}
    {% for field in form %}
      <div class="fieldWrapper">
          {{ field.errors }}
          {{ field.label_tag }} <br> {{ field }}
          {% if field.help_text %}
          <p class="help">{{ field.help_text|safe }}</p>
          {% endif %}
      </div>
    {% endfor %}
    <input type="submit" value='제출'>
  </form>
{% endblock %}
```





