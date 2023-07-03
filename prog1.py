#  EX1 colonne pivot
def trouver_colonne_pivot(matrice):
    # Mise en place des variables
    nb_lignes = len(matrice)
    nb_colonnes = len(matrice[0])

    # Parcours de la dernière ligne
    for i in range(nb_colonnes):
        # Valeur de la cellule
        cellule = matrice[nb_lignes - 1][i]
        # Si Cij est positif, on renvoie l'indice de la colonne
        if cellule > 0:
            return i
    # Sinon, la fonction est maximale
    print("La fonction est maximale")
    return -1


# Ex2 TROUVER LE RATIO
def trouver_ratio_minimal(matrice, colonne_pivot):
    lignes = len(matrice)
    colonnes = len(matrice[0])

    indice_ratio_minimal = -1
    ratio_minimal = matrice[0][colonnes - 1] / matrice[0][colonne_pivot]

    for i in range(lignes):
        ratio = matrice[i][colonnes - 1] / matrice[i][colonne_pivot]
        if ratio_minimal > 0 and ratio <= ratio_minimal:
            ratio_minimal = ratio
            indice_ratio_minimal = i

    return indice_ratio_minimal


# Exo 3 fonction pivot
#  La fonction pivot prend en compte 3 paramètres:  une matrice initiale A, une ligne pivot p et une colonne pivot q
def pivot(A, p, q):
    # Nombre de lignes et de colonnes dans la matrice
    nb_lignes = len(A)
    nb_colonnes = len(A[0])

    # Création d'une nouvelle matrice pour stocker le résultat
    nouvelle_matrice = []
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            # Appliquer les opérations de pivotement
            if i == p and j == q:
                # Élément à la position du pivot
                element = 1 / A[p][q]
            elif i == p:
                # Ligne du pivot, calculer les éléments
                element = A[p][j] / A[p][q]
            elif j == q:
                # Colonne du pivot, calculer les éléments
                element = -A[i][q] / A[p][q]
            else:
                # Autres éléments de la nouvelle matrice
                element = A[i][j] - A[i][q] * A[p][j] / A[p][q]
            ligne.append(element)
        nouvelle_matrice.append(ligne)

        # Affichage de la matrice partielle après chaque pivotement
        # print("Matrice après pivotement :")
        # for ligne in nouvelle_matrice:
        #     print(ligne)
        # print("--------------------------")

    return nouvelle_matrice


# Ex4 métode du simplex, içi je vais utiliser les 3 méthodes précedemment implémentés pour réaliser la méthode du simplex
def simplex(matrice_simplex):
    # Nombre de lignes et de colonnes dans la matrice
    nb_lignes = len(matrice_simplex)
    nb_colonnes = len(matrice_simplex[0])

    # Boucle jusqu'à ce que la condition d'arrêt soit satisfaite
    while True:
        # Trouver la colonne pivot
        indice_colonne_pivot = trouver_colonne_pivot(matrice_simplex)
        if indice_colonne_pivot == -1:
            # La fonction est maximale
            print("La fonction est maximale.")
            break

        # Trouver le ratio minimal
        indice_ratio_minimal = trouver_ratio_minimal(
            matrice_simplex, indice_colonne_pivot
        )
        if indice_ratio_minimal == -1:
            # Le domaine n'est pas borné
            print("Le domaine n'est pas borné.")
            break

        # Effectuer le pivotement
        matrice_simplex = pivot(
            matrice_simplex, indice_ratio_minimal, indice_colonne_pivot
        )

    return matrice_simplex


# Exemple de matrice
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


#  exécute la fonction simplex,le résultat est stocké dans la variable matrice_resultat
# Lors de l'appel à la fonction simplex, je passe une copie de la matrice d'origine à chaque itération avec la méthode copy(),sinon la matrice d'origine  sera modifiée à chaque pivotement
matrice_resultat = simplex([ligne.copy() for ligne in matrice])
print("Matrice résultat :")
for ligne in matrice_resultat:
    print(ligne)
