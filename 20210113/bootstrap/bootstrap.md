# CDN

`Content Delivery (Distribution) Network`

#### 컨텐츠 (CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.

> 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능 (지리적 이점) 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐. CDN은 보통 적절한 수준의 캐시 설정으로 빠르게 로딩할 수 있음.





# Bootstrap



### component

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <title>Document</title>
  <style>
    #carouselExampleControls {
      width: 300px;
    }
    

  </style>
</head>
<body>
  <!-- alert -->
  <div class="alert alert-primary" role="alert">
    A simple primary alert—check it out!
  </div>
  <!-- badge -->
  <h1>Bootstrap <span class="badge bg-danger">HOT</span></h1>
  <!-- button -->
  <button type="button" class="btn btn-warning">Warning</button>
  <!-- card -->
  <div class="card" style="width: 18rem;">
    <img src="https://picsum.photos/200" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
  </div>
  <!-- carousel -->
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="https://picsum.photos/200" class="d-block w-100 h-25" alt="...">
      </div>
      <div class="carousel-item">
        <img src="https://picsum.photos/200" class="d-block w-100 h-25" alt="...">
      </div>
      <div class="carousel-item">
        <img src="https://picsum.photos/200" class="d-block w-100 h-25" alt="...">
      </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </a>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html>

<!-- 이 외에도 많은 component들이 있다. 공식 홈페이지 document 참조 -->
```



### grid

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <style>
    .box {
      height: 100px;
      background-color: bisque;
      margin-top: 10px;
      border: 1px solid black; 
    }
    body {
      height: 10000px;
    }
    .card {
      height: 70px;
      background-color: cornflowerblue;
    }
  </style>
</head>
<body>
  <div class="container">
    컨테이너 영역
  </div>
  <div class="container-fluid">
    컨테이너 영역
  </div>
  <!-- grid system 
  12를 기준으로 나눠 갖도록 설정한다.
  -->
  <div class="container">
    <div class="row">
      <div class="col">1</div>
      <div class="col">2</div>
    </div>
    <div class="row">
      <div class="col-4">1</div>
      <div class="col-4">2</div>
      <div class="col-4">3</div>
    </div>
    <div class="row">
      <div class="col-6">1</div>
      <div class="col-6">2</div>
    </div>
    <div class="row">
      <div class="col-3">1</div>
      <div class="col-3">2</div>
      <div class="col-3">3</div>
      <div class="col-3">4</div>
    </div>
    <div class="row">
      <div class="col-3">1</div>
      <div class="col-6">2</div>
      <div class="col-3">3</div>
    </div>
    <!-- 반응형 
    gutter는 item들간의 padding
    제거 가능 : g-0
    -->
    <div class="row g-0">
      <div class="col-6 col-md-4">
        <div class="box">1</div>
      </div>
      <div class="col-6 col-md-4">
        <div class="box">2</div>
      </div>
      <div class="col-6 col-md-4">
        <div class="box">3</div>
      </div>
    </div>
    <!-- breakpoint -->
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4">
        <div class="box">1</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4">
        <div class="box">2</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4">
        <div class="box">3</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4">
        <div class="box">4</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4">
        <div class="box">5</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4">
        <div class="box">6</div>
      </div>
    </div>
    <!-- offset -->
    <div class="row">
      <div class="col-md-4">
        <div class="box"></div>
      </div>
      <div class="col-md-4 offset-md-4">
        <div class="box"></div>
      </div>
    </div>
    <div class="row">
      <div class="col-1">
        <div class="box"></div>
      </div>
      <div class="col-1">
        <div class="box"></div>
      </div>
      <div class="col-1">
        <div class="box"></div>
      </div>
      <div class="col-1 offset-6">
        <div class="box"></div>
      </div>
      <div class="col-1">
        <div class="box"></div>
      </div>
      <div class="col-1">
        <div class="box"></div>
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-6">
        <div class="card">
          <div class="row g-0">
            <div class="col-8">Text area</div>
            <div class="col-4">Image area</div>
          </div>
        </div>
      </div>
      <div class="col-6">
        <div class="card"></div>
      </div>
    </div>

  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html>
```

