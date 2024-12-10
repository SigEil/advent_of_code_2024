# Global difference counter
difference = 0

# Create lists from input to do operations
with open ('Assets/day_1_input.txt') as file:
    array1, array2 = zip(*(map(int, line.split()) for line in file))

array1 = list(array1)
array2 = list(array2)

array1.sort()
array2.sort()

# Add the differences
for i in range(len(array1)):
    if array1[i] > array2[i]:
        difference += (array1[i] - array2[i])
    else:
        difference += (array2[i] - array1[i])

print('Difference: ', difference)
