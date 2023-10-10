def search(key,list):
    for ele in list:
        if ele == key:
            return True
    return False
list=[13,343,3,234,43]
key= int(input("enter key: "))
print(search(key,list))