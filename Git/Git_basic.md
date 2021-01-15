# Git

> 분산 버전관리시스템(DVCS)



## 주요 명령어



### 저장소 생성

- init

```bash
~/Desktop/git
$ git init
Initialized empty Git repository in C:/Users/kkarl/Desktop/git/.git/

```

- clone

  > init이 저장소를 만들고 싶다는 의미, clone은 저장소를 만드는 것을 아니지만 있는 저장소를 가져오겠다는 의미가 된다.

### 버전 관리

- `git status`

  ```bash
  $ git status
  On branch master
  
  # commit이 아직 없다. (버전이력이 없다.)
  No commits yet
  
  # Untracked files -> 현재 버전에 등록되어있지 않은 파일
  Untracked files:
  	# commit될 곳에 포함시키려면(staging area) add 명령어를 써
    (use "git add <file>..." to include in what will be committed)
          a.txt
  
  # 정리멘트 - commit할 것도 없고, 다만 새로 생긴 파일은 있어
  nothing added to commit but untracked files present (use "git add" to track)
  
  ```

  ```bash
  $ git status
  On branch master
  
  No commits yet
  
  # commit 될 변경 사항
  Changes to be committed:
  	# unstage하려면 아래의 명령어를..
    (use "git rm --cached <file>..." to unstage)
          # 새로운 파일 a.txt
          new file:   a.txt
  
  ```

  ```bash
  $ git commit -m 'Init'
  [master (root-commit) 2cbd533] Init
   1 file changed, 0 insertions(+), 0 deletions(-)
   create mode 100644 a.txt
   
  $ git status
  On branch master
  # commit할 것도 없고, 작업 공간도 깨끗.
  nothing to commit, working tree clean
  
  $ git log --oneline
  2cbd533 (HEAD -> master) Init
  ```





### 원격저장소

- 원격 저장소에 등록

  ```bash
  git remote add origin {url}
  ```

- 등록 여부 확인

  ```bash
  git remote -v
  ```

- 제거

  ```bash
  git remote rm origin
  ```

- push

  ```bash
  git push origin master
  ```

  

