# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("\nTASK 1: ")

import math

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier:# * multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            print(f"Result - {result}, is greater than 25. Calculation complete.\n")
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("\nTASK 2: ")
def sum_of_numbers(a: int, b: int):
    result = a + b
    print(f"Sum of two numbers: {a} + {b} = {result}")

sum_of_numbers(4, 9)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\nTASK 3: ")
random_numbers_lst = [7, 44, 13, 58, 123, 91, 37, 4, 11, 29, 140, 88, 12, 54, 71, 14]

def average_numbers(random_numbers_lst):
    return sum(random_numbers_lst) / len(random_numbers_lst)

result = int(average_numbers(random_numbers_lst))
print(f"Arithmetic mean: {result}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\nTASK 4: ")
string = "Hello Python world!"
def reverse_string(string: str):
    return result

result = string[::-1]
print(reverse_string(string))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\nTASK 5: ")
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

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("\nTASK 6: ")
def find_substring(str1, str2):
    if str2 in str1:
        index = str1.find(str2)
        return index
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""Якщо кількість унікальних символів в строці більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()"""
print("\nTASK 7: ")
def unique_chars(chars):
    return len(set(chars))
chars = input("Enter text: ")
unique_char = set(chars)

# print(len(unique_chars))

if len(chars) > 10:
    print(True)
else:
    print(False)

# task 8

"""функція, виводіть, скільки слів у тексті починається з Великої літери"""
print("\nTASK 8: ")
sentence = "By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite,\n"\
       "in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing\n"\
       "it with—and so on, and so on, hour after hour.\n"
def words_upper_letter(sentence):
    if isinstance(sentence, str):
        words = sentence.split()  # розбиваємо рядок на слова
        count = 0
        for word in words:
            if word[0].isupper():  # якщо перша літера слова велика до в count + 1
                count += 1
        return count
    else:
        return "Error: enter text: "


print(f"Number of words with a upper letter: {words_upper_letter(sentence)}")

# task 9

"""Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?"""

print("\nTASK 9: ")
def photo_album_size(photos):
    photos_one_page = 8
    result = math.ceil(photos / photos_one_page)
    return result

while True:
    number_of_photos = input("Enter number of photos: ")
    if number_of_photos.isdigit():  # перевіряємо, що число ціле
        photos = int(number_of_photos)
        pages_required = photo_album_size(photos)
        print(f"Ihor will need {pages_required} pages.")
        break
    else:
        print("ERROR!!! Enter an integer: ")


# task 10

"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("\nTASK 10: ")
# sum_warehouses = 375291
# first_and_second_warehouses = 250449
# second_and_third_warehouses = 222950

quantity_items = ["sum_warehouses = 375291, first_and_second_warehouses = 250449, second_and_third_warehouses = 222950"]
def verification (sum_warehouses, first_and_second_warehouses, second_and_third_warehouses):

    first_warehouse = sum_warehouses - second_and_third_warehouses
    third_warehouse = sum_warehouses - first_warehouse
    second_warehouse = sum_warehouses - first_warehouse - third_warehouse
    if first_warehouse + second_warehouse + third_warehouse == sum_warehouses:
        print(
            f"There are {first_warehouse} items in first warehouse.\n"
            f"There are {second_warehouse} items in second warehouse.\n"
            f"There are {third_warehouse} items in third warehouse.\n"
        )
    else:
        print("Recalculate")
verification(375291, 250449, 222950)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним."""