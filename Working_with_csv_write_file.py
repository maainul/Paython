import csv
openfile = open('output2.csv', 'w', newline='')
ouputwriter = csv.writer(openfile)
ouputwriter.writerow(['span', 'eggs', 'bacon', 'ham'])
ouputwriter.writerow(['Hello,world', 'eggs', 'bacon', 'ham'])
openfile.close()

