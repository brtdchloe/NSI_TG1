def max_et_indice_while(tab: list) -> tuple:
    maxi = tab[0]  # Initialisation de maxi avec le premier élément du tableau
    max_occ = 0
    i = 1  # On commence à l'indice 1
    while i < len(tab):
        if tab[i] > maxi:
            maxi = tab[i]
            max_occ = i
        i += 1  # On passe à l'élément suivant
    return maxi, max_occ

def max_et_indice_for(tab: list) -> tuple:
    maxi = tab[0]  # Initialisation de maxi avec le premier élément du tableau
    max_occ = 0
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            max_occ = i
    return maxi, max_occ

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon
    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = [] 

    for x in tab:
        if x < 1 or x > n or tab == []: 
            return False
        vus.append(x) 
    return True

def nombre_points_rupture(ordre):
  '''
  Renvoie le nombre de point de rupture de ordre qui représente
  un ordre de gènes de chromosome
  '''
  # On vérifie que ordre est un ordre de gènes
  assert est_un_ordre(ordre)
  n = len(ordre)
  nb = 0
  if ordre[0] != 1: # Le premier n'est pas 1
    nb = nb + 1
  i = 0
  while i < n - 1:
    if ordre[i + 1] - ordre[i] not in [-1, 1]: # L'écart n'est pas 1
      nb = nb + 1
    i = i + 1
  if ordre[n - 1] != n: # Le dernier n'est pas n
    nb = nb + 1
  return nb