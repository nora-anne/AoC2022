input_file = open('day4_input','r')

###find how many pairs fully overlap
##full_duplicates = 0
##for line in input_file:
##    #use comma to break into two range
##    range1 = line.split(',')[0]
##    range2 = line.split(',')[1][:-1]
##    #use hyphen to get min max of range
##    range1_min = int(range1.split('-')[0])
##    range1_max = int(range1.split('-')[1])
##    range2_min = int(range2.split('-')[0])
##    range2_max = int(range2.split('-')[1])
##
##    #check if either range encompasses the other range
##    if (range1_min<=range2_min and range1_max>=range2_max) or \
##       (range1_min>=range2_min and range1_max<=range2_max):
##        full_duplicates +=1
##
##print(full_duplicates)
##
##input_file.close()

#find how many pairs partially overlap
some_duplicates = 0
for line in input_file:
    #use comma to break into two range
    range1 = line.split(',')[0]
    range2 = line.split(',')[1][:-1]
    #use hyphen to get min max of range
    range1_min = int(range1.split('-')[0])
    range1_max = int(range1.split('-')[1])
    range2_min = int(range2.split('-')[0])
    range2_max = int(range2.split('-')[1])

    #check if either range overlaps the other range
    if (range1_min>=range2_min and range1_min<=range2_max) or \
       (range2_min>=range1_min and range2_min<=range1_max):
        some_duplicates +=1

print(some_duplicates)

input_file.close()
