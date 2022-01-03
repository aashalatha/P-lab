string = input("Enter a string:")
str2 = input("Enter second string:")

str3 = str2[:2]+str1[2:]+" "+str1[:2]+str2[2:]
print(str3)
