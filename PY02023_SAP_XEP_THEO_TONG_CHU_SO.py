# Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
# Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.
# Input
# Dòng đầu ghi số bộ test (không quá 10)
# Mỗi bộ test gồm 2 dòng:
# Dòng đầu là số N (N < 100)
# Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.

for _ in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=lambda x: (sum(int(i) for i in x),int(x)))
    print(*a)