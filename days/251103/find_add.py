# def find_sum(a, b):
#     return a+b 

# def find_sum_of_four(first, second, third, fourth, offset=5):
#     add_result = first + second + third + fourth + offset
#     multiply_result = first * second * third * fourth * offset

#     return add_result, multiply_result


# # print(find_sum(1,2))
# print(find_sum_of_four(first=10, second=20, third=30, fourth=40))
# print(find_sum_of_four(first=10, second=20, third=30, fourth=40))


# *other -> tuple
# **other -> dicionary
# def add_sum_of_numbers(a, b, *others):
#     res = a + b
#     for val in others:
#         res += val
#     return res

# print(add_sum_of_numbers(1,2,4))

def find_sum_ka(a, b, **others):
    add_res = a + b
    for val in others:
        add_res += others[val]
    return add_res

print(find_sum_ka(a=1,b=2,c=4))
print("End of Program")