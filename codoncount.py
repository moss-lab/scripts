#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', type=str, default='fwd-degapped8.txt', help='input degapped filename')
parser.add_argument('-o', type=str, default='codon_count,.txt', help='output codon filename')
codon_list = (126,129,132,135,138)
args = parser.parse_args()
db = args.i
out = args.o
# with open(out, 'w', newline='\n') as writefile:
print('codon_loc' + '\t' +
      'AAA' + '\t' + 'AAC' + '\t' + 'AAG' + '\t' + 'AAU' + '\t' +
      'ACA' + '\t' + 'ACC' + '\t' + 'ACG' + '\t' + 'ACU' + '\t' +
      'AGA' + '\t' + 'AGC' + '\t' + 'AGG' + '\t' + 'AGU' + '\t' +
      'AUA' + '\t' + 'AUC' + '\t' + 'AUG' + '\t' + 'AUU' + '\t' +
      'CAA' + '\t' + 'CAC' + '\t' + 'CAG' + '\t' + 'CAU' + '\t' +
      'CCA' + '\t' + 'CCC' + '\t' + 'CCG' + '\t' + 'CCU' + '\t' +
      'CGA' + '\t' + 'CGC' + '\t' + 'CGG' + '\t' + 'CGU' + '\t' +
      'CUA' + '\t' + 'CUC' + '\t' + 'CUG' + '\t' + 'CUU' + '\t' +
      'GAA' + '\t' + 'GAC' + '\t' + 'GAG' + '\t' + 'GAU' + '\t' +
      'GCA' + '\t' + 'GCC' + '\t' + 'GCG' + '\t' + 'GCU' + '\t' +
      'GGA' + '\t' + 'GGC' + '\t' + 'GGG' + '\t' + 'GGU' + '\t' +
      'GUA' + '\t' + 'GUC' + '\t' + 'GUG' + '\t' + 'GUU' + '\t' +
      'UAA' + '\t' + 'UAC' + '\t' + 'UAG' + '\t' + 'UAU' + '\t' +
      'UCA' + '\t' + 'UCC' + '\t' + 'UCG' + '\t' + 'UCU' + '\t' +
      'UGA' + '\t' + 'UGC' + '\t' + 'UGG' + '\t' + 'UGU' + '\t' +
      'UUA' + '\t' + 'UUC' + '\t' + 'UUG' + '\t' + 'UUU' + '\t' +
      'other\n')
