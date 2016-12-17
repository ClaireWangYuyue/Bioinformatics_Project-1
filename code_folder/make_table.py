me = 'protein_frequency_num.txt'
neighbor1 = '0724_protein_frequency_num.txt'
neighbor2 = '2390_protein_frequency_num.txt'
neighbor3 = '2987_protein_frequency_num.txt'
neighbor4 = '8971_protein_frequency_num.txt'

## attention!! this file can't run again!! 会毁了已有文件!
DNA_table = 'protein_table.txt'
file_me = open(me,'r')
file_n1 = open(neighbor1,'r')
file_n2 = open(neighbor2,'r')
file_n3 = open(neighbor3,'r')
file_n4 = open(neighbor4,'r')
table_file = open(DNA_table,'w')
data_me = file_me.readlines()
data_n1 = file_n1.readlines()
data_n2 = file_n2.readlines()
data_n3 = file_n3.readlines()
data_n4 = file_n4.readlines()
file_me.close()
file_n1.close()
file_n2.close()
file_n3.close()
file_n4.close()
pointer1=0
pointer2=0
pointer3=0
pointer4=0
pointer0=0
table_dic = {}
for line in data_me:
    table_dic[line[:2]] = [line[6:-1], 'None', 'None', 'None', 'None']
for line in data_n1:
    if line[:2] not in table_dic:
        table_dic[line[:2]] = ['None',line[6:-1],'None','None','None']
    else:
        table_dic[line[:2]][1] = line[6:-1]
for line in data_n2:
    if line[:2] not in table_dic:
        table_dic[line[:2]] = ['None','None',line[6:-1],'None','None']
    else:
        table_dic[line[:2]][2] = line[6:-1]
for line in data_n3:
    if line[:2] not in table_dic:
        table_dic[line[:2]] = ['None','None','None',line[6:-1],'None']
    else:
        table_dic[line[:2]][3] = line[6:-1]
for line in data_n4:
    if line[:2] not in table_dic:
        table_dic[line[:2]] = ['None','None','None','None',line[6:-1]]
    else:
        table_dic[line[:2]][4] = line[6:-1]

print(table_dic)
sorted_key = sorted(table_dic.keys())
print('in total:',len(sorted_key))
ToBeAdd = ''
for key in sorted_key:
    data = '    '.join(table_dic[key])
    ToBeAdd += key+'  '+data+'\n'

table_file.write(ToBeAdd)
table_file.close()


