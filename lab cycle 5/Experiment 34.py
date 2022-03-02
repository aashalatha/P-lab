text = open("C:/Users/lenovo.LAPTOP-21UER7MJ/OneDrive/Desktop/extra.txt", encoding="utf-8")

d=dict()

for line in text:
	line = line.lower()
	words = line.split(" ")

	
	for word in words:
		# Check if the word is already in dictionary
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1


for key in list(d.keys()):
	print(key, ":", d[key])