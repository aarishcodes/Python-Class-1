# name = "Aarish Faiz"
# name  = "Aarish Faiz2"

# person = input("Enter you name: ")

# print(f'Hello {name}')
# print(f'hello {person}')


# def greeting():
#     print(f'"Good Afternoon" {person}')

# greeting()


# def greet(name):
#     res = f'Hello {name}'
#     return res

# def hi(name):
#     result = f'Hi {name}'
#     return result

# name = input("Enter you name: ")

# print(greet(name))
# print(hi(name))

salaries = []

salaries.append(100)
salaries.append(200)
salaries.append(300)
salaries.append(400)

# Based on the argument
# salaries.pop()

# salaries.remove(200)
# print(salaries)


search = 400
I=0
search_indx = -1

for salary in salaries:
    if salary == search:
        search_indx = I
        break
    I += 1

print(search_indx)

    