#Definir une liste en python contenant une liste de personne
#1-ecrire une fonction python permetant d'ajouter un element donné a une position
#2-ecrire une fonction python permetant de modifier une personne
#3-ecrire une fonction python permetant de supprimer une personne avec son iindice
#4-ecrire une fonction python permetant de parcourir la liste et d'afficher les elements un en un
#5-ecrire une fonction python permetant de trier par ordre alphabetique les elements de la liste
#-ecrire unprogramme permetant d'excuter les fonctions
def ajoutPersonne(list,indice,element):
    list.insert(indice, element)
    return list

def modifierPersonne(list,indice):
    list[indice]=element
    return list

def supprimerPersonne(indice):
    del list[indice]
    return list


listPersonne = ['Test','Test1','Toto']
result = ajoutPersonne(listPersonne,4,'Faye')
print(result)

result1 = modifierPersonne(listPersonne,1,'Diouf')
print(result1)

result2 = supprimerPersonne(1,'Diouf')
print(result1)

