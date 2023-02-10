"""
bpcount.py takes a list of MAFFT-aligned fasta files and a dot bracket file and outputs a base pair count file.

To run:
python bpcount.py -fa test.fa -dot dot.dot -out1 degapped.txt -out2 bpcount.txt

Default:
python bpcount.py
Runs a test file called "test.fa" and a dot file named "dot.dot", then outputs "bpcount.txt"

WIP:
Odd workaround to get first bp to output properly. Does the dot bracket count, then asks if this is first and last.

-Snake
"""

import os
import argparse
from Bio import SeqIO
from Bio.Seq import transcribe

parser = argparse.ArgumentParser()
parser.add_argument('-fa', type=str, default='test.fa', help='input fasta filename')
parser.add_argument('-dot', type=str, default='dot.dot', help='input dot bracket filename')
parser.add_argument('-out1', type=str, default='degapped.txt', help='output degapped filename')
parser.add_argument('-out2', type=str, default='bpcount.txt', help='output bpcount filename')

args = parser.parse_args()
filename = args.fa
dbn = args.dot
output1 = args.out1
output2 = args.out2

print('Alignment in progress...')
with open(filename, 'r') as fasta:
    with open('temp.txt', 'w') as tempoutput:
        for record in SeqIO.parse(fasta, 'fasta'):
            rna = record.seq.transcribe()
            tempoutput.writelines('>' + record.id + '\n')
            tempoutput.writelines(rna + '\n')
    with open('temp.txt', 'r') as tempoutput:
        print('FASTAs aligned, removing gaps...')
        with open(output1, 'w') as output1:
            i = 0
            j = len(rna)
            k = 0
            l = []
            row = tempoutput.readlines()
            m = len(row)
            while k != 0:
                break
            else:
                output1.writelines(row[k])
                k += 1
            while k != 1:
                break
            else:
                for column in row[k]:
                    if i == j:
                        output1.write('\n')
                        k += 1
                        break
                    elif column == '-':
                        l.append(i)
                        #                            print(l)
                        i += 1
                        continue
                    else:
                        output1.write(column)
                        i += 1
                        continue
            while k >= 2 and k < m:
                #                    print(k)
                while k % 2 != 1:
                    #                        print('row = '+row[k]+'\n')
                    output1.writelines(row[k])
                    k += 1
                    break
                else:
                    i = 0
                    for column in row[k]:
                        #                            print('i = '+str(i))
                        #                            print('j = '+str(j))
                        if i == j:
                            #                                print('break')
                            output1.write('\n')
                            k += 1
                            break
                        else:
                            if i in l:
                                i += 1
                                pass
                            else:
                                #                                    print(column)
                                output1.write(column)
                                i += 1
                                continue
            else:
                pass

os.remove('temp.txt')

print('Degap complete, commencing base pair count...')
print('i:j:GC:CG:AU:UA:GU:UG:GA:AG:AA:GG:UU:CC:AC:UC:CA:CU')

