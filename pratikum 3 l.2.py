
import math

a= int(input("masukan nilai dari A = "))
b= int(input("masukan nilai dari B = "))
c= int(input("masukan nilai dari C = "))

if (a == 0):
    print("Bukan merupakan persamaan kuadrat, karena nilai A =" + str(a))
else:
    D = pow(b, 2)-(4*a*c)
    if (D > 0):
        x1 = ((-b)+math.sqrt(D))/(2*a)
        x2 = ((-b)-math.sqrt(D))/(2*a)
        print("persamaan kuadrat " + str(a) + "x2 +" + str(b) + "x + " + str(c))
        print("determinannya = " + str(D))
        print("memiliki akar berbeda")
        print("akar x1 = " + str(x1))
        print("akar x2 = " + str(x2))
    elif (D == 0):
        x1 = (-b)/(2*a)
        x2 = x1
        print("persamaan kuadrat " + str(a) + "x2 +" + str(b) + ")x + " + str(c))
        print("determinannya = " + str(D))
        print("merupakan akar kembar")
        print("akar = " + str(x2))
    elif (D < 0):
        print("persamaan kuadrat " + str(a) + "x2 +" + str(b) + "x + " + str(c))
        print("determinannya = " + str(D))
        print("merupakan akar imaginer")
        print("akar x1 = -" + str(b) + " + √" + str(D) + "/2*" + str(a))
        print("akar x2 = -" + str(b) + " + √" + str(D) + "/2*" + str(a))
    else:
        print("error, masukan angka yang valid")