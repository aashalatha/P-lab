num = int(input("Enter a number:"))
flag = 1
for i in range(1,num):
    if num%i == 0:
        flag += 1

if flag > 2:
    print(num,"is not prime")
else:
    print(num,"is prime")
