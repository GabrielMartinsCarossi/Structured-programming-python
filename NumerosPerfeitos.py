#Gabriel M Carossi
while True:
    n=int(input("Digite um número: "))
    if n >= 0:
        #testa se o número é par. 
        if n % 2 == 0:
            #1 e 2 já são divisores, a soma começa com 3.
            somaDivisores=3
            for i in range (3, n-1):
                if n % i == 0:
                    somaDivisores= somaDivisores + i

            if somaDivisores == n:
                print("O número é perfeito!\n")
            else:
                print("O número não é perfeito.\n")
        #números ímpares não são perfeitos.
        else:
            print("O número não é perfeito.\n")
        
    else:
        print("Número negativo!")
        break
        
