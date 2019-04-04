string = input('type valid e-mail adress ---')
string = string.split('@')
domain = 'gmail.com'
if string[1] == domain:
    print(string[0])
else:
    print('domain name is not supported')
