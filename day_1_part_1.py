# Split file into tuples then sort
with open('Assets/day_1_input.txt') as file:
    array1, array2 = zip(*(map(int, line.split()) for line in file))

array1 = tuple(sorted(array1))
array2 = tuple(sorted(array2))

# Calculate the total difference
difference = sum(abs(a - b) for a, b in zip(array1, array2))

print('Difference:', difference)
