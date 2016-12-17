file = open('parsed_sequence.txt','r') # change file name to 'protein_sequence.txt' for protein
mono = open('mono_DNA_frequency.txt','w') # change file name to 'mono_protein_frequency.txt' for protein
alldata = file.read()
file.close()
mydic = {}
for letter in alldata:
    if letter.isalpha():
        if letter not in mydic:
            mydic[letter] = 1
        else:
            mydic[letter] += 1
sorted_key = sorted(mydic.keys())
total = sum(mydic.values())
print('in total:',len(sorted_key))
for key in sorted_key:
    mono.write(key+'  '+str(mydic[key])+'   '+str(mydic[key]/total)+'\n')
mono.close()