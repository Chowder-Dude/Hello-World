#Keyrecive.py
import socket
import os 
from Crypto.PublicKey import RSA
from Crypto import Random

host = ''
port 12800
connexion = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
connexion.bind((host, port))
connexion.listen(5)
clientconnexion, connexioninfo = connexion.accept()
enc_data = clientconnexion.recv(1024)
print(enc_data)

file = open("Keys.txt", "r")
privatestr = file. read()
file.close()
print(privatestr)

privatekey = RSA.importKey(privatestr)
data = privatekey.decrypt(enc_data)
print(data)

os.system("pause")