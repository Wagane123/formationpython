import csv

# Définition des données des étudiants
etudiants = [
    {"nom": "NIANG", "prenom": "Khadija", "INE": 1},
    {"nom": "SANE", "prenom": "Bintou", "INE": 2},
    {"nom": "DRAME", "prenom": "Assy", "INE": 3},
    {"nom": "DIOP", "prenom": "Mbar", "INE": 4}
]

# Écriture des données dans un fichier CSV
with open("Etudiant.csv", "w", newline="") as fichier:
    liste_etu = csv.DictWriter(fichier, delimiter=";", fieldnames=etudiants[0].keys())
    liste_etu.writeheader()
    for etudiant in etudiants:
        liste_etu.writerow(etudiant)

# Lecture des données à partir du fichier CSV
with open("Etudiant.csv", "r") as fichier:
    liste_aff = csv.DictReader(fichier, delimiter=";")
    for ligne in liste_aff:
        print(ligne)
