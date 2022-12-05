input_file = open('day2_input','r')

#if XYZ are RPS 
total_score = 0
for line in input_file:
    them = line[0]
    me = line[2]
    #add points based on my choice
    if me=='X':
        total_score +=1
    if me=='Y':
        total_score +=2
    if me=='Z':
        total_score +=3

    #add points for draws
    if (them=='A' and me=='X') or \
       (them=='B' and me=='Y') or (them=='C' and me=='Z'):
        total_score +=3
    #add points for wins
    if (them=='A' and me=='Y') or \
       (them=='B' and me=='Z') or (them=='C' and me=='X'):
        total_score +=6
     
print(total_score)

input_file.close()

input_file = open('day2_input','r')

#if XYZ are LDW
total_score = 0
for line in input_file:
    them = line[0]
    outcome = line[2]
    #if losing
    if outcome=='X':
        if them=='A':
            me = 'Z'
        if them=='B':
            me = 'X'
        if them=='C':
            me = 'Y'
    #if drawing
    if outcome=='Y':
        total_score +=3
        if them=='A':
            me = 'X'
        if them=='B':
            me = 'Y'
        if them=='C':
            me = 'Z'
    #if winning
    if outcome=='Z':
        total_score +=6
        if them=='A':
            me = 'Y'
        if them=='B':
            me = 'Z'
        if them=='C':
            me = 'X'
    #add points based on my choice
    if me=='X':
        total_score +=1
    if me=='Y':
        total_score +=2
    if me=='Z':
        total_score +=3

print(total_score)

input_file.close()
