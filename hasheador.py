import hashlib

# r: row, sirve para que lea el '/' como string y no como caracter de escape 

path1=r'C:\Users\Hp\Desktop\proyecto\subidas\shrek.jpg'
path2=r'C:\Users\Hp\Desktop\proyecto\subidas\shrek.jpg'

# rb= r de reading mobe b de binary mode

def hasheador(path):
    with open(path, 'rb') as opened_file:
        content= opened_file.read() #read lee todo el contenido
        sha256= hashlib.sha256()

        sha256.update(content)

        print('el hash de la imagen es: ')
        print()
        print('{}:{}'.format(sha256.name, sha256.hexdigest()))

hash1=hasheador(path1)
hash2=hasheador(path2)

if hash1==hash2:
    print()
    print('los hashes son iguales')
