import os
from Bio import SeqIO
from Bio.Seq import transcribe

def fwdcomp(filename):
    with open(filename,'r') as readfile:
        with open("fwd-"+filename,'w',newline='\n') as rev:
            for record in SeqIO.parse(readfile, 'fasta'):
                rev.writelines('>'+record.id+'\n')
                rna = record.seq.transcribe()
                rev.writelines(rna)

current_directory = os.getcwd()
all_files = os.listdir(current_directory)
for filename in all_files:
    if filename.endswith('.txt'):
        fwdcomp(filename)
