print(" ")
print("Nombre: Ruvalcaba Valverde Miguel Angel")
print("--------------Punto 7-----------------")
N = int(input("ingresa un numero natural:"))#Capturemos el un numero, No vejetal ni frutal sino natural =)
if N == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12:#qui me dio flojera, pero en resumen el or te permite poner otras posibilidades de objeto
    print("este numero natural esta entre 0 y 12")
    print(N)
else:#Si el valor es mayor que 12 se activa esto, esta es su opcion por default
    print("el numero natural ingresado no esta entre 0 y 12")
    print(N)

print("--------------Punto 8-----------------")
N1 = int(input("ingresa un numero:"))#Capturemos el un numero.
if N1 % 2 == 1:#Ahora con el modulo se hase una operacion que si el resultado es 1 sera un numero impar.
    print("Numero impar:",N1)
else:#como es un default, solo los numeros par apareseran qui.
    print("Numero par:",N1)
#este cuando lo estaba hasiendo en clase, me estaba doliendo la cabesa ya que no se me ocurian ideas y luego me dije,
#espera ya hisimos esto, y como adivino me llega el recuerdo, pongo esto qui porque es algo chisotso.
print("--------------Punto 9-----------------")
N2 = int(input("ingresa un numero:"))#Capturemos el un numero.
if N2 % 7 == 0:#se abre un if,con el modulo se hase una operacion que derminara si el resultado es divisible por 7
    print("Este numero es divisible entre 7",N2)#Nota: creo que el modulo(%) me esta emepsadon a caer bien, Nota: si el modul me permite coroborar relasiones entre resultados futuros, me podria servir para algo especial que estoy hasiendo?
else:#opcion de default con else
    print("Este numero no es divisible entre 7",N2)

if N2 > 40:#se abre un if que determina si el valor es mayor que 40
    print("Pero este numero es mayor que 40:",N2)
else:#opcion de default con else
    print("Pero este no es mayor que 40",N2)
print("--------------Punto 10-----------------")
import math #qui importo la opcion math a la mesa, pero nesitamos contexto
#esta fue la segunda que mas me carcomio la cabeza y se me ocurio una gran idea
#busque Python factorial W3schools, y aprendi esto pero al prinsipio intente usar un for, 
#ya estaba medio practicando con el pero llege a la conclusion de que no me servira hehe
N3 = int(input("Vamos a elije un numero para sacar su factorial:"))#Capturemos el un numero.
print("La Factorial de",N3,"es",math.factorial(N3))#con esta funcion, podermos haser que el valor ingresado o capturado, optenga su factorial
#pero veo algo obligatorio explicar esto.
#math es un modilo dentro de pyhton que te trai barias funsiones matematicas mas complejas como el factorial.
