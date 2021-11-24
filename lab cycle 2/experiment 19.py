num = int(input("Enter a number:"))
sum = 0
n = num
while n>0:
    rem = n % 10
    sum +=rem**3
    n //= 10
print(sum)    
if num == sum:
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")
