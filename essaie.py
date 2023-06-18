# """compteur =0
# n=28
# while(n%2==0) : 
#     n = n /1 
#     compteur += 1
#     print("le nombre",n,"est divisible par 2",compteur,"fois")"""


# def produit(x,y):
#     if((x>0 and y>0) or (x<0 and y<0)):
#         print("la le produit des deux valeurs est positif")
#     else:
#         print("le produit des deux valeur est negatif")

# x=int(input("saisissez une valeur"))
# y=int(input("saisissez une autre valeur"))     
# produit(x,y)
    


# #----------EXERCIE-------------------------------------------------
# recolter une valeur porte monnaie
# wallet = int(input("Entrer le nombre d'€ que vous possedez"))
# print("Vous avez actuellement", wallet, "euros")

# # creer un produit qui aura pour valeur 50
# produit = 50
# print("Le Produit vaut " + str(produit) + "euros")

# # enleve au "wallet" le prix du produit 
# wallet = wallet - produit
# # ou wallet -= produit

# # afficher la nouvelle valeur
# print("Produit acheté !")
# print("Il ne vous reste plus que" + str(wallet) + "euros")
# # #-----------EXERCICE-----------------------------------------------
# note1 = int(input(" ENTRER LA PREMIERE NOTE "))
# note2 = int(input(" ENTRER LA SECONDE NOTE "))
# note3 = int(input(" ENTRER LA DERNIERE NOTE "))
# MOYENNE = (note1 + note2 + note3) / 3
# print(MOYENNE)

#-------------------EXERCICE CINEMA--------------------
age = int(input("Entrer votre age :"))
if age <= 17:
    prix = 7
    print("vous etes mineur vous devez payer " + str(prix) + "£")
else:
    prix = 12
    print("vous etes majeur vous devez payer " + str(prix) + "£")
manger = input("souhaitez vous du pop-corn?")
if manger == "OUI":
    prix += 5

print("Vous devez payer" + str(prix) + "£")