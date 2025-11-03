names = input("Enter Name separated by spaces")



list_names = names.split()

list_names.sort()

tuple_names = tuple(list_names)


with open("names_data.txt", 'w') as file:
    file.write(f"name List: {list_names}\n")
    file.write(f"name tuple: {tuple_names}\n")

print("Successfully Saved the file in names_data.txt")

with open("names_data.txt", 'r') as file:
    content = file.read()
    print(content)