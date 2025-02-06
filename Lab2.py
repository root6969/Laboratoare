def suma_diagonala_principala(matrice):
    suma = 0
    for i in range(len(matrice)):
        suma += matrice[i][i]
    return suma

# Functia de creare a unei matrice pătrate manual
def create_matrix(n):
    matrice = []
    for i in range(n):
        row = []
        for j in range(n):
            value = int(input(f"Introduceți valoarea pentru elementul [{i}][{j}]: "))
            row.append(value)
        matrice.append(row)
    return matrice

# Exemplu de utilizare
n = int(input("Introduceți dimensiunea matricei pătrate: "))
matrice = create_matrix(n)
# Afisare matrice
rezultat = suma_diagonala_principala(matrice)
print(f"Suma elementelor diagonalei principale este: {rezultat}")