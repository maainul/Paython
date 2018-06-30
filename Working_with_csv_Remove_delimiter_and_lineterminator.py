import csv
openfile = open('output3.csv', 'w', newline='')
ouputwriter = csv.writer(openfile, delimiter='\t', lineterminator='\n\n')
ouputwriter.writerow(['span', 'eggs', 'bacon', 'ham'])
ouputwriter.writerow(['Hello,world', 'eggs', 'bacon', 'ham'])
openfile.close()

