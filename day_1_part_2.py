# Read input file and divide into list from left value and right value
with open('Assets/day_1_input.txt') as file:
    array1, array2 = zip(*(map(int, line.split()) for line in file))

# Go through each line of left list, check how many times it appears in right list
appearances = 0
for index1, value1 in enumerate(array1):
    found_in_array_2 = 0
    for index2, value2 in enumerate(array2):
        if value2 == value1:
            found_in_array_2 += 1
    appearances += (value1 * found_in_array_2)

print('Appearances: ', appearances)