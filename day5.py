input_file = open('day5_input','r')

###crates are moved one at a time
###get the initial configuration of the columns
##columns = [[] for i in range(9)]
##for line in input_file:
##    #stop reading before reaching instructions
##    if line[0]!='[':
##        break
##    #add the letters to the right lists
##    for i in range(9):
##        if line[4*i]=='[':
##            columns[i].append(line[4*i+1])
##
##for line in input_file:
##    if line[0]=='m':
##        #index moving to
##        destination = int(line[-2])-1
##        #index moving from
##        source = int(line[-7])-1
##        #for 1-digit numbers of crates to move
##        if len(line)==19:
##            move_number = int(line[5])
##        #for 2-digit numbers of crates to move
##        elif len(line)==20:
##            move_number = int(line[5:7])
##        #get the letter to move and remove it from the source and add to destination
##        #add to destination at the beginning of list ("top" of stack)
##        for i in range(move_number):
##            move_letter = columns[source][0]
##            columns[source].remove(move_letter)
##            columns[destination].insert(0, move_letter)
##
##for i in range(9):
##    print(columns[i][0])
##
##input_file.close()

#crates are moved all at a time
#get the initial configuration of the columns
columns = [[] for i in range(9)]
for line in input_file:
    #stop reading before reaching instructions
    if line[0]!='[':
        break
    #add the letters to the right lists
    for i in range(9):
        if line[4*i]=='[':
            columns[i].append(line[4*i+1])

for line in input_file:
    if line[0]=='m':
        #index moving to
        destination = int(line[-2])-1
        #index moving from
        source = int(line[-7])-1
        #for 1-digit numbers of crates to move
        if len(line)==19:
            move_number = int(line[5])
        #for 2-digit numbers of crates to move
        elif len(line)==20:
            move_number = int(line[5:7])
        #get the letter to move and remove it from the source and add to destination
        #add to destination just after the previous crate (ie insertion index iterates)
        for i in range(move_number):
            move_letter = columns[source][0]
            columns[source].remove(move_letter)
            columns[destination].insert(i, move_letter)

for i in range(9):
    print(columns[i][0])

input_file.close()
