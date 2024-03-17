# PREGUNTA 1
numeros_divisibles = []
for num in range (1500,2701):
    if num%5==0 and num%7==0:
        numeros_divisibles.append(num)
print('Los números que son divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:',numeros_divisibles)

# PREGUNTA 2
def patron_estrella(filas):
    for i in range(filas):
        print('*' * (i + 1))

    for i in range(filas - 1, 0, -1):
        print('*' * i)

patron_estrella(5)

# PREGUNTA 3
numeros = []
while True:
    respuesta = input('¿Desea ingresar un número? (SI/NO):' )
    if respuesta.upper() == 'SI':
        numero = int(input('Ingrese el número:' ))
        numeros.append(numero)
    elif respuesta.upper() == 'NO':
        break
    else:
        print("Respuesta inválida. Por favor, responda SI o NO.")

pares = 0
impares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print('Números ingresados:', numeros)
print('Cantidad de números pares:', pares)
print('Cantidad de números impares:', impares)

# PREGUNTA 4
def ingresar_alumnos(num_alumnos):
    alumnos = []
    for i in range(num_alumnos):
        nombre = input(f'Ingrese el nombre del alumno {i+1}:' )
        notas = []
        for j in range(3):
            nota = float(input(f'Ingrese la nota {j+1} para {nombre}:' ))
            notas.append(nota)
        alumno = {'Alumno': nombre, 'Notas': notas}
        alumnos.append(alumno)
    return alumnos

def mostrar_listado(alumnos):
    print('Listado de alumnos:' )
    for alumno in alumnos:
        print(f'Alumno:{alumno["Alumno"]}, Notas:{alumno["Notas"]}')

num_alumnos = int(input('Ingrese el número de alumnos:' ))
alumnos = ingresar_alumnos(num_alumnos)
mostrar_listado(alumnos)

# PREGUNTA 5
def contar_digitos(numero, digito):
    cantidad = str(numero).count(str(digito))
    return cantidad

numero_ingresado = int(input('Ingrese un número entero:' ))
digito = int(input('Ingrese un dígito:' ))

cantidad_digitos = contar_digitos(numero_ingresado, digito)
print(f'Cantidad de veces {digito} en el número: {cantidad_digitos}')

# PREGUNTA 6
def fibonacci_hasta_50():
    a, b = 0, 1
    fibonacci = [a, b]
    while True:
        c = a + b
        if c > 50:
            break
        fibonacci.append(c)
        a, b = b, c
    return fibonacci

serie_fibonacci = fibonacci_hasta_50()
print('Serie de Fibonacci hasta 50:',serie_fibonacci)

# PREGUNTA 7
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input('Ingrese un número:' ))
if es_primo(numero):
    print(f'{numero} es un número primo.')
else:
    print(f'{numero} no es un número primo.')

# PREGUNTA 8
def factorial(numero):
    if numero < 0:
        return 'El factorial no está definido para números negativos.'
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

def main():
    num = int(input('Ingrese un número entero no negativo:' ))
    print('El factorial de', num,'es:', factorial(num))

main()  

# PREGUNTA 9
def omitir_vocales(cadena):
    vocales = 'aeiouAEIOU'
    resultado = ''
    for letra in cadena:
        if letra not in vocales:
            resultado += letra
    return resultado

texto = input('Ingrese una cadena de texto:' )
texto_sin_vocales = omitir_vocales(texto)
print('Texto sin vocales:', texto_sin_vocales)