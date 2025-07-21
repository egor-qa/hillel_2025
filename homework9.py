"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_numbers(number15, number12):
    return sum([number15, number12])
print(sum_of_numbers(15, 12))

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

random_numbers_lst = [7, 44, 13, 37, 4, 11, 12, 14]

def average_numbers(random_numbers_lst):
    return sum(random_numbers_lst) / len(random_numbers_lst)
result = sum(random_numbers_lst) / len(random_numbers_lst)

# result = int(average_numbers(random_numbers_lst))
print(f"Arithmetic mean: {result}")

"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

string = "Hello Python world!"
def reverse_string(string: str):
    return result

result = string[::-1]
print(reverse_string(string))

"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

list = ["Longest", "word", "in", "this", "sentence"]
def longest_word(list):
    max_len = 0
    longest = ""
    for word in list:
        if len(word) > max_len:
            max_len = len(word)
            longest = word
    return longest
print(longest_word(list))

