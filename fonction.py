import turtle

# Crée un objet Turtle et un objet Screen
t = turtle.Turtle()
s = turtle.Screen()

# Définit la couleur de fond de l'écran en blanc
s.bgcolor('white')

# Définit la couleur du crayon en vert
t.pencolor('green')

# Définit la vitesse de déplacement de la tortue à la vitesse maximale
t.speed(0)

# Boucle pour dessiner les formes
for i in range(150):
    t.circle(190 - i, 90)  # Dessine un cercle avec un rayon décroissant à chaque itération et un angle de 90 degrés
    t.lt(98)  # Tourne la tortue vers la gauche de 98 degrés
    t.circle(190 - i, 90)  # Dessine un autre cercle avec un rayon décroissant et un angle de 90 degrés
    t.lt(18)  # Tourne la tortue vers la gauche de 18 degrés

# Calcule le périmètre de la dernière forme dessinée
perimetre = 2 * 3.1415 * (190 - (150 - 1))

# Calcule l'aire de la dernière forme dessinée
aire = 3.1415 * (190 - (150 - 1)) ** 2

# Affiche les résultats
print("Périmètre de la forme : ", perimetre)
print("Aire de la forme : ", aire)

# Attend que l'utilisateur ferme la fenêtre
turtle.done()
