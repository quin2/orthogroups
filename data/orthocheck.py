#import CSV and two TSVs for ortho file and both species
#for each line....
    #check if each seq exisits for each thing mentioned in the ortho file,
    #if so, move to other file, if not ignoreself.

#now turn it into one long regex string, sieve, and output!

import csv

targetfile1 = raw_input('enter the file for the species 1 output file>')
targetfile2 = raw_input('enter the file for the species 2 output file>')
orthoFileTarget = raw_input('enter the file for the ortho file!>')

file1 = open(targetfile1, 'rb')
reader1 = csv.reader(file1, delimiter='\t')

file2 = open(targetfile2, 'rb')
reader2 = csv.reader(file2, delimiter='\t')

orthoFile = open(orthoFileTarget, 'rb')
orthoReader = csv.reader(orthoFile)

#parse file1 and file2 into 2d arrays
onelist = []
for row in reader1:
    onelist.append(row[0])

twolist = []
for row in reader2:
    twolist.append(row[0])

orthoList = []

for row in orthoReader:
    for item in row:
        orthoGroup = []
        smallList = item.split('\t')
        for smallItem in smallList:
            if smallItem in onelist or item in twolist:
                orthoGroup.append(smallItem)
        if len(orthoGroup) > 0:
            orthoList.append(orthoGroup)

print(orthoList)

with open("orthoOverlap.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(orthoList)
