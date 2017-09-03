file = open('/home/mayank-ideata/setup/sampledata/employees.csv','row')
print "Name of the file: " , file.name

summary = file.readline()

print "summary : "+summary

file.close

print len(summary[0])

print summary.upper()

print summary.replace(",", "-")

print summary.split("-")
