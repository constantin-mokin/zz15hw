
#функция для поиска среднеарфиметического

def arif_mean(*args):
    arif = sum(args) / len(args)
    return arif

arguments = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(arif_mean(*arguments))


#функция для поиска среднегеометрического

def geom_mean(*args):
    mult = 1
    for elem in args:
        mult *= elem
    geom = mult ** 1/len(args)
    return geom

print(geom_mean(*arguments))


#Именованный аргумент???

def mean_type(arif_mean, geom_mean):
    print(arif_mean)
    print(geom_mean)
#???????????

#как это всё правильно делать?
