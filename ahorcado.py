"""
Ahorcado:

Crear un juego por consola donde inicalmente se pida al jugador eligir entre dos dificultades ("Facil" o "Dificil").
El programa debe tener preestablecido dos conjuntos de palabras uno para cada dificultad.
los cuales no pueden ser visibles para el jugador. Las faciles son de hasta 6 letras y de 7 letras o mas
son palabras dificiles
Cada vez que se ejecuta el juego debe mostrar una palabra al azar de las palabras predefinidas.
Inicialmente se muestran "_" por la cantidad de letras de la palabra al azar
Cuando inicia el juego se debe pedir al jugador una letra a la vez y en caso de que adivine irla poniendo en la posicion
(o posiciones) de la palabra al azar elegida por el juego
El juego se gana cuando se complete la palabra
"""

import random

print('Bievenido al juego del ahorcado')

print('Elige la dificultad')
print('1.', 'Facil')
print('2.', 'Dificil')

# 1. Elegir la dificultad

dificultad = int(input('Elige una dificulta '))

faciles = ('llavero', 'abejas', 'bancos', 'balon', 'avispo', 'balboa')
sisas = ''
dificiles = ('dinosaurio', 'kilogramo', 'kilometro', 'ornitorrinco', 'quesadilla', 'unicornio')

# 2. De acuerdo a la dificultad generar una palabra al azar


while dificultad != 1 or dificultad != 2:
    if dificultad == 1:
       print('Escogistes la opción facil ahora adivinar')
       sisas = random.choice(faciles)
    elif dificultad == 2:
        print('Escogistes la opción dificil ahora adivinar')
        sisas = random.choice(dificiles)
    else:
        print('No escogiste ninguna opcion')
        
        print('Escoje la opción')
        dificultad = int(input('Elige una dificulta '))
    break




 



intentos = 0

palabra_ingresada = '*' * len(sisas)

while palabra_ingresada != sisas:
    print(f'Intento {intentos}')
    print(palabra_ingresada)

    # 3. Pedir una letra al jugador
    letra = input('Ingresa una letra ')
    letra = letra.lower()

    intentos += 1

    # 4. Si la letra esta en la palabra, colocarla en el lugar que corresponde de la palabra al azar
    if letra in sisas:
        nueva_palabra = [c for c in palabra_ingresada]
        for i in range(len(sisas)):
            if letra == sisas[i]:
                nueva_palabra[i] = letra
            elif nueva_palabra[i] == '*':
                nueva_palabra[i] = '*'
            else:
                continue

        palabra_ingresada = ''.join(nueva_palabra)
    else:
        print(f'la letra {letra} no está en la palabra')


print(f"Haz adivinado la palabra {palabra_ingresada.upper()}")
"""
Algoritmo
1. Elegir la dificultad
2. De acuerdo a la dificultad generar una palabra al azar
3. Pedir una letra al jugador
4. Si la letra esta en la palabra colocarla en el lugar que corresponde de la palabra al azar
5. Repetir 3 y 4 hasta completar la palabra
"""




  


   
                
            
            
