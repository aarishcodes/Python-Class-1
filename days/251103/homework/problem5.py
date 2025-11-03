numbers = input("Enter the Number separated by space")

number_list = [float(x) for x in numbers.split()]

max_num = max(number_list)
min_num = min(number_list)

with open("minmax_data.txt", 'w') as f:
    f.write(f"Number List: {number_list}\n")
    f.write(f"Maximum Number: {max_num}\n")
    f.write(f"Minimum Number: {min_num}\n")

print(f"Successfully Saved the Data in minmax_data.txt")


with open("minmax_data.txt", 'r') as f:
    content = f.read()
    print(content)  
