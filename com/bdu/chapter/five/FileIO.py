import pandas

academic = open("/home/mayank-ideata/setup/sampledata/academic.tcv" , "r")



csv = pandas.read_csv("/home/mayank-ideata/setup/sampledata/circular.csv")

print csv

#excel = pandas.read_excel("/home/mayank-ideata/setup/sampledata/Motor_Revised.xls")

#print excel


lines =  academic.read().split()

for line in lines:
   # for l in line.split():
        print line


academic.close()