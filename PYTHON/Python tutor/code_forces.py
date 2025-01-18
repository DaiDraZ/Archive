
from time import perf_counter
import random
rinf = 10e18
linf = -10e18

res = 0
flag = True

arr = []
time_count = [0.0] 
# mat = [[' ' for i in range(7)] for j in range(7)]

def gcd(x: int, y: int) -> int:
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x
def lcm(x: int,y: int) -> int:
    return x*y//gcd(x,y)
def prime(x: int) -> bool: 
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    elif x % 3 == 0 or x % 2 == 0 :
        return False
    else:
        for i in range(5,int(x**0.5) + 2,2):
            if x % i == 0:
                return False
        return True
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()  # Thời gian bắt đầu
        result = func(*args, **kwargs)  # Gọi hàm
        end_time = perf_counter()  # Thời gian kết thúc
        execution_time = end_time - start_time  # Tính thời gian thực thi
        # print(f"  [Time : '{func.__name__}': {execution_time:.6f}s]")
        time_count[0] += execution_time
        return result
    return wrapper

# +=
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# '??????R??????U??????????????????????????LD????D?'
 


@timer
def ck(m):
    var = ''
    while m % 2 == 0: 
        m //= 2
        if m > 1:
            var += f'{2}*'
        else:
            var += f'{2}'
    for i in range(3,int(m**0.5) + 2,2): 
        while m % i == 0: 
            m //= i
            if m > 1:
                var += f'{i}*'
            else:
                var += f'{i}'
    if m > 1:
        var += f'{m}'
    arr.append(var)

t = int(input()) 
for _ in range(t):
    # m = int(input())
    m = random.randint(1,10000000)
    # print(m)
    if prime(m):
        arr.append(str(m))
    else:
        ck(m)
print('\n'.join(arr)) 


# ans = []
# def find(n):
#     x = 0
#     index = 9*(10**x)*(x + 1)
#     l = 1
#     r = l + index - 1
#     f = 0
#     if n < 10:
#         ans.append(n)
#     else:
#         while True:
#             print(l,r)
#             if l <= n and n <= r:
#                 break
#             else:
#                 x += 1 # so luong so dang sau so dau tien
#                 index = 9*(10**x)*(x + 1) # tinh so luong vi tri cua mot day co n chu so
#                 l = r + 1 # so co n chu so bat dau
#                 r = l + index - 1 # so co n chu so cuoi cung
#         return l,r,10**x,n
#         # f = (((n - (l + x))/(x + 1)),((n - l)/(x + 1)))
#         # k = (l + (x + 1)*f)
#         # res = str(10**x + f)
#         # ans.append(res)
#         # return res,f
# print(find(n))

# for i in range(n):
#     find(int(input()))

# for i in ans:
#     print(i)
print(f"[Time : {time_count[0]:.6f}s]") 





