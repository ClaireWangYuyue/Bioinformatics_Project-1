observeFile = open('nucleotide_frequency.txt', 'r')
expectFile = open('mono_DNA_frequency.txt','r')
newFile = open('DNA_OE_comparison.txt','w')

observe = observeFile.readlines()
expect = expectFile.readlines()
observeFile.close()
expectFile.close()
mono_search = {}
for eline in expect:
    newline = eline.split('  ')
    mono_search[newline[0]] = float(newline[2])
    #print(newline)
print(mono_search)

comparison = []
for line in observe:
    myline = []
    splitline = line.split('   ')
    for item in splitline:
        myline.append(item.strip(''))
    print(myline)
    if myline[0].isalpha():
        addline = [myline[0],myline[2]]
        expectfre1 = mono_search[myline[0][0]]
        expectfre2 = mono_search[myline[0][1]]
        #print (expectfre1,expectfre2)
        addline.insert(1,str(expectfre1*expectfre2))
        comparison.append(addline)

print(comparison)
#output = ['dipeptide expect observe\n'] # 先expect再observe
output = []
for i in comparison:
    output.append(' '.join(i))
newFile.write(''.join(output))