#!/usr/bin/python3
import os
#https://stackabuse.com/executing-shell-commands-with-python/
import subprocess
import termrecord

#TermRecord -o term-record.html


os.system('clear') #al ser linux o mac

fichero="/Users/path/SSHACCESS/vm.txt"


#print(linea)
#linea.split(sep=",", maxsplit=3)
#print(linea.split(sep=",", maxsplit=3))

numlinea=1

print("SELECCIONA OPCIÓN DE SERVIDOR")
print()

f = open(fichero, "r")
while(True):
    linea = f.readline()
    if not linea:
        break
    servidor=linea.split(sep=",", maxsplit=3)[0]
    nombre_servidor=linea.split(sep=",", maxsplit=3)[1]
    usuario=linea.split(sep=",", maxsplit=3)[2]
    print(str(numlinea) +" "+nombre_servidor+" "+servidor) 
    numlinea=numlinea+1
f.close()

print (str(numlinea) + " SALIR") 
seleccion=input()

if seleccion == numlinea:
    exit()

numlinea=1
f = open(fichero, "r")


while(True):
    linea = f.readline()
    if not linea:
        break
    servidor=linea.split(sep=",", maxsplit=3)[0]
    nombre_servidor=linea.split(sep=",", maxsplit=3)[1]
    usuario=linea.split(sep=",", maxsplit=3)[2]         
    if str(numlinea) == str(seleccion):
        #ssh_log_start = subprocess.run(["script", "sesion.txt"])
        ssh_conecta = subprocess.run(["ssh", usuario+"@"+servidor])
        #ssh_conecta.wait()
        #ssh_log_stop = subprocess.run(["exit"])
    numlinea=numlinea+1
f.close()

