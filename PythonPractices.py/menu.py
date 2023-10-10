dic = {"JIJ", "Klin", "Jaadu"}

# Iterate over the keys in dic and print the formatted strings
for index, key in enumerate(dic, start=1):
    # Replace the index position with "1" in the formatted string
    formatted_string = f"{key[:index-1]}1{key[index:]}"
    
    # Print the formatted string
    print(formatted_string)

