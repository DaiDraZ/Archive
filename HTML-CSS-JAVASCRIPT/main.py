
# ans += 1
import sys

def pascal(n: int):
    dp = [] 
    arr = [1]
    for i in range(0,n):
        dp.append(arr[:])
        temp = 1
        if len(arr) < 2:
            arr.append(1) 
        else:
            for j in range(1,len(arr)):
                x = arr[j]
                arr[j] = arr[j] + temp + 1
                temp = x
            arr.append(1)
    return dp
def fibo(n :int):
    fib = [1,1]
    if n < 3:
        return 1
    else:
        for i in range(n - 2):
            t = fib[1]
            fib[1] = (fib[0] + fib[1]) % (10**12 + 7)
            fib[0] = t
            #print(fib)
    # sys.set_int_max_str_digits(10000000)
    return fib[1]

def fibo_matrix(n: int) -> int:
    MOD = 1000000007  # Modulo lớn để tránh số quá lớn

    # Hàm nhân 2 ma trận 2x2 với modulo
    def mat_mult(A, B):
        return [
            [
                (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
                (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
            ],
            [
                (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
                (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
            ]
        ]

    # Hàm lũy thừa ma trận với phương pháp nhân nhanh
    def mat_pow(mat, p):
        res = [[1, 0], [0, 1]]  # Ma trận đơn vị 2x2
        base = mat

        while p:
            if p % 2 == 1:
                res = mat_mult(res, base)
            base = mat_mult(base, base)
            p //= 2

        return res

    if n == 1 or n == 2:
        return 1
    F = [[1, 1], [1, 0]]  # Ma trận cơ sở
    result = mat_pow(F, n - 1)
    return result[0][0]  # F(n) là phần tử [0][0] của ma trận



print(fibo_matrix(5))



