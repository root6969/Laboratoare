from collections import deque
from sortedcontainers import SortedSet, SortedDict # type: ignore
from Lab3 import Film # type: ignore

# Crearea a cel puțin cinci obiecte
filme = [
    Film.cu_toti_parametrii(1, "Inception", "Sci-Fi", "Christopher Nolan", 148, "USA"),
    Film.cu_toti_parametrii(2, "Avatar", "Fantasy", "James Cameron", 162, "USA"),
    Film.cu_toti_parametrii(3, "Titanic", "Romance", "James Cameron", 195, "USA"),
    Film.cu_toti_parametrii(4, "The Matrix", "Sci-Fi", "Lana Wachowski", 136, "USA"),
    Film.cu_toti_parametrii(5, "Interstellar", "Sci-Fi", "Christopher Nolan", 169, "USA")
]

# Adăugarea lor într-o listă (echivalentul ArrayList)
array_list = filme.copy()
print("ArrayList:", array_list)

# Adăugarea lor într-un deque (echivalentul LinkedList)
linked_list = deque(filme)
print("LinkedList:", linked_list)

# Sortarea automată a array_list
array_list.sort(key=lambda film: film.durata)
print("ArrayList sortat după durată:", array_list)

# Crearea a cel puțin trei obiecte și adăugarea lor într-o mulțime de tip SortedSet (echivalentul TreeSet)
tree_set = SortedSet(filme, key=lambda film: film.durata)
print("TreeSet:", tree_set)

# Adăugarea lor într-o mulțime de tip set (echivalentul HashSet)
hash_set = set(filme)
print("HashSet:", hash_set)

# Exemple de lucru cu dict (echivalentul HashMap)
hash_map = {film.nr: film for film in filme}
print("HashMap:", hash_map)

# Exemple de lucru cu SortedDict (echivalentul TreeMap)
tree_map = SortedDict({film.nr: film for film in filme})
print("TreeMap:", tree_map)

# Utilizarea iteratorului pentru a parcurge array_list
print("Parcurgerea ArrayList cu iteratorul:")
for film in array_list:
    print(film)

# Utilizarea comparatorului pentru a sorta filmele după denumire
array_list.sort(key=lambda film: film.denumire)
print("ArrayList sortat după denumire:", array_list)