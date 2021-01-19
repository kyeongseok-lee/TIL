# 자주 발생하는 django error 



### settings.py

- `INSTALLED_APP`에 app 등록
- trailing comma 필수
- base.html 주소 확실하게 등록
  - `TEMPLATES ` 의  `DIRS`



### urls.py

- urls.py가 없는 경우
- urls.py 내에 urlpatterns가 정의 되어 있지 않은 경우

- variable routing 한 변수 이름과 view 함수 선언시 인자가 같지 않은 경우





### model 설정 

- 단순 오타를 낸 경우
  - migartions 이력 삭제
  - db 삭제
  - `__init__.py` 삭제 금지
  - 다시 makemigrations, migrate