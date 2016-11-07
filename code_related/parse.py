import pprint
sequence = 'project_sequence.txt'
test = 'test.txt'
new = 'parsed_sequence.txt'
file = open(sequence,'r')
new_file = open(new,'w')
alldata = file.readlines()
file.close()
for line in alldata:
    if 'SQ ' in line:
        start = alldata.index(line)
        break
raw_sequence_lines = alldata[start+1:-1]
sequence_lines = []
for line in raw_sequence_lines:
    new_line =''
    for i in line:
        if not i.isalpha() and ord(i) != 32:
            break
        new_line += i
    stripped_new_line = new_line.strip()
    sequence_lines.append(stripped_new_line)
new_sequence = '\n'.join(sequence_lines)
new_file.write(new_sequence)
new_file.close()