import csv
examplefile = open('example.csv')
exampleReader = csv.reader(examplefile)
for i in exampleReader:
    print(str(i))
