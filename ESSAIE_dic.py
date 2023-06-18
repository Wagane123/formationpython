# Définition du dictionnaire CBanque contenant des informations sur les comptes bancaires
CBanque = [
    {"nom": "fall", "prenom": "mamour", "solde": 1002000},
    {"nom": "niang", "prenom": "Khadija", "solde": 100000}
]

# Définition de la fonction Depot pour effectuer un dépôt
def Depot(solde, numero_compte):
    if numero_compte == solde:  # Correction : Utilisation de l'opérateur d'égalité (==) au lieu de l'opérateur d'affectation (=)
        print("Votre demande a été effectuée")

# Définition de la fonction retrait pour effectuer un retrait
def retrait(solde, numero_compte):
    if numero_compte == solde:  # Correction : Utilisation de l'opérateur d'égalité (==) au lieu de l'opérateur d'affectation (=)
        print("Votre demande a été effectuée")

# Initialisation du dictionnaire compt_bancaire
compt_bancaire = {"client": {"NOM", "Prenom"}, "solde": 0}

numero_compte = input("Entrez votre numero de compte : ")

if numero_compte == numero:  # Correction : Utilisation de l'opérateur d'égalité (==) au lieu de l'opérateur d'affectation (=)
    action = int(input("Voulez-vous faire un dépôt (1) ou un retrait (2) ? : "))

    if action == 1:  # Si l'action est un dépôt
        montant_depot = float(input("Entrez le montant à déposer : "))
        compt_bancaire["solde"] += montant_depot
        print("Votre dépôt a été effectué")

    elif action == 2:  # Si l'action est un retrait
        montant_retrait = float(input("Entrez le montant à retirer : "))
        if montant_retrait <= compt_bancaire["solde"]:
            compt_bancaire["solde"] -= montant_retrait
            print("Votre retrait a été effectué")
        else:
            print("Solde insuffisant")

    else:
        print("Action invalide")

else:
    print("Numéro de compte invalide")
