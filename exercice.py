#Definir une liste en python contenant une liste de personne
#1-ecrire une fonction python permetant d'ajouter un element donné a une position
#2-ecrire une fonction python permetant de modifier une personne
#3-ecrire une fonction python permetant de supprimer une personne avec son iindice
#4-ecrire une fonction python permetant de parcourir la liste et d'afficher les elements un en un
#5-ecrire une fonction python permetant de trier par ordre alphabetique les elements de la liste
#-ecrire unprogramme permetant d'excuter les fonctions

def ajoutPersonne(a,i,val):
    if i<len(a) :
        a[i]=val
        
    else:
        a[i]=val
    print(a)




def modifPersonne(a ,i ,val ):
        if i<len(a)-1 :
            a[i]=val
        else :
             print("cette indice n'est pas dans la liste")   
             


def suppfPersonne(a ,i ):
        if i<len(a)-1 :
            a.pop(i)
        else :
             print("cette indice n'est pas dans la liste")                       


def parcourParsonne(a) :
     Personne=["amina","kine","fallou","mouhamed","ali"]
     

def tree(a) :
     a.sort()
     print(a)

if __name__=="__main__":
    Personne=["amina","kine","fallou","mouhamed","ali"]

    nom=input("veuiller inserer un  nom")  #pour la supp on enleve ce message
    index=(int(input("Donner l indice ")))
    ajoutPersonne( Personne,index,nom)
    #4
    # parcourPersonne(Personne)
    #5
    # ordrePersonne(Personne)

   


 
