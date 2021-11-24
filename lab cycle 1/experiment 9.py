dict1={}
n = int(input("Enter the number of elements to be added into the first dictionary:"))
for i in range(n):
    key = input("Enter key:");
    value = input("Enter value:");
    dict1[key] = value
print(dict1)

dict2={}
n = int(input("Enter the number of elements to be added into the second dictionary:"))
for i in range(n):
    key = input("Enter key:");
    value = input("Enter value:");
    dict2[key] = value
print(dict2)

dict1.update(dict2)
print(dict1)
