# Générateur de mot de passe par mouvement de la souris
# DAUMUR Guillaume SN2 C2

# Import des librairies
from tkinter import *
import random

# Liste des coordonnées de la souris
list_coord = []

# Fonction qui récupère les coordonnées de la souris au mouvement de la souris aprer un clic gauche
def detectMouv(event):
    chaine.configure(text = "En cours de génération...")
    # Ajout des coordonnées dans la liste list_coord
    list_coord.append(event.x)
    list_coord.append(event.y)
    # Création de points noirs sur le cadre pour montrer le mouvement de la souris
    cadre.create_oval(event.x, event.y, event.x+1, event.y+1, fill="black")
    
# Fonction exécutée au relachement du clic gauche
def affichMDP(event):
    # Si l'utilisateur n'a pas rentré de longueur de mot de passe alors on l'initialise à 10
    if choixNum.get() == "":
        lgMDP = 10
    # Sinon on récupère la longueur du mot de passe rentrée par l'utilisateur
    else:
        lgMDP = int(choixNum.get())
    # Si la longueur du mot de passe est supérieure à 115 alors on affiche un message d'erreur
    if lgMDP > 115:
        chaine.configure(text = "Le mot de passe est trop long")
    # Sinon on commence la génération du mot de passe 
    else:
        # Premier filtre :
        #  On choisit la moitié des coordonnées de la souris de manière aléatoire
        result1 = random.choices(list_coord, k = (len(list_coord)//2))
        # Deuxième filtre :
        # On crée une liste de lettres majuscules et minuscules et 3 caractères spéciaux : [ \ ]
        list_temp_lettre = []
        # On crée une liste de chiffres
        list_temp_num = []
        # On parcours la nouvelle liste de coordonnées
        for i in range(len(result1)):
            # Si le nombre est compris entre 65 et 93 ou 97 et 122 alors on ajoute sa valeur ASCII à la liste de lettres
            if 65 <= result1[i] <= 93 or 97 <= result1[i] <= 122:
                list_temp_lettre.append(chr(result1[i]))
            # Sinon on ajoute le nombre à la liste de chiffres
            else :
                list_temp_num.append(result1[i])
        # Troisième filtre :
        # On crée une liste qui mélange de façon aléatoire les lettres et les chiffres et les caractères spéciaux de : list_temp_lettre et list_temp_num
        list_melange = []
        n = 0
        # Tant que la longueur de la liste de mélange est inférieure à la longueur du mot de passe on continue de mélanger et d'ajouter les éléments
        while n < lgMDP/2:
            # On ajoute un élément à la liste de mélange grâce à un index aléatoire
            list_melange.append(list_temp_num[random.randrange(1, len(list_temp_num))])
            list_melange.append(list_temp_lettre[random.randrange(1, len(list_temp_lettre))])
            n+=1
        # On initialise le mot de passe final
        resultFinal = ""
        # On transforme la liste de mélange en mot de passe final
        for i in range(len(list_melange)):
            resultFinal += str(list_melange[i])
            # Condition pour ajouter un espace tous les 25 caractères afin de rendre le mot de passe plus lisible dans la fenêtre
            if i == 25 or i == 50 or i == 75 or i == 100 or i == 125 or i == 150 or i == 175 or i == 200:
                resultFinal += "\n"
        # On affiche le mot de passe final dans la fenêtre
        chaine.configure(text = resultFinal)
            
# Création de la fenêtre
fen = Tk()
# Titre de la fenêtre
fen.title("SignaScrypt")
# Taille de la fenêtre ( max et min)
fen.geometry("600x570")
fen.minsize(600, 570)
fen.maxsize(600, 570)

# Création d'un label afin de demander à l'utilisateur de rentrer la longueur du mot de passe
choixNum_label = Label(fen, text = "Choisissez la longueur du mot de passe", font = ("Helvetica 15")) 
choixNum_label.pack()
# On crée un input afin de récupérer la longueur du mot de passe
choixNum = Entry(fen, bd=5)
choixNum.pack()

# Création d'un cadre pour récupérer et afficher le mouvement de la souris
cadre = Canvas(fen, width =400, height =350, bg="light yellow")
# <B1-Motion>  => action du clic gauche enfoncé avec mouvement
cadre.bind("<B1-Motion>", detectMouv)
# <Button-1> => action du clic gauche relaché
cadre.bind("<ButtonRelease-1>", affichMDP)
cadre.pack()

# Affichage du mot de passe
mdp = Label(fen, text = "Mot de passe :", font = ("Helvetica 15 underline")) 
mdp.pack()
chaine = Label(fen)
chaine.pack()

# Button pour copier le mot de passe dans le presse papier
copy = Button(fen, text = "Copier le mot de passe", command = lambda: fen.clipboard_clear() or fen.clipboard_append(chaine.cget("text")))
copy.pack()

# Button pour réinitialiser le cadre afin de recommencer une nouvelle génération de mot de passe
reset = Button(fen, text = "Réinitialiser", command = lambda: cadre.delete("all") or chaine.configure(text = "") or list_coord.clear())
reset.pack()

# On affiche la fenêtre avec tout ces éléments
fen.mainloop()