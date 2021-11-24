l1 = input("Enter the values of first list:")
l2 = input("Enter the values of second list:")

list1 = l1.split(" ")
list2 = l2.split(" ")

#checks whether the lists are of same length

if len(list1)==len(list2):
    print("The lists are of same length")
else:
    print("The lists are not of same length")

#list sums to the same value

sum1 = 0
sum2 = 0
for i in range(len(list1)):
    sum1 = sum1 + int(list1[i])
for i in range(len(list2)):
    sum2 = sum2 + int(list2[i])

if sum1 == sum2:
    print("The sum of the lists are same")
else:
    print("The sum of the lists are not same")

#any value occur in both

if len(list1) >= len(list2):
    for i in range(len(list1)):
        if list1[i] in list2[::]:
            print(list1[i],"occurs in both the lists")
else:
    for i in range(len(list2)):
        if list2[i] in list1[::]:
            print(list2[i],"occurs in both the lists")
    
