from django.shortcuts import render

import string

from .functions_and_classes import *


def home(request):
    return render(request, 'app_main/home.html')


'''
1. Escribir una función que calcule el máximo común divisor entre dos números.
'''

def mcd(request):
    rta = None
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        rta = get_mcd(int(num1), int(num2))

    return render(request, 'app_main/max_com_div.html', {'rta': rta, 'num1': num1, 'num2': num2})


'''
2. Escribir una función que calcule el mínimo común múltiplo entre dos números
'''

def mcm(request):
    rta = None
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        rta = get_mcm(int(num1), int(num2))

    return render(request, 'app_main/min_com_mul.html', {'rta': rta, 'num1': num1, 'num2': num2})


'''
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

def contar_palabras(request):
    words_dict = {}
    if request.method == 'POST':
        trans_table = request.POST.get('texto').maketrans('','',string.punctuation)
        texto = request.POST.get('texto').lower().translate(trans_table)
        
        for word in texto.split():
            words_dict[word] = words_dict.get(word, 0) + 1
    return render(request, 'app_main/contar_palabras.html', {'words': words_dict})


'''
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
'''

def palabra_popular(request):
    popular_word_tuple = ()
    if request.method == 'POST':
        word_dict = get_contar_palabras_dict(request.POST.get('texto'))
        popular_word_tuple = get_palabra_popular_tuple(word_dict)

    return render(request, 'app_main/palabra_popular.html', {'popular_word_tuple': popular_word_tuple})


'''
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
'''

def value_error(request):
    return render(request, 'app_main/value_error.html')


'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

def persona(request):
    p = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        dni = request.POST.get('dni')
        p = Persona(nombre, edad, dni)

    return render(request, 'app_main/persona.html', {
        'persona': p,
    })


'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''

def cuenta(request):
    p = Persona('Danilo', 44, 27285435)
    c = Cuenta(p)
    cantidad = None
    initial = True
    if request.method == 'POST':
        initial = False
        cantidad = request.POST.get('cantidad')
        operation = request.POST.get('operation')
        if operation == 'ingresar':
            c.ingresar(cantidad)
        elif operation == 'retirar':
            c.retirar(cantidad)

    return render(request, 'app_main/cuenta.html', {
        'persona': p,
        'cuenta': c,
        'initial': initial,
    })



'''
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
'''

def cuenta_joven(request):
    return render(request, 'app_main/cuenta_joven.html')