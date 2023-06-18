def ajoutPersonne(a, i, val):
    if i < len(a):
        a.insert(i, val)  # Utilise la méthode insert() pour ajouter l'élément à la position donnée
    else:
        a.append(val)  # Utilise la méthode append() pour ajouter l'élément à la fin de la liste
    print(a)


def modifPersonne(a, i, val):
    if i < len(a):
        a[i] = val  # Modifie l'élément à l'indice donné avec la nouvelle valeur
    else:
        print("Cet indice n'est pas dans la liste")


def suppfPersonne(a, i):
    if i < len(a):
        a.pop(i)  # Utilise la méthode pop() pour supprimer l'élément à l'indice donné
    else:
        print("Cet indice n'est pas dans la liste")


def parcourParsonne(a):
    for personne in a:
        print(personne)  # Parcourt la liste et affiche chaque élément


def triPersonne(a):
    a.sort()  # Utilise la méthode sort() pour trier les éléments de la liste par ordre alphabétique
    print(a)


if __name__ == "__main__":
    Personne = ["amina", "kine", "fallou", "mouhamed", "ali"]

    nom = input("Veuillez insérer un nom : ")
    index = int(input("Donnez l'indice : "))
    ajoutPersonne(Personne, index, nom)  # Appel de la fonction ajoutPersonne pour ajouter un élément à une position donnée

    # modifPersonne(Personne, index, nom)  # Appel de la fonction modifPersonne pour modifier une personne

    # suppfPersonne(Personne, index)  # Appel de la fonction suppfPersonne pour supprimer une personne avec son indice

    # parcourParsonne(Personne)  # Appel de la fonction parcourParsonne pour parcourir et afficher les éléments de la liste

    # triPersonne(Personne)  # Appel de la fonction triPersonne pour trier les éléments de la liste par ordre alphabétique
