def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(notes)): 
        if notes[i] == note_maxi: 
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]] 

    return (note_maxi, meilleurs_eleves)

def fibonacci(n):
  """
  Calcule le terme d'indice n de la suite de Fibonacci.

  Args:
    n: Un entier strictement positif.

  Returns:
    Le terme d'indice n de la suite de Fibonacci.
  """
  nb = 1
  fibo = 1
  for i in range(2,n):
      nb, fibo = fibo, fibo + nb
  return fibo