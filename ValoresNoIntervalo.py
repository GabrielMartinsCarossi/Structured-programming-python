while True:
    n=int(input("Digite um número: "))
    if n>=0:
        if (n<=100):
            print("Número no intervalo [0, 100]")
        elif (n>=101) and (n<=200):
            print("Número no intervalo [101, 200]")
        elif (n>=201) and (n<=400):
            print("Número no intervalo [201, 400]")
        else:
            print("Número no intervalo [401, infinito]")
    else:
        print("Número negativo: ")
        break