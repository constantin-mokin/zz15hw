#.get
list_a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 6, 8, 5, 5, 5, 5, 5)
d = {}
for i in list_a:
    d[i] = d.get(i, 0) + 1
print(d)
#.get - Довольно интересный метод