a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))
print("")
delta = ((b**2) - 4*a*c)

raiz1 = ((b*-1) + (delta**(1/2)))/(2*a)

print("Raiz 1 é :", raiz1)

raiz2 = ((b*-1) - (delta**(1/2)))/(2*a)

print("Raiz 2 é :", raiz2)
print("")