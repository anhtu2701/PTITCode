# Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
# Hãy sắp xếp dãy số theo tích các chữ số tăng dần. Nếu tích các chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.
# Input
# Dòng đầu ghi số bộ test (không quá 10)
# Mỗi bộ test gồm 2 dòng:
# Dòng đầu là số N (N < 100)
# Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.

def multi_digits(n):
    res = 1
    while n != 0:
        res *= n % 10
        n //= 10
    return res

for _ in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=lambda s: (multi_digits(int(s)),int(s)))
    print(*a)

