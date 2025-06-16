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


# Cells in row 0 stay the same.  Cell in row 1 increases by 1, row 2 decrease by 2.
#  After adjusting, sum the values and print the total energy.

energy_grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for i in range(len(energy_grid)):
    for j in range(len(energy_grid[i])):
       energy_grid[i][j] -= i

total_energy = 0

for row in energy_grid:
    for cell in row:
        total_energy += cell  # Summing the values in the energy grid
print("Total Energy after adjustments:", total_energy)


# Extract even numers

numers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
for number in numers:
    if number % 2 == 0:  # Check if the number is even
        total += number  # Add the even number to the total
print("Total of even numbers:", total)

# Eliminating duplicates from a list of laser sequences
laser_sequence = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7]

seen_numbers = []
rogue_lasers = []

for number in laser_sequence:
    if number not in seen_numbers:
        seen_numbers.append(number)  # Add the number to the seen list if it's not already there
    else:
        rogue_lasers.append(number)  # If it's a duplicate, add it to the rogue lasers

print("Unique Laser Sequences:", seen_numbers)


# The bomb is armered, but its detonation sequence is incomplete.
# Six control wires of varying lenghths determine when the bomb will explode.
# However, only the middle four wires hold the correct timing data needed to activate the bomb.
# Your mission is to analize the wire lengths and extract the crucial four wires.
# And vereify if they match the activation key.

wire_lengths = [10, 20, 30, 40, 50, 60]
activation_key = [20, 30, 40, 50]

sorted_wires = sorted(wire_lengths)  # Sort the wire lengths in ascending order
selected_wires = sorted(activation_key)

# Como deberia de ser la secuencia de activación
# Ordenar las longitudes de los cables
sorted_wires = sorted(wire_lengths)

# Extraer los cuatro cables centrales
middle_wires = sorted_wires[1:5]  # Índices 1 a 4 (excluyendo el último)

# Verificar si coinciden con la clave de activación
if middle_wires == activation_key:
    print("La bomba está activada correctamente.")
else:
    print("Error: Los cables no coinciden con la clave de activación.")


# billboard_matrix = [
#     [***********************],
#     [**************************************],
#     [**************************************]
# ]
#
#
# for i in range(len(billboard_matrix)):
#     billboard_matrix[i] = billboard_matrix[i][::-1]  # Reversing each row


list1 = [1000, 2420, 3210, 4120, 1250]
list2 = [3220, 5340, 1590, 7860, 96542]

combined_list = list1+list2
unique_list = []


for num in combined_list:
  if num not in unique_list:
    unique_list.append(num)


reversed_list = list(reversed(unique_list))


passcode = reversed_list[0]
print("Passcode:", passcode)


#
initial_rotation = [10]

replicating_rotation = 9


rotation_steps = initial_rotation * replicating_rotation

total_rotation = 0
for step in rotation_steps:
   total_rotation -= step


print("Total crane rotation:", total_rotation, "degrees")

power_levels = [10, 12, 27.5, 16, 40]


even_levels = [] # Numeros pares
odd_levels = [] # Numeros impares multiplicados por 2

for num in power_levels:
    if num % 2 == 0:
        even_levels.append(num)
    else:
        odd_levels.append(num * 2)

codes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valid_codes = []

for num in codes:
    if num % 2 == 0:
        valid_codes.append(num)

access_code = 0

access_code = sum(valid_codes)

print("Access Code:", access_code)


access_codes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


sum = 0


for i in range(len(access_codes)):
  if i % 2 == 0 and access_codes[i] % 5 == 0:
    sum = sum + access_codes[i]




scrambled = 'S3G78R1A2M4B5L6E9D0'

result = ""

for ch in scrambled:
    if not ch.isdigit():
        result += ch.lower()


power_grids = ["grid-1", "grid-2", "grid-3", "grid-4"]

current_power_connection = power_grids[4]

