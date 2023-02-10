from flask import Flask , render_template , request
from werkzeug.utils import secure_filename
from hasheador import url_select

import os

app = Flask(__name__)

app.config["UP_FOLDER"] = "static/comparador"

ext_permitidas = set(['png', 'jpg', 'jpeg'])

def ext_permitida(file):
 file = file.split('.')
 if file[1] in ext_permitidas:
  return True
 return False

@app.route('/', methods = ['GET'])
def home():
 return render_template('home.html')

@app.route('/nuevousuario')
def nuevousuario():
 return render_template('nuevousuario.html')

@app.route('/vayavaya')
def vayavaya():
 return render_template('vayavaya.html')

@app.route('/registro')
def registro():
  return render_template('registro.html')

@app.route('/subir_imagen', methods = ['GET' , 'POST'])
def subir_imagen():
  if request.method == 'POST':
    file = request.files['archivo_subido']
    basepath = os.path.dirname (__file__)
    filename = secure_filename(file.filename)

    if ext_permitida(filename):
        upload_path = os.path.join (basepath, app.config["UP_FOLDER"], filename) 
        file.save(upload_path)
    else:
        return render_template('vayavaya.html')

    return render_template(url_select(upload_path))

  return render_template('subir_imagen.html')

if __name__ == '__main__':
 app.run(debug = True, port=7000)