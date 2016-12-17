outlierFile = open('outlier_protein_table.txt', 'r')
outlierDNA = open('outlier_DNA_table.txt', 'r')
expectFile = open('mono_protein_frequency.txt','r')
expectDNA = open('mono_DNA_frequency.txt','r')

newFile = open('test_protein.txt','w')
newDNA = open('test_DNA.txt','w')

total_dipeptide = 534628
total_dipeptide1 = 660017
total_dipeptide2 = 58354
total_dipeptide3 = 568358
total_dipeptide4 = 271111
total_dinucleotide = 1766189

observe = outlierFile.readlines()
observe_dna = outlierDNA.readlines()

expect = expectFile.readlines()
expect_dna = expectDNA.readlines()
mono_search = {}
mono_dna_search = {}
for eline in expect:
    newline = eline.split('  ')
    mono_search[newline[0]] = float(newline[2])
print(mono_search)
print(observe)

for dline in expect_dna:
    newline_d = dline.split('  ')
    mono_dna_search[newline_d[0]] = float(newline_d[2])
print(mono_dna_search)
new = []
new_dna = []
# do the observe vs expect for protein
for line in observe:
    if line[0].isalpha():
        expect_value = mono_search[line[0]] * mono_search[line[1]] * total_dipeptide
        newline = line[:-1] + '     '+str(expect_value)
        new.append(newline)
    else:
        new.append(line)
print(new)
newFile.write('\n'.join(new))
newFile.close()
# do the observe vs expect for DNA
print(observe_dna)
for line_d in observe_dna:
    if line_d[0].isalpha():
        expect_value_d = mono_dna_search[line_d[0]] * mono_dna_search[line_d[1]] * total_dinucleotide
        newline_d = line_d[:-1] + '     '+str(expect_value_d)
        new_dna.append(newline_d)
    else:
        new_dna.append(line_d)
print(new_dna)
newDNA.write('\n'.join(new_dna))
newDNA.close()
