# number = input("Enter a Integer Line, sperated by the space")

# str_number = [int(num) for num in number.split()]

# total = sum(str_number)
# avg = total/len(number)

# with open('integer_line_user.txt', 'r') as output_file:
#     output_file.write(f'list: {words}\n')
#     output_file.write(f'tuple: {word_tuple}\n')

integer_list = input('Numbers (separated by space):')
print(integer_list)
nums = integer_list.split()
print(nums, type(nums))
num=[]

for num_str in nums:
    num = int(num_str)
    nums.append(num)
print(num)

res = 0
for numb in num:
    res += numb

avg = res / len(num)

print(f'sum: {}')

with open('numbers.data.txt', 'w') as output_file:
    output_file.write(f'nubers list: {num}\n')
    output_file.write(f'sum list: {res}\n')
    output_file.write(f'avg: {avg}\n')


with open('numbers.data.txt', 'r') as in_file:
    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()
    print(line1)
    print(line2)
    print(line3)
    