with open(dbn, 'r') as dot1:
    with open(dbn, 'r') as dot2:
        with open(output2, 'w') as output2:
            #                print('Files opened, beginning pair count')
            a = 1
            row1 = dot1.readlines()
            row2 = dot2.readlines()
            amax = len(row1[0])
            match = {}
            #                print('a = '+str(a))
            #            print('amax = '+str(amax))
            #                print(row1)
            while a != amax + 1:
                #                print('current a = '+str(a))
                for column1 in row1[0]:
                    if str(column1) != '(':
                        #                        print(column1)
                        a += 1
                    else:
                        #                        print('pair at '+str(a))
                        b = 1
                        count = 1
                        for column2 in row2[0]:
                            #                            print(a)
                            #                            print(b)
                            if b >= amax + 1:
                                #                                print('1')
                                break
                            elif b < a:
                                #                                print('2')
                                b += 1
                            elif b == a:
                                #                                print('3')
                                count = 1
                                b += 1
                            else:
                                #                                print('4')
                                #                                print('a: '+str(a))
                                #                                print('b: '+str(b))
                                if count == 0:
                                    match[a] = b
                                    #                                    print('Beginning count')
                                    # i:j:GC:CG:AU:UA:GU:UG:GA:AG:AA:GG:UU:CC:AC:UC:CA:CU}
                                    i = a  # i
                                    j = match[i]  # j
                                    #                                        bp = [i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
                                    k = 0  # GC
                                    l = 0  # CG
                                    m = 0  # AU
                                    n = 0  # UA
                                    o = 0  # GU
                                    p = 0  # UG
                                    q = 0  # GA
                                    r = 0  # AG
                                    s = 0  # AA
                                    t = 0  # GG
                                    u = 0  # UU
                                    v = 0  # CC
                                    w = 0  # AC
                                    x = 0  # UC
                                    y = 0  # CA
                                    z = 0  # CU
                                    with open(output1, 'r') as degapped:
                                        sequence = SeqIO.parse(degapped, 'fasta')
                                        for record in sequence:
                                            #                                            print(record.seq)
                                            #                                            print('i-'+str(i))
                                            #                                            print('j-'+str(j))
                                            #                                            print(str(record.seq[i-1]+record.seq[j-1]))
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GC':
                                                k += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CG':
                                                l += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AU':
                                                m += 1
                                            #                                                print(m)
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UA':
                                                n += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GU':
                                                o += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UG':
                                                p += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GA':
                                                q += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AG':
                                                r += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AA':
                                                s += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GG':
                                                t += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UU':
                                                u += 1
                                            #                                                print(u)
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CC':
                                                v += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AC':
                                                w += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UC':
                                                x += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CA':
                                                y += 1
                                            if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CU':
                                                z += 1
                                            else:
                                                pass
                                            #                                        print(j)
                                        bp = [i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
                                        print(bp)
                                        output2.writelines(str(bp).strip('[').strip(']').split(','))
                                        output2.writelines('\n')
                                        break
                                else:
                                    if str(column2) == '(':
                                        count += 1
                                        #                                        print('( at b = '+str(b)+' count = '+str(count))
                                        b += 1
                                    elif str(column2) == ')':
                                        if a == 1 and b == amax:  # due to weird bug when first and last are paired
                                            #                                            print('7')
                                            match[a] = b
                                            #                                    print('Beginning count')
                                            # i:j:GC:CG:AU:UA:GU:UG:GA:AG:AA:GG:UU:CC:AC:UC:CA:CU}
                                            i = a  # i
                                            j = match[i]  # j
                                            #                                        bp = [i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
                                            k = 0  # GC
                                            l = 0  # CG
                                            m = 0  # AU
                                            n = 0  # UA
                                            o = 0  # GU
                                            p = 0  # UG
                                            q = 0  # GA
                                            r = 0  # AG
                                            s = 0  # AA
                                            t = 0  # GG
                                            u = 0  # UU
                                            v = 0  # CC
                                            w = 0  # AC
                                            x = 0  # UC
                                            y = 0  # CA
                                            z = 0  # CU
                                            #                                    print(str(i)+','+str(match[i]))
                                            with open(output1, 'r') as degapped:
                                                sequence = SeqIO.parse(degapped, 'fasta')
                                                for record in sequence:
                                                    #                                            print(record.seq)
                                                    #                                            print('i-'+str(i))
                                                    #                                            print('j-'+str(j))
                                                    #                                            print(str(record.seq[i-1]+record.seq[j-1]))
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GC':
                                                        k += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CG':
                                                        l += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AU':
                                                        m += 1
                                                    #                                                print(m)
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UA':
                                                        n += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GU':
                                                        o += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UG':
                                                        p += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GA':
                                                        q += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AG':
                                                        r += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AA':
                                                        s += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'GG':
                                                        t += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UU':
                                                        u += 1
                                                    #                                                print(u)
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CC':
                                                        v += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'AC':
                                                        w += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'UC':
                                                        x += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CA':
                                                        y += 1
                                                    if (str(record.seq[i - 1] + record.seq[j - 1])) == 'CU':
                                                        z += 1
                                                    else:
                                                        pass
                                                        #                                        print(j)
                                                bp = [i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
                                                print(bp)
                                                output2.writelines(str(bp).strip('[').strip(']').split(','))
                                                output2.writelines('\n')
                                                break
                                        else:
                                            count -= 1
                                            #                                        print(') at b = '+str(b)+' count = '+str(count))
                                            if count == 0:
                                                pass
                                            else:
                                                b += 1
                                    elif str(column2) == '.':
                                        #                                        print('no matches at '+str(b))
                                        b += 1
                                        pass
                                    else:
                                        break
                        a += 1
            else:
                pass

print('Base pair count complete!')