# task 01 == Виправте синтаксичні помилки

print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки

hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print

    for letter in "Hello world!":
        print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук

apples = 2
banana = apples * 4
print(banana)

# task 05 == виправте назви змінних

side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача

perimetery = 1 + 2 + 3 + 4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apples = 4
pears = apples + 5
plums = apples - 2
print(apples, pears, plums)
trees = apples + pears + plums
print(trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

temp_before_lunch = 0 + 5
temp_after_lunch = (temp_before_lunch - 10)
temp_evening = (temp_after_lunch + 4)
print(temp_before_lunch, temp_after_lunch, temp_evening)
print(temp_evening)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys = 24
girls = 24 / 2
sick = 1
absent = 2
present = int(boys + girls - sick - absent)
print(present)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

book_1 = 8
book_2 = 8 + 2
book_3 = int(book_1 + book_2) / 2
all_books = int(book_1 + book_2 + book_3)
print (all_books)