a = int(input('---> '))
if a%1000 == 0:
    print('millenium') #01.complete

n = int(input('Enter the number of guest:  '))
if n < 20:
    print('Go Home!')
elif n > 50:
    print('Go Rest')
else:
    print('Go Cafe') #02. complete

string = input('type here...')
if len(string) > 10:
    string_a = ('!!!')
    print(string_a)
elif len(string) < 10 and len(string) > 1:
    print(string[1]) #03. complete
else:
    print(string[0]) # немного увеличил код т.к. выкидывало ошибку при выведении 2го символа если в строке 1 символ

string_c = input('type --->  ') # затупил... жёстко затупил...
str_a = len(string_c) // 2
print(string_c[str_a])

if string_c[0] == string_c[-1]:
    print(string_c[1:-1]) #04. complete... если б не ваши подсказки)))

