#task11

with open('test.txt', 'w') as my_file:
    # my_file.writelines(['sdada\n', 'aaa\n', 'bbbb\n', 'c\n', 'asdasdf\n', 'qwrkjzncv\n'])
    for i in range(6):
        a = input('write a word ---')
        my_file.write(a + 'd\n')
#input
#while True
my_file.close()
