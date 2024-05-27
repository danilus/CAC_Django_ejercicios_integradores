from django.db import models

# Create your models here.


'''
1. Escribir una función que calcule el máximo común divisor entre dos números.
'''

def get_mcd(num1, num2):
    a = num1
    b = num2
    temp = a
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


'''
2. Escribir una función que calcule el mínimo común múltiplo entre dos números
'''
def get_mcm(num1, num2):
    mcd = get_mcd(num1, num2)
    return int((num1 * num2) / mcd)


'''
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

# RESUELTO EN VIEWS


'''
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
'''

def get_contar_palabras_dict(text):
    words_dict = {}
    trans_table = text.maketrans('','',string.punctuation)
    texto = text.lower().translate(trans_table)
    
    for word in texto.split():
        words_dict[word] = words_dict.get(word, 0) + 1
    
    return words_dict

def get_palabra_popular_tuple(words_dict):
    popular_word_tuple = ()

    max_quant = 0
    for word, quant in words_dict.items():
        if quant > max_quant:
            max_quant = quant
            popular_word_tuple = (word, quant)
    return popular_word_tuple


'''
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
'''

# NO COMPRENDÍ ESTE ENUNCIADO


'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def __str__(self):
        return self.get_nombre()
    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        assert isinstance(nombre, str), 'Nombre debe ser un string'
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        assert isinstance(edad, int), 'Edad debe ser un entero'
        self.__edad = edad

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        assert isinstance(dni, int), 'DNI debe ser un entero'
        self.__dni = dni
    
    def mostrar(self):
        return 'Nombre: ' + self.get_nombre() + ' / ' + 'Edad: ' + str(self.get_edad()) + ' / ' + 'DNI: ' + str(self.get_dni())
    
    def es_mayor_de_edad(self):
        return self.__edad >= 18
    

'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''

class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        assert isinstance(titular, Persona), 'Titular debe ser una Persona'
        self.__titular = titular
        try:
            cantidad = float(cantidad)
        except ValueError:
            raise ValueError('Cantidad debe ser un Float o convertible a Float')
        except TypeError:
            raise TypeError('Cantidad debe ser un Float o convertible a Float')
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    # En el enunciado dice crear los setters y getters
    # pero también dice que no se deben poder modificar los datos directamente, es confuso, dejo comentado por las dudas
    #def set_titular(self, titular):
    #    assert isinstance(titular, Persona), 'Titular debe ser una Persona'
    #    self.__titular = titular

    def get_cantidad(self):
        return self.__cantidad

    # En el enunciado dice crear los setters y getters
    # pero también dice que no se deben poder modificar los datos directamente, es confuso, dejo comentado por las dudas
    #def set_cantidad(self, cantidad):
    #    assert isinstance(cantidad, float), 'Cantidad debe ser un Float'
    #    self.__cantidad = cantidad

    def mostrar(self):
        return f"Titular: {str(self.get_titular())} / Cantidad: {str(self.get_cantidad())}"
    
    def ingresar(self, cantidad):
        try:
            cantidad = float(cantidad)
        except ValueError:
            raise ValueError('Cantidad debe ser un Float o convertible a Float')
        except TypeError:
            raise TypeError('Cantidad debe ser un Float o convertible a Float')
            
        if float(cantidad) >= 0.0:
            self.__cantidad += cantidad
            return f"Se ingresaron {str(cantidad)} a la Cuenta. Saldo actual: {str(self.get_cantidad())}."
        else:
            return 'Cantidad negativa. No se realizó ninguna acción.'
    
    def retirar(self, cantidad):
        try:
            cantidad = float(cantidad)
        except ValueError:
            raise ValueError('Cantidad debe ser un Float o convertible a Float')
        except TypeError:
            raise TypeError('Cantidad debe ser un Float o convertible a Float')

        self.__cantidad -= cantidad
        return f"Se retiraron {str(cantidad)} de la Cuenta. Saldo actual: {str(self.get_cantidad())}."

'''
p1 = Persona('Dan', 44, 28285435)
print(p1.mostrar())

c1 = Cuenta(p1, 123)
print(c1.mostrar())

print(c1.ingresar(210))
print(c1.mostrar())

print(c1.retirar(33))
print(c1.mostrar())

print(c1.ingresar(-30.0))
print(c1.mostrar())

print(c1.retirar(319.5))
print(c1.mostrar())
'''


'''
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
'''

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion=0):
        super().__init__(titular, cantidad)
        try:
            bonificacion = int(bonificacion)
        except ValueError:
            raise ValueError('Bonificacion debe ser un Entero o convertible a Entero')
        assert 0 <= bonificacion < 100, 'Bonificación debe estar entre 0 y 100 pues es un porcentaje'
        self.__bonificacion = bonificacion
        
    def get_bonificacion(self):
        return self.__bonificacion
        
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def es_titular_valido(self):
        return 18 <= self.get_titular().get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            return super().retirar(cantidad)
        else:
            return 'No es posible retirar pues el Titular de esta Cuenta Joven no es válido'

    def mostrar(self):
        #print(f"Cuenta Joven. Bonificacion: {self.get_bonificacion()}%")
        return f"Cuenta Joven. Bonificacion: {self.get_bonificacion()}%"

'''
p1 = Persona('Dan', 44, 28285435)
p2 = Persona('Simón', 13, 99999999)
p3 = Persona('Marti', 18, 77777777)

cj = CuentaJoven(p3, 120, 15)
print(cj.mostrar())
print(cj.get_cantidad())
print(cj.retirar(20))
print(cj.ingresar(10))
print(cj.get_cantidad())
'''