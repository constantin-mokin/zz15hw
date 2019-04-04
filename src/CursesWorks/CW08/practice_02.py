def my_func(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
        #if not len(key) % 2:
            print(key, value)


arguments = {'ad' : 1, 'b' : 2, 'c' :3, 'rd' : 4,'errrr' :5,'fffff' : 6}

my_func(**arguments)
