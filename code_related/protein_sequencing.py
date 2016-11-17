import pprint
file = open('parsed_AP008971_DNA.txt','r')
frequency = open('8971_DNA_frequency.txt','w')
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
pprint.pprint(pair_table)
string_list = []
for key in pair_table:
    string_list.append(key+'    '+str(pair_table[key]))
string_list.sort()
saved_string = '\n'.join(string_list)
print(saved_string)
frequency.write(saved_string)



