a = input("Enter the numbers:")
list1 = a.split(",")

list2 = [list1[i] for i in range(len(list1)) if int(list1[i])>0]
print(list2)
