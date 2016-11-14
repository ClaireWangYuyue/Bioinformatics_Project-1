import pprint
file = open('parsed_sequence.txt','r')
frequency = open('protein_frequency.txt','w')
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
saved_string = ''
for key in pair_table:
    saved_string += (key+' : '+str(pair_table[key])+'\n')
frequency.write(saved_string)



