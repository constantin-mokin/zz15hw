#task09 #Poisk oshibok

try:
   a = int(input('a: '))
   b = int(input('b: '))
   result = a / b
except ZeroDivisionError as err:
   print(f'b is zero - {err}!!!')
except Exception as err:
   print(f'SOMETHING WRONG - {err}!!!')


