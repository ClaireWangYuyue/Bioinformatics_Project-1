import pprint
# file = open('protein_sequence.txt','r')
# file = open('parsed_AP008971_protein.txt')
# file = open('parsed_CP000724_protein.txt')
# file = open('parsed_CP002390_protein.txt')
file = open('parsed_CP002987_protein.txt')


# frequency = open('protein_frequency_num.txt','w')
# frequency = open('8971_protein_frequency_num.txt','w')
# frequency = open('0724_protein_frequency_num.txt','w')
# frequency = open('2390_protein_frequency_num.txt','w')
frequency = open('2987_protein_frequency_num.txt','w')


alldata = file.read()
file.close()
counter = 0
pair = ''
pair_table = {}
for letter in alldata:
    if not letter.isalpha():
        pass
    else:
        counter += 1
        pair += letter
    if counter == 2:
        if pair not in pair_table:
            pair_table[pair] = 1
        else:
            pair_table[pair] += 1
        counter = 0
        pair = ''
#pairsum = (sum(pair_table.values()))
#for key in pair_table:
#    pair_table[key] = str(pair_table[key])+'    '+str(pair_table[key]/pairsum)
string_list = []
for key in pair_table:
    string_list.append(key+'    '+str(pair_table[key]))
string_list.sort()
saved_string = '\n'.join(string_list)
print(saved_string)
frequency.write(saved_string)


