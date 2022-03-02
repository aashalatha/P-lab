import csv
h=[]

with open("username.csv", "r") as csvfile:
  data = csv.reader(csvfile, delimiter=";")
  h=next(data)
  print(h)
  for row in data:
    print(row)
    print(" ".join(row))
    