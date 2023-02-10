#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
"""
To run:
python bpcount.py -fa test.fa -dot dot.dot -out1 degapped.txt -out2 bpcount.txt

Default:
python bpcount.py
Runs a test file called "test.fa" and a dot file named "dot.dot", then outputs "bpcount.txt"

-Snake
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i',type=str,default='test.txt',help='input degapped filename')
parser.add_argument('-o',type=str,default='count.txt',help='input degapped filename')

args = parser.parse_args()
db = args.i
out = args.o

with open(out,'w',newline='\n') as writefile:
    ntcount = [['nt','A','C','G','U']]
    with open(db,'r') as readfile:
        firstpass = True
        lines = readfile.readlines()
        for line in lines:
            if line.startswith('>'):
                pass
            else:
                if firstpass == True:
                    for nt_num in range(len(line)):
                        if line[nt_num] == ('A'):
                            ntcount.append([int(nt_num)+1,1,0,0,0])
                        if line[nt_num] == ('C'):
                            ntcount.append([int(nt_num)+1,0,1,0,0])
                        if line[nt_num] == ('G'):
                            ntcount.append([int(nt_num)+1,0,0,1,0])
                        if line[nt_num] == ('U'):
                            ntcount.append([int(nt_num)+1,0,0,0,1])
                    #print(ntcount)
                    firstpass = False
                else:
                    try:
                        for nt_num in range(len(line)):
                            nt_value = ntcount[int(nt_num)+1]
                            #print(nt_values)
                            nt_name =  nt_value[0]
                            nt_A = nt_value[1]
                            nt_C = nt_value[2]
                            nt_G = nt_value[3]
                            nt_U = nt_value[4]
                            if line[nt_num] == ('A'):
                                nt_A += 1
                            if line[nt_num] == ('C'):
                                nt_C += 1
                            if line[nt_num] == ('G'):
                                nt_G += 1
                            if line[nt_num] == ('U'):
                                nt_U += 1
                            ntcount[int(nt_num)+1] = [nt_name,nt_A,nt_C,nt_G,nt_U]
                    except:
                        pass
    for row in ntcount:
        writefile.writelines(str(row).replace("'","").strip('[').strip(']').split(','))
        writefile.writelines('\n')
