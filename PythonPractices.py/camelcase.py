user_input = input("Enter the string: ")
result_list = [user_input[i].upper() if i % 2 == 0 else user_input[i] for i in range(len(user_input))]
result_string = ''.join(result_list)
print(result_string)

