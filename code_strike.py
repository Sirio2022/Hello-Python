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


encrypted_floors = [
    [9, 8, 5, 4],
    [7, 6, 3, 2],
    [4, 5, 6, 3],
    [1, 5, 9, 0]
]

flat_list = []


for row in encrypted_floors:
    for value in row:
        flat_list.append(value)  # Flattening the list by appending each value

# i = 0
# j = len(flat_list) -1
#
# while i <= j:
#     flat_list[i], flat_list[j] = flat_list[j], flat_list[i]  # Swapping elements
#     i += 1
#     j -= 1

flat_list.reverse()  # Reversing the flat list

print("Reversed Flat List:", flat_list)

# Identify the row with the highest production, and bring its production to zero
drone_production = [
    [5, 2, 3, 4],
    [8, 1, 6, 7],
    [3, 9, 2, 5, 9],
    [4, 7, 8, 6]
]

max_production_index = 0
max_production_value = sum(drone_production[0])  # Initialize with the first row's sum

for i in range(1, len(drone_production)):
    current_production_value = sum(drone_production[i])  # Calculate the sum of the current row
    if current_production_value > max_production_value:
        max_production_value = current_production_value  # Update the maximum production value
        max_production_index = i  # Update the index of the row with the highest production

# Set the row with the highest production to zero
drone_production[max_production_index] = [0] * len(drone_production[max_production_index])

print("Drone Production after setting the highest production row to zero: ", drone_production)


access_code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
invalid_digit = 5

# Remove the invalid digit from the access code
while invalid_digit in access_code:
    access_code.remove(invalid_digit)

print("Access Code after removing invalid digit:", access_code)
