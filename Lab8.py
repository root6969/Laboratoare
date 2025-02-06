import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Entry, Button, PhotoImage
import pickle
from Lab3 import Film # type: ignore
import os

# Numele fișierului în care se vor salva datele
FILENAME = 'A:/Laboratoare/filme.dat'
# Calea către fișierul pictogramă
ICON_PATH = 'A:/Laboratoare/icon.png'

class FilmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionare Filme")
        
        # Adăugarea pictogramei la aplicație
        self.icon = PhotoImage(file=ICON_PATH)
        self.root.iconphoto(False, self.icon)
        
        # Crearea widget-urilor interfeței grafice
        self.create_widgets()
        # Încărcarea filmelor din fișier
        self.load_films()

    def create_widgets(self):
        # Crearea unui listbox pentru afișarea filmelor
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.pack(pady=10)

        # Stilul butoanelor
        button_style = {'padx': 10, 'pady': 5, 'bg': 'lightblue', 'fg': 'black', 'font': ('Arial', 12), 'width': 20}

        # Crearea butonului pentru adăugarea unui film
        self.add_button = tk.Button(self.root, text="Adaugă Film", command=self.add_film, **button_style)
        self.add_button.pack(pady=5)

        # Crearea butonului pentru ștergerea unui film
        self.delete_button = tk.Button(self.root, text="Șterge Film", command=self.delete_film, **button_style)
        self.delete_button.pack(pady=5)

        # Crearea butonului pentru modificarea unui film
        self.modify_button = tk.Button(self.root, text="Modifică Film", command=self.modify_film, **button_style)
        self.modify_button.pack(pady=5)

        # Crearea butonului pentru afișarea filmelor de genul horror
        self.process_button = tk.Button(self.root, text="Afișează Filme Horror", command=self.process_films, **button_style)
        self.process_button.pack(pady=5)

        # Crearea butonului pentru salvarea filmelor în fișier
        self.save_button = tk.Button(self.root, text="Salvează Filme", command=self.save_films, **button_style)
        self.save_button.pack(pady=5)

    def load_films(self):
        # Încărcarea filmelor din fișier
        try:
            with open(FILENAME, 'rb') as file:
                self.films = pickle.load(file)
                for film in self.films:
                    self.listbox.insert(tk.END, film.denumire)
        except FileNotFoundError:
            self.films = []

    def add_film(self):
        # Afișarea dialogului pentru adăugarea unui film
        self.show_film_dialog()

    def delete_film(self):
        # Ștergerea filmului selectat din listbox și din lista de filme
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            del self.films[selected_index[0]]
        else:
            messagebox.showwarning("Atenție", "Selectați un film pentru a șterge.")

    def modify_film(self):
        # Modificarea filmului selectat din listbox și din lista de filme
        selected_index = self.listbox.curselection()
        if selected_index:
            film = self.films[selected_index[0]]
            self.show_film_dialog(film, selected_index[0])
        else:
            messagebox.showwarning("Atenție", "Selectați un film pentru a modifica.")

    def process_films(self):
        # Afișarea filmelor de genul horror
        horror_films = [film for film in self.films if film.gen.lower() == "horror"]
        if horror_films:
            messagebox.showinfo("Filme Horror", "\n".join(film.denumire for film in horror_films))
        else:
            messagebox.showinfo("Filme Horror", "Nu există filme de genul horror.")

    def save_films(self):
        # Salvarea filmelor în fișier
        with open(FILENAME, 'wb') as file:
            pickle.dump(self.films, file)
        messagebox.showinfo("Salvare", "Filmele au fost salvate.")

    def show_film_dialog(self, film=None, index=None):
        # Afișarea dialogului pentru adăugarea sau modificarea unui film
        dialog = Toplevel(self.root)
        dialog.title("Detalii Film")

        labels = ["Număr", "Denumire", "Gen", "Regizor", "Durată (minute)", "Țară"]
        entries = []

        for i, label in enumerate(labels):
            Label(dialog, text=label).grid(row=i, column=0, padx=10, pady=5)
            entry = Entry(dialog)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        if film:
            entries[0].insert(0, film.nr)
            entries[1].insert(0, film.denumire)
            entries[2].insert(0, film.gen)
            entries[3].insert(0, film.regizor)
            entries[4].insert(0, film.durata)
            entries[5].insert(0, film.tara)

        def save():
            # Salvarea datelor introduse în dialog
            nr = int(entries[0].get())
            denumire = entries[1].get()
            gen = entries[2].get()
            regizor = entries[3].get()
            durata = int(entries[4].get())
            tara = entries[5].get()

            new_film = Film.cu_toti_parametrii(nr, denumire, gen, regizor, durata, tara)

            if index is not None:
                self.films[index] = new_film
                self.listbox.delete(index)
                self.listbox.insert(index, new_film.denumire)
            else:
                self.films.append(new_film)
                self.listbox.insert(tk.END, new_film.denumire)

            dialog.destroy()

        Button(dialog, text="Salvează", command=save).grid(row=len(labels), columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FilmApp(root)
    root.mainloop()