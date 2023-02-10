import hashlib
import db

def hasheado(path):
    with open(path, 'rb') as opened_file:
        content = opened_file.read()
        sha256 = hashlib.sha256()

        sha256.update(content)
        # print('El hash de la imagen es: ')
        return ('{} : {}'.format(sha256.name, sha256.hexdigest()))

def comparador(path1, path2):
    hash1 = hasheado(path1)
    hash2 = hasheado(path2)

    if hash1 == hash2:
        return True
    else:
        return False
    
def url_select(path):
    if comparador(db.path_cortada, path):
        return ('info_cortada.html')
    elif comparador(db.path_quemadura, path):
        return ('info_quemadura.html')
    elif comparador(db.path_congela, path):
        return ('info_congela.html')
    elif comparador(db.path_mordedura, path):
        return ('info_mordedura.html')
    elif comparador(db.path_respiracion, path):
        return ('info_respiracion.html')
    elif comparador(db.path_arma, path):
        return ('info_arma.html')
    else:
        return ('vayavaya.html')
