numbers_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 7, 4, 1, 3, 10, 9, 6, 11, 14, 15, 12, 13, 8, 9, 2]
duplicate = []

for number in numbers_list:
        if number % 2 == 0:
            duplicate.append(number)

print("Sum of even numbers:", sum(duplicate))