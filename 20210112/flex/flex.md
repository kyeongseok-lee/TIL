# flex

- 배치를 할 때  `float`, `position`으로만 지정했지만, `flex` 이후에 보다 효율적이고 간편한 배치가 가능해졌다.



### 주요 개념

- `container` ,`item`

  ```html
  <style>
      .container {
          display: flex;
      }
  </style>
  
  <div class="container">
      <div class="item"></div>
      <div class="item"></div>
  </div>
  ```

- `main axis`, `cross axis`

  - `main axis`을 기준으로 배치를 한다. 
  - `flex-direction` 속성 값이 `main axis`을 결정한다.
    - `row (기본값)`, `row-reverse`, `column`, `column-reverse`
  - 모든 `item`들은 기본적으로 행으로 배치 되고, `cross axis`을 모두 채운다.
  - 모든 `item`들은 본인의 너비 혹은 컨텐츠 영역만큼 너비를 가지게 된다.
    - 경우에 따라, 지정받은 너비보다 작을 수 있다. (`flex-wrap`의 속성값이 기본적으로 `nowrap`이기 때문에)





### 주요 속성

#### 1. flex-grow

> 남은 너비를 비율로 나눠 가진다.
>
> 기본값 : 0

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flex</title>
	<link rel="stylesheet" href="style.css">
	<style>
    .container {
      display: flex;
    }
    .item {
      width: 100px;
    }
    .item1 {
      /* 기본값 0 
      남은 너비를 각각 비율로 가져간다.
      */
      flex-grow: 0;
    }
     /* item1, 2, 3이 100px씩 차지하고 남은 700px을 2, 3이
     2:3의 비율로 나눠 가진다.   
     */   
    .item2 {
      /* 100 + 700 * 2/5 */
      flex-grow: 2;
    }
    .item3 {
      /* 100 + 700 * 3/5 */
      flex-grow: 3;
    }
  </style>
</head>
<body>
	<div class="container">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
	</div>
</body>
</html>
```



#### 2. justify-content

> main axis 를 기준으로 정렬한다.
>
> 기본값 : flex-start

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flex</title>
	<link rel="stylesheet" href="style.css">
	<style>
    .container {
      display: flex;
      margin: 1rem 0;
    }
    .item {
      width: 100px;
    }
    .jc-start {
      justify-content: flex-start;
    }
    .jc-center {
      justify-content: center;
    }
    .jc-end {
      justify-content: flex-end;
    }
    .jc-around {
      justify-content: space-around;
    }
    .jc-between {
      justify-content: space-between;
    }
    .jc-evenly {
      justify-content: space-evenly;
    }
	</style>
</head>
<body>
	<div class="container jc-start">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container jc-center">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container jc-end">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container jc-around">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container jc-between">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container jc-evenly">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
	</div>
</body>
</html>
```



#### 3. align-items

> cross axis 를 기준으로 정렬한다.
>
> 기본값 : stretch

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flex</title>
	<link rel="stylesheet" href="style.css">
	<style>
    .container {
      display: flex;
      height: 30vh;
    }
    .ai-stretch {
      /* 기본값 stretch */
      align-items: stretch;
    }
    .ai-center {
      align-items: center;
    }
    .ai-start {
      align-items: flex-start;
    }
    .ai-end {
      align-items: flex-end;
    }
    .ai-baseline {
      /* font size가 다른 아이템들의 밑라인을 맞춰줌 */
      align-items: baseline;
    }
    .item4 {
      font-size: 40px
    }
    .item5 {
      font-size: 100px;
    }
    .item6 {
      font-size: 60px
    }
	</style>
</head>
<body>
	<div class="container ai-stretch">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container ai-center">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container ai-start">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container ai-end">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
  </div>
  <div class="container ai-baseline">
		<div class="item item4">4</div>
		<div class="item item5">5</div>
		<div class="item item6">6</div>
  </div>
  
</body>
</html>
```



#### 4. order

> 아이템의 순서를 지정할 수 있다.
>
> 기본값 : 0

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flex</title>
	<link rel="stylesheet" href="style.css">
	<style>
    .container {
      display: flex;
    }
    /* order 기본값 0  */
    .item2 {
      order: -1;
    }
    .item6 {
      order: -2
    }
    .item10 {
      order: 1;
    }
    .item5 {
      order: 2;
    }
    .item9 {
      order: 3;
    }
    /* 6 2 ````` 10 5 9 */
	</style>
</head>
<body>
	<div class="container">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
		<div class="item item3">3</div>
		<div class="item item4">4</div>
		<div class="item item5">5</div>
		<div class="item item6">6</div>
		<div class="item item7">7</div>
		<div class="item item8">8</div>
		<div class="item item9">9</div>
		<div class="item item10">10</div>
		<div class="item item11">11</div>
		<div class="item item12">12</div>
	</div>
</body>
</html>
```



#### 5. align-self

> 아이템에 직접 align을 지정할 수 있다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Flex</title>
	<link rel="stylesheet" href="style.css">
	<style>
    .container {
      display: flex;
      height: 50vh;
    }
    .item1 {
      align-self: flex-start;
    }
    .item2 {
      align-self: stretch;
    }
    .item3 {
      align-self: center;
    }
    .item4 {
      align-self: flex-end;
    }
    .item5 {
      align-self: baseline;
    }
	</style>
</head>
<body>
	<div class="container">
		<div class="item item1">1</div>
		<div class="item item2">2</div>
    <div class="item item3">3</div>
    <div class="item item4">4</div>
		<div class="item item5">5</div>
	</div>
</body>
</html>
```

