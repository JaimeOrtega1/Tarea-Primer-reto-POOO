#Ejercicio 1#
#Análisis + Desarrollo Crea un script en el lenguaje de tu elección y encuentre la(s) cadena de texto que es(son) igual al revés en el siguiente texto:
#afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood

codigo = "afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"

print(tuple(codigo))
for i in reversed(codigo):
    print(tuple(i))
    contador = 0
    for x in i:
        contador += 1
print("Hay ",contador,"Cadenas iguales ")






#Ejercicio 2#

#Análisis + Desarrollo La serie de Fibonacci se construye utilizando la siguiente relación de recurrencia: Fn = Fn1 + Fn2, donde F1 = 1 y F2 = 1. Por ende, los primeros doce términos de esta serie son: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

#Ahora, consideremos los divisores de estos términos:

#1 = 1
#1 = 1
#2 = 1, 2
#3 = 1, 3
#5 = 1, 5
#8 = 1, 2, 4, 8
#13 = 1, 13
#21 = 1, 3, 7, 21
#34 = 1, 2, 17, 34
#55 = 1, 5, 11, 55
#89 = 1, 89
#144 = 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144

#Como se puede ver, 144 es el primer número de la serie de Fibonacci que tiene más de 10 divisores (de hecho tiene 15).
#Crea un script en tu lenguaje favorito que obtenga el primer número de Fibonacci que tiene más de 1000 divisores

def pideNumero():
    while True:
        n=int(input("Humano ingresa un numero mayor a 1:"))
        if n>1:
            return n

def generaFibonnaci(n):
    lista=[]
    for i in range(0,n):
        if i==0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[-2]+lista[-1])
    return lista

def muestraLista(lista):
    for i in lista:
        if(i!=lista[-1]):
            print(f"{i}",end="+")
        else:
            print(f"{i}")

n=pideNumero()

lista=generaFibonnaci(n)
print(lista)
muestraLista(lista)
contador = 0
suma = 0
for resultado in lista:
    suma += resultado
print("los divisores de ",suma)
for divisor in range(1,suma+1):
    if (suma % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("el numero ",suma," tiene ",contador," divisores")





#EJERCICIO 3#
#Análisis + Desarrollo Aplicado a Negocio Desarrolla una función o procedimiento que estime el tiempo de la entrega de una compra online (en días), en función de la distancia que existe entre una dirección de origen y destino.
# Suponga que los envíos siempre se despachan desde el mismo origen.Para la determinación de la distancia entre el origen y destino genere números aleatorios entre 0 km y 2.000 km Asuma que el tiempo de despacho está determinado por una sucesión numérica, donde cada N término se relaciona con un incremento en un rango de distancia entre la dirección de origen y de destino como se muesta a continuación.

#Rango 1. Menos de 100 km, se entregan el mismo día (Día cero)
#Rango 2. Menos de 200 km, se entregan al día siguiente (Día uno)
#Rango 3. Menos de 300 km, se entregan al día siguiente (Día uno)
#Rango 4. Menos de 400 km, se entregan al día subsiguiente (Día dos)
#Rango 5. Menos de 500 km, se entregan al tercer día (Día tres) ...
#Rango n. Menos de n km,
#Los días de entrega se calculan como la suma de los días de entrega de los rangos n–1 y n-2


import random

Origen = 0
Destino = int(input("Ingrese a cuantos metros esta el destino: "))

comenzar = random.randint(0,2000)

despacho = Destino - comenzar

if despacho < 100 :
    print("Rango 1")
    print("Se entregara el dia 0")
elif despacho < 200:
    print("Rango 2")
    print("Se entregara el dia 1")
elif despacho < 300:
    print("Rango 3")
    print("Se entregara el dia 1")
elif despacho < 400:
    print("Rango 4")
    print("Se entregara el dia 2")
elif despacho < 500:
    print("Rango 4")
    print("Se entregara el dia 3")
else:
    print("Rango",despacho)
    dias = 7
    while despacho < 23:
        dias += dias
        despacho -= despacho
    print("Se entregara el dia ",dias)