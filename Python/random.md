# random 모듈



### 각종 함수

```python
import random

# 0부터 1사이의 실수를 랜덤으로 리턴한다.
pick = random.random() # random float x, 0.0 <= x < 1.0

# 2개 숫자 사이의 랜덤 실수를 리턴한다.
pick = random.uniform(1, 10) # random float x, 1.0 <= x < 10.0

# 2개 숫자 사이의 랜덤 정수를 리턴한다. 2번째인자도 포함
pick = random.randint(1, 10) # random Integer x, 1 <= x <= 10

# range(start, end, step) 함수로 만들어지는 정수 중 하나를 랜덤으로 리턴한다.
pick = random.randrange(0, 101, 2) # 짝수 from 0 to 100

# 랜덤하게 하나의 원소를 선택한다.
pick = random.choice('abc') # 1 random element

# 랜덤하게 여러 개의 원소를 선택한다.
pick = random.sample([1, 2, 3, 4, 5], 3) # choose 3 random element

# 원소의 순서를 랜덤하게 바꾼다.
pick = [1, 2, 3, 4, 5]
random.shuffle(pick) # random shuffle
```

