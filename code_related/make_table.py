me = 'nucleotide_frequency.txt'
neighbor1 = '0724_DNA_frequency.txt'
neighbor2 = '2390_DNA_frequency.txt'
neighbor3 = '2987_DNA_frequency.txt'
neighbor4 = '8971_DNA_frequency.txt'
DNA_table = 'DNA_table.txt'
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
print(data_me)
table = ['  me  0724    2390    2987    8971    ']
for line in data_me:
