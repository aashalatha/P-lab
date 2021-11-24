num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 > num2:
    small = num1
else:
    small = num2

for i in range(1,small):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD of",num1,"and",num2,"is:",gcd)

