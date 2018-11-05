import sys #allows print on blank line
import time #tracks exec time between platforms
from Bio import SeqIO #FASTA parsing

start = time.time()

FILENAME = "Gasterosteus_aculeatus.BROADS1.pep.all.fa"
parsedFile = SeqIO.parse(FILENAME, "fasta")

print('searching')

# iritiate through each seq name...
geneCount = 0
for record in parsedFile:
    dna = record.seq
    dnaLength = len(dna)
    #go through string 3 characters at a time
    repeatCount = 0.0
    masterRepeatCount = 0.0
    for i in xrange(0, dnaLength, 1):
        #once found, start looking for GAG or CAG
        if (dna[i] == 'E' or dna[i] == 'Q'):
            repeatCount += 1.0
            #print("found")
        else:
            if repeatCount >= 5.0:
                masterRepeatCount += 1.0
                sys.stdout.write('|')
                print(repeatCount)
            repeatCount = 0.0

    if masterRepeatCount > 0.0:
        geneCount += 1

sec = time.time() - start
print('')
print('the sequence had %i genes with significant repeat segments' % geneCount)
print('took %i seconds to run' % sec)
