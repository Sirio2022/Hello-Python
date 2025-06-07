billboard_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    ]

for i in range(len(billboard_matrix)):
    billboard_matrix[i] = billboard_matrix[i][::-1]  # Reversing each row

print(billboard_matrix)



# Sorting a list of platforms in ascending order for the first four elements
platforms = [3, 1, 2 , 0, 4, 5, 6, 7]

platforms[:4] = sorted(platforms[:4]) # Sorting the first four elements in ascending order

# platforms[0] = 0
# platforms[3] = 3

print(platforms)


# Modifying power levels based on conditions
# and calculating the total power
power_levels = [10, 12, 27.5, 16, 40]

for i in range(len(power_levels)):
    if power_levels[i] < 10:
        power_levels[i] *= 2
    elif power_levels[i] > 50:
        power_levels[i] /= 2

total_power = sum(power_levels)
print("Total Power:", total_power)


# Calculating total energy from a matrix
energy_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

total_enerygy = 0

for i in energy_matrix:
    for value in i:
        total_enerygy += value
print("Total Energy:", total_enerygy)

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data_list.remove(
    5  # Removing the element 5 from the list
)
