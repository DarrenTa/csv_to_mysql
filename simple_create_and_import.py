#!./venv/bin/python3

import csv
import sys
import sqlite3

def return_type(fieldname):
	print("1) INTEGER")
	print("2) TEXT")
	print("3) REAL")
	print("4) DATE")
	print("5) BLOB")
	fieldnum = input("Which data type is the field: "+fieldname+"?")
	if fieldnum == "1":
		print("You pressed 1")
		return "INTEGER"
	elif fieldnum == "2":
		print("You pressed 2")
		return "TEXT"
	elif fieldnum == "3":
		print("You pressed 3")
		return "REAL"
	elif fieldnum == "4":
		print("You pressed 4, note SQLite stores dates as integers")
		return "DATE"
	elif fieldnum == "5":
		print("You pressed 5")
		return "BLOB"
	else:
		print("Response not understood")
		return return_type(fieldname)



file=open(sys.argv[1])

contents = csv.reader(file)

readin = []

for row in contents:
	readin.append(row)

print(readin[0])

print(readin[0][0])

print(len(readin[0]))

for k in range(0,len(readin[0])):
	names = readin[0]
	change = True
	while change:
		useri = input('One field heading is "' +names[k] +'" would you like to change it?(y/n)')
		if useri == "y":
			changeto = input('What would you like the filed name to be?\n')
			names[k] = changeto
		elif useri == "n":
			change = False
		else:
			print("response not understood")

print(names)

datatypes = []


for k in range(0,len(names)):
	print("One field name ",names[k]," has first few entries:")
	disp = min(6,len(readin))-1
	for l in range(0,disp):
		print(readin[l+1][k])
	datatypes.append(return_type(names[k]))
#print(datatypes)


print("Going to create a table with the following field names || type")
for k in range(0,len(names)):
	print(k+1,") ",names[k]," || ",datatypes[k])

create_table = '''CREATE TABLE Master(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		'''
for k in range(0,len(names)-1):
	create_table = create_table + names[k] + " " + datatypes[k]+",\n\t\t"

create_table = create_table + names[len(names)-1]+" "+datatypes[len(names)-1]+");"

print(create_table)

connection = sqlite3.connect('data/main.db')

cursor = connection.cursor()

cursor.execute(create_table)

sql_insert_query= "INSERT INTO Master(\n"

for k in range(0,len(names)-1):
	sql_insert_query = sql_insert_query + names[k]+",\n"

sql_insert_query = sql_insert_query + names[len(names)-1] + ")\nVALUES(?"

for k in range(0,len(names)-1):
	sql_insert_query = sql_insert_query + ",?"

sql_insert_query = sql_insert_query + ")"

print(sql_insert_query)

for k in range(1,len(readin)):
	cursor.execute(sql_insert_query,readin[k])

connection.commit()

