from collections import Counter

# Split file into tuples
with open('day_1_input.txt') as file:
    array1, array2 = zip(*(map(int, line.split()) for line in file if line.strip()))

# Count occurrences of each value in array2
count_array2 = Counter(array2)

# Calculate total appearances
appearances = sum(value1 * count_array2[value1] for value1 in array1)

print('Appearances:', appearances)
