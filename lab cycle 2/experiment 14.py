string = input("Enter a string:")
print("String after replacing:",string[0]+string[1::].replace(string[0],'$'))
