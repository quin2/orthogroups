import sys #allows print on blank line
import time #tracks exec time between platforms
import re #regex parsing
from Bio import SeqIO #FASTA parsing

targetfile = raw_input('enter the file name to look at >')
parsedFile = SeqIO.parse(targetfile, "fasta")

filename = raw_input('enter the desired file name >')
s = open(filename + '_seqlength.tab' , 'w+')
g = open(filename + '_genecount.tab', 'w+')

start = time.time()

print('searching')

#for genecount
g.write('record\tsig_segments\ttotal_length\n')

#for seqlength
s.write('record\tsegment_length\n')

# iritiate through each seq name...
geneCount = 0
totalCount = 0
for record in parsedFile:
    dna = str(record.seq)

    func = re.compile('(?:GAG|CAG|CAA|GAA){10,}')
    matches = re.findall(func, dna)

    if len(matches) > 0:
        lengthSum = 0;
        for match in matches:
            lengthSum += len(match) / 3
            #for seqlength
            s.write(record.id + '\t' + str(len(match) / 3) + '\n')
            print(match)

        #for genecount
        g.write(record.id + '\t' + str(len(matches)) + '\t' + str(lengthSum) + '\n')
        geneCount += 1
    totalCount += 1

sec = time.time() - start
print('')
print('the sequence had %i genes with  significant repeat segments' % geneCount)
print('took %i seconds to run' % sec)
print('transcript length is %i' % totalCount)
