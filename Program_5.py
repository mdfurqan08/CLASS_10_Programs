a = 0
b = 1
n = 10  
print(a, b)

for i in range(n-1):
    c = a + b
    print(c)
    a = b
    b = c
