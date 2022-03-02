import csv

a_file = open("sample.csv", "w")
a_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

writer = csv.writer(a_file)
for key, value in a_dict.items():
    writer.writerow([key, value])

a_file.close()


with open("sample.csv", "r") as a_file:
  data = csv.reader(a_file, delimiter=" ")

  for row in data:
    print(row)
 