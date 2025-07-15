alice_in_wonderland = ( "Would you tell me, please, which way I ought to go from here?\n"
                       "That depends a good deal on where you want to get to - said the Cat.\n"
                       "I don't much care where - said Alice.\n"
                       "Then it doesn't matter which way you go - said the Cat.\n"
                       "So long as I get somewhere, Alice added as an explanation.\n"
                       "Oh, you're sure to do that - said the Cat, - if you only walk long enough." )
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

for mean in alice_in_wonderland:
    if mean == "'":
        print(mean)

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800
area_black_and_azov_sea = area_black_sea + area_azov_sea

print(f"Площа двох морів дрорівнює {area_black_and_azov_sea} км2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum_warehouses = 375291
first_and_second_warehouses = 250449
second_and_third_warehouses = 222950
first_warehouse = sum_warehouses - second_and_third_warehouses
third_warehouse = sum_warehouses - first_warehouse
second_warehouse = sum_warehouses - first_warehouse - third_warehouse

def verification ():
    if first_warehouse + second_warehouse + third_warehouse == sum_warehouses:
        print(
            f"На першому складі {first_warehouse} товарів.\n"
            f"На другому складі {second_warehouse} товарів.\n"
            f"На третьому складі {third_warehouse} товарів."
        )
    else:
        print("перерахувати")
verification()

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_per_month = 1179
payment_term = 18
cost_pc = payment_per_month * payment_term

print(f"Вартість комп’ютера складає {cost_pc} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(a, b, c, d, e, f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
cost_big_pizza = 4 * 274
cost_middle_pizza = 2 * 218
cost_juice = 4 * 35
cost_cake = 1 * 350
cost_water = 3 * 21
total_cost = cost_big_pizza + cost_middle_pizza + cost_juice + cost_cake + cost_water

print(f"для замовлення потрібно {total_cost} грн.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photos_one_page = 8
pages_required = all_photos / photos_one_page

print(f"для розміщення всіх фото, Ігорю знадобиться {int(pages_required)} сторінок альбому.")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

Kharkiv_Budapest = 1600
tank_capacity = 48
gasoline_at_100 = 9
distance_tank = (tank_capacity / gasoline_at_100) * 100
print(f"Відстань, яку можна проїхати на повному баку дрорівнює {round(distance_tank)} км.")

gasoline_required = Kharkiv_Budapest / 100 * gasoline_at_100
print(f"кількість бензину для подорожі дрорівнює {round(gasoline_required)} л.")

refuel_car = Kharkiv_Budapest / distance_tank
print(f"кількість заправок дрорівнює {int(refuel_car)}.")