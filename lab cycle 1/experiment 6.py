a = input("Enter the values to the list:")

l1 = a.split(" ")
l2 = []

for i in range(len(l1)):
    if int(l1[i])%2 != 0:
        l2.append(l1[i])

print(l2)
