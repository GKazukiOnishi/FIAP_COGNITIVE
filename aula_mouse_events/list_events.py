# Dica python como usar um list comprehensions no python e a função built-in dir()

import cv2
import numpy as np

# A função dir() devolte todas propriedades e métodos de um objeto especifico
#print(len(dir(cv2)))
#print (dir(cv2))


# Vamos varrer o objeto cv2 e filtrar apenas os métodos que tem relação com EVENT
eventos = []
for i in dir(cv2):
    if 'EVENT' in i:
        eventos.append(i)
print(eventos)
print(len(eventos))

# Usando List comprehension
# Devolve uma lista na variavel events filtando os dados de outra lista

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print( events )


