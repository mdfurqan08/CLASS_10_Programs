List = []
for i in range(10):
    x = int(input("Enter the number for the list: "))
    List.append(x)

s = min(List)
m = max(List)
count = int(input("Enter the number to search in the list: "))
frequency = List.count(count)
print("Least value:", s, "Largest Value:", m)
print("Frequency:", frequency, "Count:", count)
