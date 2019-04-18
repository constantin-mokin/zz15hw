#task 06

from datetime import datetime

name = ('Mr.Key')

print((lambda name: f' Hello, {name}')(name))

def my_decorator(func):
    def time_1():
        start = datetime.now()
        func()
        end = datetime.now() - datetime.now()
        print(f'{end - start}')
    return time_1()






