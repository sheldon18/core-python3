with open('myfile.txt', 'w+') as f:
    f.write('Hello, World\n')
    f.seek(0)
    data = f.read()