import sys
sys.stdin = open('5185.txt', 'r')


for t in range(1, int(input()) + 1):
    N, Hexa = input().split()
    
    print('#%d' % t, end=' ')
    result = []
    for i in range(int(N)):
        n = int(Hexa[i], 16)
        blist = []
        while True:
            if n < 2:
                blist.insert(0, n)
                break
            m = n % 2
            blist.insert(0, m)
            n //= 2
        
        while True:
            if len(blist) == 4:
                break
            blist.insert(0, 0)
        
        for s in blist:
            print(s, end='')
    print()

'''
bin 함수를 사용하지 않고 구현해 보았다.
각 자리의 16진수 숫자를 4자리 2진수로 표현하여
문자열 형식으로 전부 합쳐 출력해야 한다.
숫자의 값이 2보다 작을 때까지, 2로 나누어 나머지를
리스트에 저장하고, 숫자는 몫으로 대체한다.
4자리 이하로 저장된 배열에 앞쪽에 4자리까지 0을 추가하여 주는 것이 핵심
'''

# bin 사용
# for t in range(1, int(input()) + 1):
#     N, Hexa = input().split()
    
#     AF = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    
#     result = []
    
#     for i in range(int(N)):    
#         s = Hexa[i]
#         if s in AF.keys(): 
#             Bn = list(bin(AF[s]))
#         else:
#             Bn = list(bin(int(s)))
#         Bn = Bn[2:]
#         while True:
#             if len(Bn) == 4:
#                 break
#             Bn.insert(0, '0')
#         result += Bn
#     print('#%d' % t, end=' ')
#     print(''.join(result))




