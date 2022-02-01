l1 = input("Enter a list of words:")
llist = l1.split(",")
max1 = len(llist[0])
word = llist[0]
for i in llist:
    if len(i)>max1:
        word=i
        max1 = len(i)
print("The length of the longest word",word,":",max1)