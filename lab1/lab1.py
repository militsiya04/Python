# task 1
x = input('Enter x: ')
x = int(x)
y = input('Enter y: ')
y = int(y)
z = 0

if x > 8:
    z = y + 3
else:
    z = 9 * x * y
print('z is equal to', z)
# task 2
n = input('Enter n: ')
n = int(n)
z = x = 1
for i in range(n - 1):
    z = z * (x + 1)
    x = x + 1
print('Factorial of', n, 'is', z)
# task 3
rows = 4
cols = 6
c = 1
a = [[0] * cols for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        a[i][j] = c
        c = c + 1
print(a)
i = j = k = b = 0
s = [1, 2, 3, 4]
while i < (rows * cols):
    b = b + a[j][k]
    i = i + 1
    if (i % cols) == 0:
        s[j] = b
        j = j + 1
        k = 0
    else:
        k = k + 1
for i in range(rows - 1, 0, -1):
    s[i] = s[i] - s[i - 1]
print(s)
