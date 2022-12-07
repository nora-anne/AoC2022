input_file = open('day6_input','r')

#load data string
incoming_data = input_file.readline()
input_file.close()

#go through each character and check if the most recent 4 are unique
for i,x in enumerate(incoming_data):
    #skip first 3 since not enough to make a set of 4
    if i<=2:
        continue
    count = 0
    #for each character in the most recent 4, check if any are unique
    for j in range(4):
        subset = incoming_data[i-3:i+1]
        to_check = subset[j]
        subset = subset[:j] + subset[j+1:]
        if to_check in subset:
            #means the character is not unique
            count +=1
    #if no character was not unique, then it's the first set of 4 different
    if count==0:
        #wants the ordinal number not index
        print(i+1)
        break

#go through each character and check if the most recent 14 are unique
for i,x in enumerate(incoming_data):
    #skip first 13 since not enough to make a set of 14
    if i<=12:
        continue
    count = 0
    #for each character in the most recent 14, check if any are unique
    for j in range(14):
        subset = incoming_data[i-13:i+1]
        to_check = subset[j]
        subset = subset[:j] + subset[j+1:]
        if to_check in subset:
            #means the character is not unique
            count +=1
    #if no character was not unique, then it's the first set of 4 different
    if count==0:
        #wants the ordinal number not index
        print(i+1)
        break


