l = input("Enter the numbers:")
a = l.split(" ")
for i in range(len(a)):
    if int(a[i])>100:
        a[i] = 'over'
print(a)
