def search_element(element, lst):
    for item in lst:
        if item == element:
            return True
    return False

# Example usage
my_list = [10, 20, 30, 40, 50]
search_value = int(input('enter a number'))

if search_element(search_value, my_list):
    print(f"The element {search_value} is present in the list.")
else:
    print(f"The element {search_value} is not found in the list.")
