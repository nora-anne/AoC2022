input_file = open('day1_input.txt')

#find the calories each elf is carrying
calories_per_elf = []
calories = 0
for line in input_file:
    try:
        val = float(line) #converts line to float
        calories += val
    except:
        #cannot convert blank line to float
        #blank lines mean that elf is done
        #append to list and reset calories for next elf
        calories_per_elf.append(calories)
        calories = 0
        continue
input_file.close()

#find how many calories are being carried by the elf with the most
print(max(calories_per_elf))

#find how many calories are being carried by the 3 elves with the most
max1 = max(calories_per_elf)
calories_per_elf.remove(max1)

max2 = max(calories_per_elf)
calories_per_elf.remove(max2)

max3 = max(calories_per_elf)

print(max1+max2+max3)
