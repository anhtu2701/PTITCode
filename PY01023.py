# Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố. Kết quả được in ra theo mẫu trong ví dụ, trong đó thêm số thừa số 1 (không phải nguyên tố) ở đầu kết quả phân tích.
# Input
# Dòng đầu ghi số bộ test, mỗi test ghi trên một dòng số nguyên dương N không quá 6 chữ số.
import math

for _ in range(int(input())):
    n = int(input())
    res = '1'
    for i in range(2, math.isqrt(n)+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n /= i
        if cnt != 0:
            res += ' * ' + str(i) + '^' + str(cnt)
        if n == 1:
            break
    if n != 1:
        res += ' * ' + str(int(n)) + '^1'
    print(res)

