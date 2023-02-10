import sqlite3
import os

def db_create():
  conn = sqlite3.connect('database.db')
  print ("Base de datos abierta exitosamente")

  conn.execute('CREATE TABLE usuario(nombre TEXT, apellido TEXT, correo TEXT, password TEXT)')
  print ("Tabla creada")

  conn.close()

base_dir = os.path.join (os.path.dirname(__file__), 'static')

path_cortada = os.path.join (base_dir, r'cortada.jpg')
path_quemadura = os.path.join (base_dir, r'quemadura.jpg')
path_congela = os.path.join (base_dir, r'congela.jpg')
path_respiracion = os.path.join (base_dir, r'rcp.jpeg')
path_mordedura = os.path.join (base_dir, r'picadura_arana.jpeg')
path_arma = os.path.join (base_dir, r'herida_armablanca.jpg')