import csv
with open("username.csv", "r") as csvfile:
 data = csv.DictReader(csvfile, delimiter=";")
 
 print("Identifier Username")
 print("---------------------------------")
 for row in data:
   print(row[' Identifier'], row['Username'])