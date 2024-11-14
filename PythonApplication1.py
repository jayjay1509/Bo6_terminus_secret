# -*- coding: utf-8 -*-
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Fonctions de calcul
def calculate(x, y, z):
    first = 2 * x + 11
    second = (2 * z + y) - 5
    third = abs((y + z) - x)
    return first, second, third

# Fonction pour afficher le code
def show_code():
    if x_val.get() is None or y_val.get() is None or z_val.get() is None:
        messagebox.showwarning("Attention", "Veuillez selectionner une image pour chaque valeur de base.")
        return

    first, second, third = calculate(x_val.get(), y_val.get(), z_val.get())
    code = f"{first}{second}{third}"
    messagebox.showinfo("Code", f"Votre code est : {code}")

# Fonction pour s�lectionner une image et afficher un carre autour
def select_image(val, var, label, canvas, img):
    var.set(val)
    # Effacer le carre vert autour de la precedente image selectionnee
    if label:
        canvas.delete(label)
    # Dessiner un carre vert autour de l'image selectionnee
    label = canvas.create_rectangle(5, 5, 105, 105, outline="green", width=3)
    # Changer l'image affichee pour celle selectionnee
    canvas.create_image(50, 50, image=img)
    return label

# Initialiser la fenetre principale
root = tk.Tk()
root.title("Calculateur de Code")

# Variables pour stocker les valeurs selectionnees
x_val = tk.IntVar(value=None)
y_val = tk.IntVar(value=None)
z_val = tk.IntVar(value=None)

# Charger les images et assigner les valeurs
image_dir = os.path.dirname(__file__)  # Dossier où se trouve le script Python
image_values = {
    1: 0,
    2: 10,
    3: 11,
    4: 22,
    5: 21,
    6: 20
}

images = []
for i in range(1, 7):
    img_path = os.path.join(image_dir, f"T{i}.png")  # Crée le chemin relatif vers chaque image
    if os.path.exists(img_path):  # Vérifie si l'image existe
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        images.append((img, image_values[i]))
    else:
        print(f"Image {img_path} non trouvée.")

# Creer les canvases pour afficher les images
canvas_x = tk.Canvas(root, width=110, height=110)
canvas_y = tk.Canvas(root, width=110, height=110)
canvas_z = tk.Canvas(root, width=110, height=110)
canvas_x.pack(side="left", padx=5)
canvas_y.pack(side="left", padx=5)
canvas_z.pack(side="left", padx=5)

# Variables pour memoriser le carre vert autour des images
label_x = None
label_y = None
label_z = None

# Afficher les images par defaut dans les canvases
def load_images():
    for img, _ in images:
        canvas_x.create_image(50, 50, image=img)
        canvas_y.create_image(50, 50, image=img)
        canvas_z.create_image(50, 50, image=img)

load_images()

# Creer les boutons pour chaque image et gerer la selection
frame_x = tk.Frame(root)
frame_x.pack(pady=10)
frame_y = tk.Frame(root)
frame_y.pack(pady=10)
frame_z = tk.Frame(root)
frame_z.pack(pady=10)

tk.Label(frame_x, text="Selectionnez une image pour x :").pack()
tk.Label(frame_y, text="Selectionnez une image pour y :").pack()
tk.Label(frame_z, text="Selectionnez une image pour z :").pack()

# Creer les boutons pour chaque image et gerer la selection
for i, (img, value) in enumerate(images):
    # Ajouter un bouton pour chaque image dans chaque groupe
    tk.Button(frame_x, image=img, command=lambda value=value, img=img: select_image(value, x_val, label_x, canvas_x, img)).pack(side="left", padx=5)
    tk.Button(frame_y, image=img, command=lambda value=value, img=img: select_image(value, y_val, label_y, canvas_y, img)).pack(side="left", padx=5)
    tk.Button(frame_z, image=img, command=lambda value=value, img=img: select_image(value, z_val, label_z, canvas_z, img)).pack(side="left", padx=5)

# Bouton pour calculer le code
btn_calculate = tk.Button(root, text="Calculer le Code", command=show_code)
btn_calculate.pack(pady=20)

# Lancer la boucle principale
root.mainloop()
