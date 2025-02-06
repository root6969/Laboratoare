def suma_divizorilor_for(n):
    """Calculează suma divizorilor proprii ai unui număr n folosind un ciclu for."""
    total = 1  # Începem cu 1 deoarece 1 este un divizor al tuturor numerelor
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            total += i
    return total


def sunt_prietene_for(a, b):
    """Verifică dacă două numere sunt prietene folosind un ciclu for."""
    return suma_divizorilor_for(a) == b and suma_divizorilor_for(b) == a


def suma_divizorilor_while(n):
    """Calculează suma divizorilor proprii ai unui număr n folosind un ciclu while."""
    total = 1
    i = 2
    while i <= n // 2:
        if n % i == 0:
            total += i
        i += 1
    return total


def sunt_prietene_while(a, b):
    """Verifică dacă două numere sunt prietene folosind un ciclu while."""
    return suma_divizorilor_while(a) == b and suma_divizorilor_while(b) == a


def suma_divizorilor_do_while(n):
    """Simulează un ciclu do-while pentru calculul sumei divizorilor."""
    total = 1
    i = 2
    if n < 2:
        return total

    while True:
        if n % i == 0:
            total += i
        i += 1
        if i > n // 2:
            break
    return total


def sunt_prietene_do_while(a, b):
    """Verifică dacă două numere sunt prietene folosind o abordare do-while."""
    return suma_divizorilor_do_while(a) == b and suma_divizorilor_do_while(b) == a


# Citirea numerelor de la utilizator
numar1 = int(input("Introdu primul număr: "))
numar2 = int(input("Introdu al doilea număr: "))

# Verificare cu diferite structuri de buclă
print("\nFolosind ciclul for:")
print(f"{numar1} și {numar2} sunt prietene: {sunt_prietene_for(numar1, numar2)}")

print("\nFolosind ciclul while:")
print(f"{numar1} și {numar2} sunt prietene: {sunt_prietene_while(numar1, numar2)}")

print("\nFolosind simularea ciclului do-while:")
print(f"{numar1} și {numar2} sunt prietene: {sunt_prietene_do_while(numar1, numar2)}")
