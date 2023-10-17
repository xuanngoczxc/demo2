#Tìm giá trị lớn nhất trong ma trận
n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
print("Ma trận vừa nhập: ")
for i in range(n):
    for j in range(m):
        print(a[i][j], end = " ")
    print()
num_max = a[0][0]
print("giá trị lớn nhất trong ma trận trên là:")
for i in range(n):
    for j in range(m):
        if a[i][j] > num_max:
            num_max = a[i][j]
print(num_max)