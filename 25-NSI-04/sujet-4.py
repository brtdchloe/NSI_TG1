def ecriture_binaire_entier_positif(n : int) -> str:
    n_str = ''
    while n > 0:
        n_str = str(n%2) + n_str
        n = n // 2
    return n_str

def echange(tab, i, j):
  '''Echange les éléments d'indice i et j dans le tableau tab.'''
  temp = tab[i]
  tab[i] = tab[j]
  tab[j] = temp

def tri_bulles(tab):
  '''Trie le tableau tab dans l'ordre croissant
  par la méthode du tri à bulles.'''
  n = len(tab)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if tab[j] > tab[j + 1]:
        echange(tab, j, j + 1)
  return tab