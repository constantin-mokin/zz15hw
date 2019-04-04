list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = 0
i = 0
while i < len(list_a):
    if list_a[i] % 2 == 0:
        even += 1
    i += 1      # пока не вывел из под условия не работало..
print(even)

