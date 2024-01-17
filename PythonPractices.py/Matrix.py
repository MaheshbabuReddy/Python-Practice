x = 4
matrix = list(range(1, x**2 + 1))

# Split the matrix into 4 types using map and lambda function
split_size = len(matrix) // 4
types = list(map(lambda i: matrix[i * split_size:(i + 1) * split_size], range(4)))

# Print the four types
for i, matrix_type in enumerate(types, start=1):
    print(f"Type {i}:", matrix_type)




