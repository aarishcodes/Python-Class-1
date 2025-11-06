message = input("Words (Seperated by space):")
print(message)
words = message.split(" ")

print(words, type(words))

word_tuple = tuple(words)
print(word_tuple, type(word_tuple))

'''
output_file = open('qn01_data.txt', 'w')
output_file.write(f'list: {words}')
output_file.write(f'tuple: {word_tuple}')
output_file.close()
'''

with open('qn01_data.txt', 'w') as output_file:
    output_file.write(f'list: {words}\n')
    output_file.write(f'tuple: {word_tuple}\n')

with open('qn01_data.txt', 'w') as input_file:
    file_words_list_line = input_file.readline()
    file_words_tuple_line = input_file.readline()
    print(file_words_list_line)
    print(file_words_tuple_line)
