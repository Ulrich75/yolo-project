# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:01:41 2024

@author: Ldr
"""

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import ultralytics

# Fonction pour charger l'image sélectionnée
def charger_image():
    global image_path, image_tk
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    image_tk = ImageTk.PhotoImage(image)
    image_label.configure(image=image_tk)

# Fonction pour exécuter YOLOv8 et afficher les résultats
def detecter_objets():
    model = ultralytics.yolov8n.load_model("yolov8n.pt")
    results = model.predict(image_path)
    # Affichage des résultats (à compléter)

# Interface graphique
fenetre = Tk()
fenetre.title("Détection d'Objets avec YOLOv8")

# Zone de sélection d'image
bouton_charger = Button(fenetre, text="Sélectionner une image", command=charger_image)
bouton_charger.pack()
# Zone de bouton pour la détection
bouton_detecter = Button(fenetre, text="Détecter des objets", command=detecter_objets)
bouton_detecter.pack()

# Zone d'affichage de l'image
image_label = Label(fenetre)
image_label.pack()


fenetre.mainloop()
