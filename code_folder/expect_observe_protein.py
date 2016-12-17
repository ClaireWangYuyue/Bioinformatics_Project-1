
observeFile = open('observe_frequency_table.txt', 'r')
expectFile = open('mono_protein_frequency.txt','r')
newFile = open('protein_OE_comparison.txt','w')

observe = observeFile.readlines()
expect = expectFile.readlines()
mono_search = {}
for eline in expect:
    newline = eline.split('  ')
    mono_search[newline[0]] = float(newline[2])
    #print(newline)
#print(mono_search)
observeFile.close()
expectFile.close()
comparison = []
for line in observe:
    myline = []
    splitline = line.split(',')
    for item in splitline:
        myline.append(item.strip('"'))
    #print(myline)
    if myline[1].isalpha():
        addline = myline[1:]
        expectfre1 = mono_search[myline[1][0]]
        expectfre2 = mono_search[myline[1][1]]
        #print (expectfre1,expectfre2)
        addline.insert(1,str(expectfre1*expectfre2))
        comparison.append(addline)

print(comparison)
#output = ['dipeptide expect observe\n'] # 先expect再observe
output = []
for i in comparison:
    output.append(' '.join(i))
newFile.write(''.join(output))