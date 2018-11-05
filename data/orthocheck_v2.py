#find entire OGs with which have AT LEAST 1 select sequence!
from Bio import SeqIO
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

ffile = raw_input('enter the first fasta>')
fasta1 = SeqIO.parse(ffile, "fasta")

ffile2 = raw_input('enter the second fasta>')
fasta2 = SeqIO.parse(ffile2, "fasta")

#parse file1 and file2 into 2d arrays
onelist = []
for row in reader1:
    onelist.append(row[0])

twolist = []
for row in reader2:
    twolist.append(row[0])

for row in orthoReader:
    smallList = []

    for item in row:
        smallList += item.split('\t');

    for smallItem in smallList:
        orthoList = []
        if smallItem in onelist or smallItem in twolist:
            print('match')
            print(smallList)
            #get entire row, turn into fasta file with each seq
            #shit is not blending!!!
            for item in smallList:
                for obj in fasta1:
                    if item in str(obj.id):
                        orthoList.append(obj)
                for obj in fasta2:
                    if item in str(obj.id):
                        orthoList.append(obj)


                #make fasta file for group

            print(orthoList)
            fname = smallList[0] + '.fasta'
                #with open(fname, "w") as output_handle:
                #    SeqIO.write(orthoList, output_handle, "fasta")
