import pickle
import os
from Lab3 import Film # type: ignore

FILENAME = 'filme.dat'

def create_file():
    with open(FILENAME, 'wb') as file:
        pickle.dump([], file)
    print("Fișierul a fost creat.")

def display_file():
    try:
        with open(FILENAME, 'rb') as file:
            filme = pickle.load(file)
            for film in filme:
                film.afisare()
                print()
    except FileNotFoundError:
        print("Fișierul nu există. Creați fișierul mai întâi.")

def add_data():
    try:
        with open(FILENAME, 'rb') as file:
            filme = pickle.load(file)
    except FileNotFoundError:
        filme = []

    nr = int(input("Introduceți numărul filmului: "))
    denumire = input("Introduceți denumirea filmului: ")
    gen = input("Introduceți genul filmului: ")
    regizor = input("Introduceți regizorul filmului: ")
    durata = int(input("Introduceți durata filmului (în minute): "))
    tara = input("Introduceți țara filmului: ")

    film = Film.cu_toti_parametrii(nr, denumire, gen, regizor, durata, tara)
    filme.append(film)

    with open(FILENAME, 'wb') as file:
        pickle.dump(filme, file)
    print("Datele au fost adăugate.")

def modify_data():
    try:
        with open(FILENAME, 'rb') as file:
            filme = pickle.load(file)
    except FileNotFoundError:
        print("Fișierul nu există. Creați fișierul mai întâi.")
        return

    nr = int(input("Introduceți numărul filmului de modificat: "))
    for film in filme:
        if film.nr == nr:
            film.denumire = input("Introduceți noua denumire a filmului: ")
            film.gen = input("Introduceți noul gen al filmului: ")
            film.regizor = input("Introduceți noul regizor al filmului: ")
            film.durata = int(input("Introduceți noua durată a filmului (în minute): "))
            film.tara = input("Introduceți noua țară a filmului: ")
            break
    else:
        print("Filmul nu a fost găsit.")

    with open(FILENAME, 'wb') as file:
        pickle.dump(filme, file)
    print("Datele au fost modificate.")

def delete_data():
    try:
        with open(FILENAME, 'rb') as file:
            filme = pickle.load(file)
    except FileNotFoundError:
        print("Fișierul nu există. Creați fișierul mai întâi.")
        return

    nr = int(input("Introduceți numărul filmului de șters: "))
    filme = [film for film in filme if film.nr != nr]

    with open(FILENAME, 'wb') as file:
        pickle.dump(filme, file)
    print("Datele au fost șterse.")

def process_data():
    try:
        with open(FILENAME, 'rb') as file:
            filme = pickle.load(file)
            for film in filme:
                if film.gen.lower() == "horror":
                    film.afisare()
                    print()
    except FileNotFoundError:
        print("Fișierul nu există. Creați fișierul mai întâi.")

def menu():
    while True:
        print("\nMeniu:")
        print("1. Creare fișier")
        print("2. Afișare conținut fișier")
        print("3. Adăugare date")
        print("4. Modificare date")
        print("5. Ștergere date")
        print("6. Prelucrare date (afișare filme horror)")
        print("7. Ieșire")
        optiune = input("Alegeți o opțiune: ")

        if optiune == '1':
            create_file()
        elif optiune == '2':
            display_file()
        elif optiune == '3':
            add_data()
        elif optiune == '4':
            modify_data()
        elif optiune == '5':
            delete_data()
        elif optiune == '6':
            process_data()
        elif optiune == '7':
            break
        else:
            print("Opțiune invalidă. Încercați din nou.")

if __name__ == "__main__":
    menu()