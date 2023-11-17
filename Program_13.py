list = []

for i in range(0, 10, 1):
    x = input("Enter the number:")
    list.append(x)
    print(list)

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum = 0

for i in range(0, 10, 1):
    sum = sum + list[i]

print(sum)
