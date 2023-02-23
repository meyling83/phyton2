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