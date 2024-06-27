"""
Conway's Game of Life
Pyhton 3.11.0

à faire :
- créer tableau
- créer jolie grille
- afficher tableau dans jolie grille
- changer couleur cases
- fonction prend état en cours et calcul le suivant
- bouton pour cette fonction et afficher nouvel état*
-
"""

import tkinter as tk

def nouvelle_grille(n):
    """crée une grille de taille n x n remplie de 0"""
    grille = []
    for i in range(n)

# Fonction pour enregistrer un nouveau contact
def enregistrer_contact():
    nom = champ_nom.get()
    email = champ_email.get()
    carnet.append((nom, email))
    afficher_contacts()

# Fonction pour afficher les contacts dans la listebox
def afficher_contacts():
    liste_contacts.delete(0, tk.END)
    for contact in carnet:
        liste_contacts.insert(tk.END, f"{contact[0]} - {contact[1]}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Carnet d'adresses")

# Variables Tkinter pour les champs de saisie
nom = tk.StringVar()
email = tk.StringVar()

# Champs de saisie pour le nom et l'email
tk.Label(fenetre, text="Nom :").grid(row=0, column=0)
champ_nom = tk.Entry(fenetre, textvariable=nom)
champ_nom.grid(row=0, column=1)

tk.Label(fenetre, text="Email :").grid(row=1, column=0)
champ_email = tk.Entry(fenetre, textvariable=email)
champ_email.grid(row=1, column=1)

# Bouton pour enregistrer un nouveau contact
tk.Button(fenetre, text="Enregistrer", command=enregistrer_contact).grid(row=2, column=0, columnspan=2)

# Listebox pour afficher les contacts
liste_contacts = tk.Listbox(fenetre)
liste_contacts.grid(row=3, column=0, columnspan=2)

# Liste de contacts (initialisation vide)
carnet = []

# Afficher les contacts initiaux (vides)
afficher_contacts()

# Boucle principale d'exécution
fenetre.mainloop()