for codon_location in codon_list:
    codon_AAA = 0
    codon_AAC = 0
    codon_AAG = 0
    codon_AAU = 0
    codon_ACA = 0
    codon_ACC = 0
    codon_ACG = 0
    codon_ACU = 0
    codon_AGA = 0
    codon_AGC = 0
    codon_AGG = 0
    codon_AGU = 0
    codon_AUA = 0
    codon_AUC = 0
    codon_AUG = 0
    codon_AUU = 0
    codon_CAA = 0
    codon_CAC = 0
    codon_CAG = 0
    codon_CAU = 0
    codon_CCA = 0
    codon_CCC = 0
    codon_CCG = 0
    codon_CCU = 0
    codon_CGA = 0
    codon_CGC = 0
    codon_CGG = 0
    codon_CGU = 0
    codon_CUA = 0
    codon_CUC = 0
    codon_CUG = 0
    codon_CUU = 0
    codon_GAA = 0
    codon_GAC = 0
    codon_GAG = 0
    codon_GAU = 0
    codon_GCA = 0
    codon_GCC = 0
    codon_GCG = 0
    codon_GCU = 0
    codon_GGA = 0
    codon_GGC = 0
    codon_GGG = 0
    codon_GGU = 0
    codon_GUA = 0
    codon_GUC = 0
    codon_GUG = 0
    codon_GUU = 0
    codon_UAA = 0
    codon_UAC = 0
    codon_UAG = 0
    codon_UAU = 0
    codon_UCA = 0
    codon_UCC = 0
    codon_UCG = 0
    codon_UCU = 0
    codon_UGA = 0
    codon_UGC = 0
    codon_UGG = 0
    codon_UGU = 0
    codon_UUA = 0
    codon_UUC = 0
    codon_UUG = 0
    codon_UUU = 0
    error_count = 0
    with open(db, 'r') as readfile:
        lines = readfile.readlines()
        for line in lines:
            if line.startswith('>'):
                pass
            else:
                if line[codon_location - 1:codon_location + 2] == 'AAA':
                    codon_AAA += 1
                elif line[codon_location - 1:codon_location + 2] == 'AAC':
                    codon_AAC += 1
                elif line[codon_location - 1:codon_location + 2] == 'AAG':
                    codon_AAG += 1
                elif line[codon_location - 1:codon_location + 2] == 'AAU':
                    codon_AAU += 1
                elif line[codon_location - 1:codon_location + 2] == 'ACA':
                    codon_ACA += 1
                elif line[codon_location - 1:codon_location + 2] == 'ACC':
                    codon_ACC += 1
                elif line[codon_location - 1:codon_location + 2] == 'ACG':
                    codon_ACG += 1
                elif line[codon_location - 1:codon_location + 2] == 'ACU':
                    codon_ACU += 1
                elif line[codon_location - 1:codon_location + 2] == 'AGA':
                    codon_AGA += 1
                elif line[codon_location - 1:codon_location + 2] == 'AGC':
                    codon_AGC += 1
                elif line[codon_location - 1:codon_location + 2] == 'AGG':
                    codon_AGG += 1
                elif line[codon_location - 1:codon_location + 2] == 'AGU':
                    codon_AGU += 1
                elif line[codon_location - 1:codon_location + 2] == 'AUA':
                    codon_AUA += 1
                elif line[codon_location - 1:codon_location + 2] == 'AUC':
                    codon_AUC += 1
                elif line[codon_location - 1:codon_location + 2] == 'AUG':
                    codon_AUG += 1
                elif line[codon_location - 1:codon_location + 2] == 'AUU':
                    codon_AUU += 1
                elif line[codon_location - 1:codon_location + 2] == 'CAA':
                    codon_CAA += 1
                elif line[codon_location - 1:codon_location + 2] == 'CAC':
                    codon_CAC += 1
                elif line[codon_location - 1:codon_location + 2] == 'CAG':
                    codon_CAG += 1
                elif line[codon_location - 1:codon_location + 2] == 'CAU':
                    codon_CAU += 1
                elif line[codon_location - 1:codon_location + 2] == 'CCA':
                    codon_CCA += 1
                elif line[codon_location - 1:codon_location + 2] == 'CCC':
                    codon_CCC += 1
                elif line[codon_location - 1:codon_location + 2] == 'CCG':
                    codon_CCG += 1
                elif line[codon_location - 1:codon_location + 2] == 'CCU':
                    codon_CCU += 1
                elif line[codon_location - 1:codon_location + 2] == 'CGA':
                    codon_CGA += 1
                elif line[codon_location - 1:codon_location + 2] == 'CGC':
                    codon_CGC += 1
                elif line[codon_location - 1:codon_location + 2] == 'CGG':
                    codon_CGG += 1
                elif line[codon_location - 1:codon_location + 2] == 'CGU':
                    codon_CGU += 1
                elif line[codon_location - 1:codon_location + 2] == 'CUA':
                    codon_CUA += 1
                elif line[codon_location - 1:codon_location + 2] == 'CUC':
                    codon_CUC += 1
                elif line[codon_location - 1:codon_location + 2] == 'CUG':
                    codon_CUG += 1
                elif line[codon_location - 1:codon_location + 2] == 'CUU':
                    codon_CUU += 1
                elif line[codon_location - 1:codon_location + 2] == 'GAA':
                    codon_GAA += 1
                elif line[codon_location - 1:codon_location + 2] == 'GAC':
                    codon_GAC += 1
                elif line[codon_location - 1:codon_location + 2] == 'GAG':
                    codon_GAG += 1
                elif line[codon_location - 1:codon_location + 2] == 'GAU':
                    codon_GAU += 1
                elif line[codon_location - 1:codon_location + 2] == 'GCA':
                    codon_GCA += 1
                elif line[codon_location - 1:codon_location + 2] == 'GCC':
                    codon_GCC += 1
                elif line[codon_location - 1:codon_location + 2] == 'GCG':
                    codon_GCG += 1
                elif line[codon_location - 1:codon_location + 2] == 'GCU':
                    codon_GCU += 1
                elif line[codon_location - 1:codon_location + 2] == 'GGA':
                    codon_GGA += 1
                elif line[codon_location - 1:codon_location + 2] == 'GGC':
                    codon_GGC += 1
                elif line[codon_location - 1:codon_location + 2] == 'GGG':
                    codon_GGG += 1
                elif line[codon_location - 1:codon_location + 2] == 'GGU':
                    codon_GGU += 1
                elif line[codon_location - 1:codon_location + 2] == 'GUA':
                    codon_GUA += 1
                elif line[codon_location - 1:codon_location + 2] == 'GUC':
                    codon_GUC += 1
                elif line[codon_location - 1:codon_location + 2] == 'GUG':
                    codon_GUG += 1
                elif line[codon_location - 1:codon_location + 2] == 'GUU':
                    codon_GUU += 1
                elif line[codon_location - 1:codon_location + 2] == 'UAA':
                    codon_UAA += 1
                elif line[codon_location - 1:codon_location + 2] == 'UAC':
                    codon_UAC += 1
                elif line[codon_location - 1:codon_location + 2] == 'UAG':
                    codon_UAG += 1
                elif line[codon_location - 1:codon_location + 2] == 'UAU':
                    codon_UAU += 1
                elif line[codon_location - 1:codon_location + 2] == 'UCA':
                    codon_UCA += 1
                elif line[codon_location - 1:codon_location + 2] == 'UCC':
                    codon_UCC += 1
                elif line[codon_location - 1:codon_location + 2] == 'UCG':
                    codon_UCG += 1
                elif line[codon_location - 1:codon_location + 2] == 'UCU':
                    codon_UCU += 1
                elif line[codon_location - 1:codon_location + 2] == 'UGA':
                    codon_UGA += 1
                elif line[codon_location - 1:codon_location + 2] == 'UGC':
                    codon_UGC += 1
                elif line[codon_location - 1:codon_location + 2] == 'UGG':
                    codon_UGG += 1
                elif line[codon_location - 1:codon_location + 2] == 'UGU':
                    codon_UGU += 1
                elif line[codon_location - 1:codon_location + 2] == 'UUA':
                    codon_UUA += 1
                elif line[codon_location - 1:codon_location + 2] == 'UUC':
                    codon_UUC += 1
                elif line[codon_location - 1:codon_location + 2] == 'UUG':
                    codon_UUG += 1
                elif line[codon_location - 1:codon_location + 2] == 'UUU':
                    codon_UUU += 1
                else:
                    error_count += 1
    print(str(codon_location) + '\t' +
          str(codon_AAA) + '\t' + str(codon_AAC) + '\t' + str(codon_AAG) + '\t' + str(codon_AAU) + '\t' +
          str(codon_ACA) + '\t' + str(codon_ACC) + '\t' + str(codon_ACG) + '\t' + str(codon_ACU) + '\t' +
          str(codon_AGA) + '\t' + str(codon_AGC) + '\t' + str(codon_AGG) + '\t' + str(codon_AGU) + '\t' +
          str(codon_AUA) + '\t' + str(codon_AUC) + '\t' + str(codon_AUG) + '\t' + str(codon_AUU) + '\t' +
          str(codon_CAA) + '\t' + str(codon_CAC) + '\t' + str(codon_CAG) + '\t' + str(codon_CAU) + '\t' +
          str(codon_CCA) + '\t' + str(codon_CCC) + '\t' + str(codon_CCG) + '\t' + str(codon_CCU) + '\t' +
          str(codon_CGA) + '\t' + str(codon_CGC) + '\t' + str(codon_CGG) + '\t' + str(codon_CGU) + '\t' +
          str(codon_CUA) + '\t' + str(codon_CUC) + '\t' + str(codon_CUG) + '\t' + str(codon_CUU) + '\t' +
          str(codon_GAA) + '\t' + str(codon_GAC) + '\t' + str(codon_GAG) + '\t' + str(codon_GAU) + '\t' +
          str(codon_GCA) + '\t' + str(codon_GCC) + '\t' + str(codon_GCG) + '\t' + str(codon_GCU) + '\t' +
          str(codon_GGA) + '\t' + str(codon_GGC) + '\t' + str(codon_GGG) + '\t' + str(codon_GGU) + '\t' +
          str(codon_GUA) + '\t' + str(codon_GUC) + '\t' + str(codon_GUG) + '\t' + str(codon_GUU) + '\t' +
          str(codon_UAA) + '\t' + str(codon_UAC) + '\t' + str(codon_UAG) + '\t' + str(codon_UAU) + '\t' +
          str(codon_UCA) + '\t' + str(codon_UCC) + '\t' + str(codon_UCG) + '\t' + str(codon_UCU) + '\t' +
          str(codon_UGA) + '\t' + str(codon_UGC) + '\t' + str(codon_UGG) + '\t' + str(codon_UGU) + '\t' +
          str(codon_UUA) + '\t' + str(codon_UUC) + '\t' + str(codon_UUG) + '\t' + str(codon_UUU) + '\t' +
          str(error_count) + '\n')
        # writefile.writelines(str(row).replace("'","").strip('[').strip(']').split(','))
        # writefile.writelines('\n')
