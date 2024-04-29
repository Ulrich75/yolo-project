# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:01:41 2024

@author: Ldr
"""
"""
import tkinter as tk
from tkinter import filedialog
import subprocess
from PIL import Image, ImageTk

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 300))  # Resize l'image pour l'affichage
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        global selected_image_path
        selected_image_path = file_path

def execute_yolo():
    if selected_image_path:
        output_dir = filedialog.askdirectory(title="Sélectionner un dossier de sortie")
        if output_dir:
            subprocess.run(["yolo", "detect", "predict", "model=yolov8n.pt", f"source='{selected_image_path}'", f"--save-dir='{output_dir}'"])

# Création de la fenêtre principale
root = tk.Tk()
root.title("YOLOv8 Image Detection")

# Frame pour l'affichage de l'image sélectionnée
image_frame = tk.Frame(root)
image_frame.pack(pady=10)
image_label = tk.Label(image_frame)
image_label.pack()

# Bouton pour sélectionner une image
select_button = tk.Button(root, text="Sélectionner une image", command=select_image)
select_button.pack(pady=5)

# Bouton pour exécuter YOLOv8
execute_button = tk.Button(root, text="Go", command=execute_yolo)
execute_button.pack(pady=5)

# Chemin de l'image sélectionnée
selected_image_path = None

root.mainloop()
"""






import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Import de ttk pour les widgets Themed Tkinter
import subprocess
from PIL import Image, ImageTk

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 300))  # Resize l'image pour l'affichage
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        global selected_image_path
        selected_image_path = file_path

def execute_yolo():
    if selected_image_path:
        progress_bar.start()  # Démarre la barre de progression
        subprocess.run(["yolo", "detect", "predict", "model=yolov8n.pt", f"source='{selected_image_path}'"])
        progress_bar.stop()  # Arrête la barre de progression après l'exécution

# Création de la fenêtre principale
root = tk.Tk()
root.title("YOLOv8 Image Detection")
root.geometry("500x700")  # Fixe la taille de la fenêtre

# Configuration du style dark
root.configure(bg="#222222")

# Frame pour l'affichage de l'image sélectionnée
image_frame = tk.Frame(root, bg="#222222")
image_frame.pack(pady=10)

# Étiquette pour afficher l'image sélectionnée
image_label = tk.Label(image_frame, bg="#222222")
image_label.pack()

# Bouton pour sélectionner une image avec des radius
select_button = tk.Button(root, text="Sélectionner une image", command=select_image, bg="#008CBA", fg="white", borderwidth=0, relief=tk.RAISED, padx=10, pady=5, highlightthickness=0, bd=0, font=("Arial", 12), cursor="hand2")
select_button.pack(pady=5)

# Bouton pour exécuter YOLOv8 avec des radius
execute_button = tk.Button(root, text="Go", command=execute_yolo, bg="#4CAF50", fg="white", borderwidth=0, relief=tk.RAISED, padx=10, pady=5, highlightthickness=0, bd=0, font=("Arial", 12), cursor="hand2")
execute_button.pack(pady=5)

# Barre de progression avec ttk
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="indeterminate")
progress_bar.pack(pady=5)

# Chemin de l'image sélectionnée
selected_image_path = None

root.mainloop()