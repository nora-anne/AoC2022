input_file = open('day3_input','r')

#list of all the possible items
all_items = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
             'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
             'Q','R','S','T','U','V','W','X','Y','Z']
#priorities corresponding to items
all_priorities = list(range(1,53))

###find duplicates between compartments
##priority_sum = 0
##for line in input_file:
##    #split the line in equal halves
##    items_num = len(line)-1
##    items_num_half = int(items_num/2)
##    compartment1 = line[:items_num_half]
##    compartment2 = line[items_num_half:-1]
##    #check for an item that appears in both
##    for item in compartment1:
##        if item in compartment2:
##            duplicate = item
##            break
##    #find the priority associated with that item
##    dup_index = all_items.index(duplicate)
##    priority = all_priorities[dup_index]
##
##    priority_sum += priority
##
##print(priority_sum)
##
##input_file.close()

#find item in common between groups of 3 lines
priority_sum = 0
lines_left = True
while lines_left==True:
    #load 3 lines per group
    line1 = input_file.readline()
    line2 = input_file.readline()
    line3 = input_file.readline()
    if line3=='': #make sure ends when reach end of lines
        lines_left = False
        break
    #find unique item in all 3 lines
    for item in line1:
        if item in line2:
            if item in line3:
                duplicate = item
                break
    #find the priority associated with that item
    dup_index = all_items.index(duplicate)
    priority = all_priorities[dup_index]

    priority_sum += priority

print(priority_sum)

input_file.close()
