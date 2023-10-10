# Function to print a hollow rectangle with user-specified numbers and symbols
def print_rectangle(n, m, data):
    data_index = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or i == n or j == 1 or j == m:
                if data_index < len(data):
                    print(data[data_index], end="")
                    data_index += 1
                else:
                    print("*", end="")
            else:
                print(" ", end="")
        print()

# Driver program for above function
rows = 6
columns = 20

# Ask the user to enter a string containing numbers and symbols
user_input = input("Enter a string of numbers and symbols: ")
print_rectangle(rows, columns, user_input)

