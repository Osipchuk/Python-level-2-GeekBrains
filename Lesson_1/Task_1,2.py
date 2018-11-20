words = ['разработка', 'сокет', 'декоратор']
for word in words:
    print(f'{word} - {type(word)}')

print('='*20)
print('Unicode')

words_u = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
            '\u0063\u043e\u043a\u0435\u0442',
            '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for word in words_u:
    print(f'{word} - {type(word)}')

print('='*20)
print('Bytes')

words_b = [b'class', b'function', b'method']
for word in words_b:
    print(f'{word} - {type(word)} - длина {len(word)}')