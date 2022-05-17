print('Hallar la potencia de cualquier numero x')
numero=int(input('Ingrese un número: '))
potencia=int(input('Ingrese la potencia: '))
res=numero**potencia
print('La potencia del número: ', numero, 'es: ',round(res,2))


print('Ingresar cualquier numero y calcular su raiz cuadrada')
num1=int(input('Ingrese un número: '))
resul=num1**0.5
print('la raiz cuadrada de: ', num1,'es: ', round (resul, 2))



print('Probar si un numero es negativo')
num=int(input('Ingrese un número:'))
if num<0:
    print('El número',num,'es negativo')

else:
    print('El número',num,'no es negativo')


                        
print('Pedir al usuario su nombreysaludarlo')
nombre=input('Ingrese su nombre: ')
print('HOLA!!!', nombre)

print('volumen de la esfera')
radio=int(input('Ingrese el radio de la esfera:'))
resultadoo=((4/3)*3.1415*radio **3)
print('El volumen de la esfera es:',round(resultadoo,2))
