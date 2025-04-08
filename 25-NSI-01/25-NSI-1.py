def voisins_entrants(adj, x):
    """
    Trouve les voisins entrants d'un sommet dans un graphe représenté par une liste d'adjacence.

    Args:
      adj: La liste d'adjacence du graphe.
      x: Le sommet cible.

    Returns:
      Une liste des sommets ayant une arête entrante vers x.
    """
    voisins = []
    for i in range(len(adj)):
        if x in adj[i]:
            voisins.append(i)
        i += 1
    return voisins

# Exemples d'utilisation :
adj = [[1, 2], [2], [0], [0]]
print(voisins_entrants(adj, 0))  # Output: [2, 3]
print(voisins_entrants(adj, 1))  # Output: [0]

def nombre_suivant(s):
  '''Renvoie le nombre suivant de celui representé par s
  en appliquant le procédé de lecture.'''
  resultat = ''
  chiffre = s[0]
  compte = 1
  for i in range(1, len(s)):
    if s[i] == chiffre:
      compte += 1
    else:
      resultat += str(compte) + chiffre
      chiffre = s[i]
      compte = 1
  lecture_chiffre = str(compte) + chiffre
  resultat += lecture_chiffre
  return resultat