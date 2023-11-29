n = int(input())
list1 = set()
list2 = set()
m = int(input())
for i in range(m):
    list1.add(input())

for i in range(n - 1):
    n = int(input())
    for j in range(n):
        list2.add(input())
    list1 = list1.intersection(list2)
    list2.clear()
for i in list1:
    print(i)