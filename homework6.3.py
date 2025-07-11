lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

for elements in lst1:
    lst2 = []
    if isinstance(elements, str):
        lst2.append(elements)
        print(lst2)