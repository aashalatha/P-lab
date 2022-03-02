fn = open('bcd.txt', 'r', encoding="utf-8")
fn1 = open('nfile.txt', 'w', encoding="utf-8")

cont = fn.readlines()

for i in range(0, len(cont)):
	if(i%2 != 0):
		fn1.write(cont[i])
	else:
		pass #do nothing



fn1.close()


fn1 = open("nfile.txt", "r", encoding="utf-8")

cont1 = fn1.read()
print(cont1)


fn.close()
fn1.close()


