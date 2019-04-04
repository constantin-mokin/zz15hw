# inch to cm

def inch_cm(inch):
    return inch * 2.54
    #return {'cm': inch * 2.54}

#cm to inch

def cm_inch(cm):
    return cm * 0.393701



#mile to km

def mile_km(mile):
    return mile * 1.60934

#km to mile

def km_mile(km):
    return km * 0.621371



#lb to kg

def lb_kg(lb):
    return lb * 0.453592

#kg to lb

def kg_lb(kg):
    return kg * 2.20462



#oz to gram

def oz_gr(oz):
    return oz * 28.3495

#gram to oz

def gr_oz(gr):
    return gr * 0.035274



#american  gallon to liter
def gal_lit(gal):
    return gal * 3.78541

#liter to american gallon
def lit_gal(lit):
    return lit * 0.264172



#american pint to liter

def pint_lit(pint):
    return pint * 0.473176

#liter to american pint

def lit_pint(lit):
    return lit * 2.11338


print('Сделайте свой выбор: ')
print('01. Дюймы в сантиметры')
print('02. Сантиметры в дюймы')
print('03. Мили в километры')
print('04. Километры в мили')
print('05. Фунты в килограммы')
print('06. Килограммы в фунты')
print('07. Унции в граммы')
print('08. Граммы в унции')
print('09. Галлон в литры')
print('10. Литры в галлоны')
print('11. Пинты в литры')
print('12. Литры в пинты')
print('>>>>>>>>>>>>')


while True:
    x = int(input('Введите число от 1 до 12:  '))
    y = 0

    if x == 0:
        print('Exit program')
        break

    elif x not in range(1, 13):
        print('incorrect value!')
        continue

    elif x == 1:
        y = int(input('enter you choice:  '))
        print(inch_cm(y))

    elif x == 2:
        y = int(input('enter you choice:  '))
        print(cm_inch(y))

    elif x == 3:
        y = int(input('enter you choice:  '))
        print(mile_km(y))

    elif x == 4:
        y = int(input('enter you choice:  '))
        print(km_mile(y))

    elif x == 5:
        y = int(input('enter you choice:  '))
        print(lb_kg(y))

    elif x == 6:
        y = int(input('enter you choice:  '))
        print(kg_lb(y))

    elif x == 7:
        y = int(input('enter you choice:  '))
        print(oz_gr(y))

    elif x == 8:
        y = int(input('enter you choice:  '))
        print(gr_oz(y))

    elif x == 9:
        y = int(input('enter you choice:  '))
        print(gal_lit(y))

    elif x == 10:
        y = int(input('enter you choice:  '))
        print(lit_gal(y))

    elif x == 11:
        y = int(input('enter you choice:  '))
        print(pint_lit(y))

    elif x == 12:
        y = int(input('enter you choice:  '))
        print(lit_pint(y))

#print(f'..... думаю что можно было ограничиться меньшим количеством print'ов, не додумал как это реализовать
