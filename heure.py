def heursup(nbh, salaire):
    sumsup = 0
    if nbh <= 39:  # Si le nombre d'heures est inférieur ou égal à 39
        sumsup = 0  # Pas de supplément de salaire
    elif nbh <= 44:  # Si le nombre d'heures est entre 40 et 44 inclus
        sumsup = ((nbh - 39) * (50 / 100)) * salaire  # Calcul du supplément de salaire à 50%
    elif nbh <= 49:  # Si le nombre d'heures est entre 45 et 49 inclus
        sumsup = (((nbh - 39) * (50 / 100)) + ((nbh - 44) * (75 / 100))) * salaire  # Calcul du supplément de salaire à 75%
    else:  # Si le nombre d'heures est supérieur à 49
        sumsup = (((nbh - 39) * (50 / 100)) + ((nbh - 44) * (75 / 100)) + ((nbh - 49) * (100 / 100))) * salaire  # Calcul du supplément de salaire à 100%
    return sumsup  # Retourne le supplément de salaire calculé

nbh = int(input("Veuillez saisir le nombre d'heures : "))  # Demande à l'utilisateur de saisir le nombre d'heures
salaire = float(input("Veuillez saisir le salaire : "))  # Demande à l'utilisateur de saisir le salaire
print(heursup(nbh, salaire))  # Appelle la fonction heursup() avec les valeurs saisies et affiche le résultat
