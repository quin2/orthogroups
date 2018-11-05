import sys #allows print on blank line
import time #tracks exec time between platforms
import re #regex parsing
from Bio import SeqIO #FASTA parsing

targetfile = raw_input('enter the file name to look at > ')
parsedFile = SeqIO.parse(targetfile, "fasta")

filename = raw_input('enter the desired file name and ext > ')
f = open(filename, 'w+')

start = time.time()

#for seqlength
#print('record   segment length')
#f.write('record\tsegment_length\n')

#for genecount
print('record   sig segments    total length')
f.write('record\tsig_segments\ttotal_length\n')

# iritiate through each seq name...
geneCount = 0
for record in parsedFile:
    pro = str(record.seq)

    #significance is Q or E repeat >5 times
    func = re.compile('(?:Q|E){10,}')
    matches = re.findall(func, pro)

    if len(matches) > 0:
        lengthSum = 0
        for match in matches:
            lengthSum += len(match)
            #for seqlength
            #f.write(record.id + '\t' + str(len(match)) + '\n')
            #print(record.id + ' ' + str(len(match)))

        #for genecount
        print(record.id + ' ' + str(len(matches)) + '   ' + str(lengthSum))
        f.write(record.id + '\t' + str(len(matches)) + '\t' + str(lengthSum) + '\n')
        geneCount += 1

sec = time.time() - start
f.close()
print('')
print('the sequence had %i genes with significant repeat segments' % geneCount)
print('took %i seconds to run' % sec)
