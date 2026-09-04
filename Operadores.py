"""
Operadores
"""
# Operadores Aritmeticos
sum = 10 + 3
print("El resultado de sumar 10 + 3 es = ", sum)
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3 }")
print(f"Division entero: 10 // 3 = {10 // 3}")

# Operadores de comparacion
print(f"Igualda: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores logicos 
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4} ")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignacion 
my_number = 11 # asignacion
print(my_number)
my_number += 1 # suma y asignacion
print(my_number)
my_number -= 1 # resta y asignacion 
print(my_number)
my_number *= 2 # multiplicacion y asignacion
print(my_number)
my_number /= 2 # Division y asignacion 
print(my_number)
my_number %= 2 # Modulo y asignacion
print(my_number)
my_number ** 2 # exponente y asignacion 
print(my_number)
my_number //= 2 # Division entera y asignacion
print(my_number)    

# Operadores de identidad
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not  my_new_number}")

# operadores de pertenencia
print(f"u in 'moure' ={'u' in 'moure'}") # busca y compara si pertenece el elemento u en la palabra 'moure'
print(f"b not in 'moure' ={'b' not in 'moure'}") # busca y compara si no pertenece el elemento b en la palabra 'moure'

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # '0010'compara los binarios de los numeros y si son iguales es 1 sino es 0 que es 2
print(f"OR: 10 | 3 = {10 | 3}") # '1011'compara los binarios de los numeros y si en alguno tiene un 1 es 1 pero si ambos son 0 el valor es 0 
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # '1001' compara los binarios de los numerosy si un valor es 1 coloca 0 y si es 0 coloa 1
print(f"NOT: ~10 = {~10}") # niega cada uno de los bit del numero donde pasamos de 00001010 a 11110101 recordando que la linea es de 8 bit
print(f"Desplazamiento a la derecha: 10 >> 2 ={10 >> 2}") # pasamos de 1010 a 0101 luego 0010
print(f"Desplazamiento a la izquierda: 10 << 2 ={10 << 2}") # pasamo de 1010 a 101000