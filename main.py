from flask import Flask, jsonify, render_template,request, url_for
from werkzeug.utils import secure_filename
import os
app=Flask(__name__)

app.config['UPLOAD_FOLDER']='static/uploads/'

ALLOWED_EXTENSIONS=set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_files(file):
    file=file.split('.')
    print(file)
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False
@app.route('/upload', methods=['POST'])
def upload():
    file=request.files['uploadfile']
    print(file, file.filename)
    filename=secure_filename(file.filename)
    print(filename)
    if file and  allowed_files(filename):
        print('permitido')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload_file.html',mensaje='archivo subido exitosamente' )
    return render_template('upload_file.html',mensaje='no se subio el archivo' )
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')

