import socket

adresseIP ="127.0.0.1" #ici le poste local
port = 50000

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((adresseIP,port))
print("connecté au serveur")
client.send("bonjour,je suis le client".encode("utf-8"))
reponse=client.recv(255)
print (reponse.decode(utf-8))
print("connexion fermée")
cklient.close()