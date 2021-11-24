dict1={}
n = int(input("Enter the number of elements to be added into the dictionary:"))
for i in range(n):
    key = input("Enter key:");
    value = input("Enter value:");
    dict1[key] = value
print(dict1)

print("Sorting by keys")
print("Sort in ascending order:",sorted(dict1))
print("Sort in descending order:",sorted(dict1,reverse = True))

print("Sorting by values")
print("Sort in ascending order:",sorted(dict1.values()))
print("Sort in descending order:",sorted(dict1.values(),reverse = True))
