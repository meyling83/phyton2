import os

#print(os.environ)

#login=os.getlogin()
#print(login)


#path=os.getcwd()
#print(path)
#os.chdir('../')
#path=os.getcwd()
#print(path)

directorio=input("entre el nombre del directorio")
parent_dir=os.getcwd()
path=os.path.join(parent_dir,directorio)
os.mkdir(path)

import os
import platform
""" directorio=input("entre el nombre del directorio")
parent_dir="D:\\"
path=os.path.join(parent_dir,directorio)
print(os.getcwd())
os.mkdir(path) """

print(os.name)
print(platform.uname())
print(os.getcwd())
path=os.path.join(os.getcwd(),"carpeta")
#os.mkdir(path)
print (path)
print(os.path.split(os.getcwd()))
dir,carpeta=os.path.split(os.getcwd())
print(dir,carpeta)
#devuelve verdadero si abc.py es un archivo, si no existe devuelve false
print(os.path.isfile(os.path.join(os.getcwd(),"abc.py")))
#devuelve verdadero si carpeta es un directorio, sino existe devuelve falso
print(os.path.isdir(os.path.join(os.getcwd(),"carpeta")))
#devuelve verdadero si existe carpeta en el directorio actual
print(os.path.exists(os.path.join(os.getcwd(),"carpeta")))
#sube una carpeta
#os.chdir("../")
#muestra las carpetas y achivos que hay en el directorio actual
print(os.listdir(os.getcwd()))

