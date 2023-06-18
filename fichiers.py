import csv

Etudiant =[
            {"nom":"NIANG","prenom":"Khadija","INE":1},
            {"nom":"SANE","prenom":"Bintou","INE":2},
            {"nom":"DRAME","prenom":"Assy","INE":3},
            {"nom":"DIOP","prenom":"Mbar","INE":4}]


##fichier = open("Etudiant.csv","wt")
#liste_etu = csv.DictWriter(fichier,delimiter=";",fieldnames=Etudiant[0].keys())
#liste_etu.writeheader()
#for ligne in Etudiant:
 #   liste_etu.writerow(ligne)
#fichier.close()

fichier = open("Etudiant.csv","r")
liste_aff= csv.DictReader(fichier ,delimiter=";")
for ligne in liste_aff:
    print(ligne)
fichier.close()

