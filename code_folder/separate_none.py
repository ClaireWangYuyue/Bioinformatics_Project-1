ori_table = open('protein_table.txt','r')
protein_valid_table = open('dipeptide_table.txt','w')
protein_none_table = open('none_table.txt','w')
alldata = ori_table.readlines()
ori_table.close()
valid_table = []
none_table = []
for line in alldata:
    if 'None' in line:
        none_table.append(line)
    else:
        valid_table.append(line)
protein_valid_table.write(''.join(valid_table))
protein_none_table.write(''.join(none_table))
protein_valid_table.close()
protein_none_table.close()
