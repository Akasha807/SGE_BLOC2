import read_registre as rr
results = rr.read_reg()
for i in results:
    print('\n')
    print('Nom: ' + i[1])
    print('Adreça:' + i[2])
    print('telèfon: ' + i[3])
    print('email: ' + i[4])
    print('neixament: ' + i[5])