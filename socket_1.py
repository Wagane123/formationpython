import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crée un objet socket pour le serveur
serveur.bind(('localhost', 50000))  # Associe le serveur à l'adresse locale (localhost) et au port 50000
serveur.listen(5)  # Met le serveur en mode écoute, acceptant jusqu'à 5 connexions en attente

while True:  # Boucle principale du serveur, continue indéfiniment jusqu'à ce qu'il soit arrêté

    client, infosclient = serveur.accept()  # Accepte une connexion entrante du client et retourne un nouvel objet socket pour la communication avec le client
    print("Client connecté. Adresse : " + infosclient[0])  # Affiche l'adresse IP du client connecté

    requete = client.recv(255)  # Reçoit les données envoyées par le client (ici, jusqu'à 255 octets)
    print(requete.decode("utf-8"))  # Décode les données reçues en utilisant l'encodage UTF-8 et les affiche

    reponse = "Bonjour, je suis le serveur"  # Prépare la réponse à envoyer au client
    client.send(reponse.encode("utf-8"))  # Encode la réponse en utilisant l'encodage UTF-8 et l'envoie au client

    print("Connexion fermée")  # Affiche un message indiquant que la connexion est fermée
    client.close()  # Ferme la connexion avec le client

    serveur.close()  # Ferme le socket du serveur (ce code ne sera pas atteint car la boucle while est infinie)
