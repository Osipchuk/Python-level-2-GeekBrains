attribute = b'attribute'
# cl = b'класс'
# func = b'функция'
tp = b'type'

enc_dev = 'разработка'.encode()
enc_adm = 'администрирование'.encode()
enc_prot = 'protocol'.encode()
enc_std = 'standard'.encode()

print([enc_dev, enc_adm, enc_prot, enc_std])

dec_dev = enc_dev.decode()
dec_adm = enc_adm.decode()
dec_prot = enc_prot.decode()
dec_std = enc_std.decode()

print([dec_dev, dec_adm, dec_prot, dec_std])