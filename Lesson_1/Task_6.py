with open('test_file.txt', 'w') as f:
    f.write('сетевое программирование\nсокет\nдекоратор')
#print(f)
with open('test_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

