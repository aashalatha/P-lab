a = input("Enter the sentence: ")

l1 = a.split(" ")

for i in range(len(l1)):
    print("Occurence of",l1[i],"is :",l1.count(l1[i]))
