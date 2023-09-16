from pynput import mouse, keyboard
import tkinter as tk
from tkinter import messagebox,ttk
import pyautogui
import time
from PIL import Image,ImageTk

# Liste pour stocker les coordonnées des clics et les mots saisis au clavier
coordonnees_clics = []

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left or button == mouse.Button.right:
            coordonnee = (x, y, button)
            coordonnees_clics.append(coordonnee)

listener = mouse.Listener(on_click=on_click)

def on_key_release(key):
    try:
        key_str = key.char
        coordonnees_clics.append(key_str)
    except AttributeError:
        pass

keyboard_listener = keyboard.Listener(on_release=on_key_release)

def demarrer_bot():
    listener.start()
    keyboard_listener.start()  
    print("Bot en cours d'enregistrement...")
    demarrer_bot_button.config(state=tk.DISABLED)

def arreter_bot_et_executer():
    listener.stop()
    keyboard_listener.stop()  
    print("Arrêt de l'enregistrement du bot...")
    repetition = repetition_entry.get()  
    if not repetition.isdigit() or int(repetition) <= 0:
        messagebox.showerror("Erreur", "Le nombre de traitements n'est pas valide.")
    else:
        perform_bot_actions(int(repetition))
        print("Actions du bot terminées.")
        fenetre.destroy()  


def perform_bot_actions(repetition):
    print(f"Démarrage des actions du bot pour {repetition} répétitions...")
    for _ in range(repetition):
        for coord in coordonnees_clics:
            if isinstance(coord, tuple):
                x, y, button = coord
                
                if button == mouse.Button.left:
                    pyautogui.click(x, y)
                elif button == mouse.Button.right:
                    pyautogui.rightClick(x, y)
            elif isinstance(coord, str):
                
                pyautogui.write(coord)
            time.sleep(1)


# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.title("Bot de clics et de saisie au clavier")
style = ttk.Style()
style.configure("White.TFrame", background="white")



logo_image = Image.open("tt.png")
logo_image = logo_image.resize((150, 75))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(fenetre, image=logo_photo, highlightthickness=0  , bg="light gray")
logo_label.pack()


demarrer_bot_button = tk.Button(fenetre, text="Démarrer le bot", command=demarrer_bot)
demarrer_bot_button.pack(pady=10)


repetition_label = tk.Label(fenetre, text="Nombre de répétitions:")
repetition_label.pack()
repetition_entry = tk.Entry(fenetre)
repetition_entry.pack()

arreter_bot_button = tk.Button(fenetre, text="Arrêter le bot et exécuter", command=arreter_bot_et_executer)
arreter_bot_button.pack(pady=10)


fenetre.mainloop()
