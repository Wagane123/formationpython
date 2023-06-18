import socket

serveur=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serveur.blind(''(50000))
serveur. listen(5)
while true:
    
client, infosclient=serveur.accept()
print("client connecté.Adresse"+ infosclient[0])
requete = clint.recv(255)

print(requete.decode("utf-8"))
reponse="Bonjour,Je suis le serveur"
client.send(reponse.encode("utf-8"))
print("connexion fermée")
client.close()
serveur.close()