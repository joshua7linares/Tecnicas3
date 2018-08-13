num1=int(input("introduce un numero---------"))
num2=int(input("introduce otro numero--------"))

print ("que operacion deseas realizar")
print ("1. suma")
print ("2. resta")
print ("3. multiplicacion")
print ("4. division")

opcion = int(input("elije una opcion-----"))
if opcion ==1:
    suma=num1+num2
    print("el resultado es-------",suma)

elif opcion ==2:
    resta=num1-num2
    print("el resultado es-------",resta)


elif opcion ==3:
    mult=num1*num2
    print("el resultado es-------",mult)


elif opcion ==4:
    div=num1/num2
    print("el resultado es-------",div)
