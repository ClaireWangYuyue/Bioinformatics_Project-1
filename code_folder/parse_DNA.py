# use different matched sequence/new name for different species
sequence = 'project_sequence.txt'
# sequence = 'CP002987_DNA.txt'
# sequence = 'AP008971_DNA.txt'
# sequence = 'CP002390_DNA.txt'
# sequence = 'CP000724_DNA.txt'
test = 'test.txt' # just for testing
new = 'parsed_CP002987_DNA.txt'
# new = 'parsed_sequence.txt'
# new = 'parsed_AP008971_DNA.txt'
# new = 'parsed_CP002390_DNA.txt'
# new = 'parsed_CP000724_DNA.txt'
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
        if i.isalpha():
            new_line += i
    stripped_new_line = new_line.strip()
    sequence_lines.append(stripped_new_line)
new_sequence = '\n'.join(sequence_lines)
new_file.write(new_sequence)
new_file.close()