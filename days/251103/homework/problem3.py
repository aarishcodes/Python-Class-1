sentance_by_user = input("Enter a Sentance ")

words_list = sentance_by_user.split()

word_tuple = tuple(word.upper() for word in words_list)

with open("sentence_data.txt", 'w') as file:
    file.write(f"List: {words_list}\n")
    file.write(f"Tuple: {word_tuple}\n")

print("Successfully Saved the data in sentence_data.txt")

with open("sentence_data.txt", 'r') as file:
    content = file.read()
    print(content)