# 1 하드코딩.. 심지어 시간도 오래걸렸다..
from collections import deque

def cycling(nums):
    for n, r in nums:
        if r < 0:
            num = wheel[n].pop(0)
            wheel[n].append(num)
        else:
            num = wheel[n].pop()
            wheel[n].insert(0, num)


def rotate(n, r, wheel):
    global t
    target = [wheel[0][2], wheel[1][6], wheel[1][2], wheel[2][6], wheel[2][2], wheel[3][6]]
    
    rot = []
    for i in range(0, len(target), 2):
        if target[i] != target[i+1]:
            rot.append(1)
        else:
            rot.append(0)

    
    rot_n = []
    if n == 1:
        if rot[0] == 0:
            cycling([(0, r)])
            return
        else:
            rot_n.append((0, r))
            rot_n.append((1, -r))
            if rot[1]:
                rot_n.append((2, r))
                if rot[2]:
                    rot_n.append((3, -r))
    
    elif n == 2:
        if rot[0] == 0 and rot[1] == 0:
            cycling([(1, r)])
            return
        else:
            rot_n.append((1, r))
            if rot[0]:
                rot_n.append((0, -r))
            
            if rot[1]:
                rot_n.append((2, -r))
                if rot[2]:
                    rot_n.append((3, r))
    
    elif n == 3:
        if rot[1] == 0 and rot[2] == 0:
            cycling([(2, r)])
            return
        else:
            rot_n.append((2, r))
            if rot[1]:
                rot_n.append((1, -r))
                if rot[0]:
                    rot_n.append((0, r))
            
            if rot[2]:
                rot_n.append((3, -r))

    else:
        if rot[2] == 0:
            cycling([(3, r)])
            return
        else:
            rot_n.append((3, r))
            rot_n.append((2, -r))
            if rot[1]:
                rot_n.append((1, r))
                if rot[0]:
                    rot_n.append((0, -r))
    
    cycling(rot_n)
    

wheel = [list(input()) for _ in range(4)]

K = int(input())
play = deque()
for _ in range(K):
    n, r = map(int, input().split())
    play.append((n, r))

while play:
    n, r = play.popleft()
    rotate(n, r, wheel)

result = 0
k = 1
for i in range(4):
    result += int(wheel[i][0]) * k 
    k *= 2
print(result)

#2 재귀 사용, 왼쪽 오른쪽 구간 나눠서 검사 후 rotate
from collections import deque

def rotate(n, r):
    if r < 0:
        num = wheel[n].popleft()
        wheel[n].append(num)
    else:
        num = wheel[n].pop()
        wheel[n].appendleft(num)

def check_left(n, r):
    if n < 1 or wheel[n][2] == wheel[n+1][6]:
        return
    
    check_left(n-1, -r)
    rotate(n, r)

def check_right(n, r):
    if n > 4 or wheel[n][6] == wheel[n-1][2]:
        return
    
    check_right(n+1, -r)
    rotate(n, r)

wheel = {}
for i in range(1, 5):
    wheel[i] = deque(map(int, list(input())))

K = int(input())

for _ in range(K):
    n, r = map(int, input().split())
    check_left(n-1, -r)
    check_right(n+1, -r)
    rotate(n, r)

result = 0
for i in range(4):
    result += (2**i) * wheel[i+1][0]

print(result)