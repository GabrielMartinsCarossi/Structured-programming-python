#   Programa M2 Gabriel   #

from abc import abstractproperty
import datetime

try:
    # Captura nome do usuário
    import os
    print(f'\nOlá, {os.getlogin()}')
except:
    # Se não conseguir o nome do usuário
    print("Olá, usuário ")

print("\nEscolha entre as opções:\n1) Intervalo entre 2 nmrs \n2)Somatório 1-100\n3)Números positivos\n4)LOGIN\n5)Fatorial\n6)Número Primo\n7)Separar o joio do trigo")
print("\n100)Sair")

# Laço esperando entradas do usuário- Só acaba quando o usuário digitar 7  
while True:

    opcaoValida = False
    print("\nDigite a opção desejada: ")
    try:
        opcao = int(input())
        
        if opcao > 0 and opcao < 8:
            # Valida a opcao
            opcaoValida = True
        else:
            print("Erro: Insira um número entre 1 e 7!")
    except ValueError:
        print("Erro: Insira um número entre 1 e 7!")

    if opcaoValida:
        #SAIR
        if opcao == 100:
            print("Obrigado por utilizar nosso sistema!\n")
            # Quebra o laço
            break
        # Intervalo entre dois números
        elif opcao == 1:
            print("Opção 1: Intervalo entre dois números")
            n1=int(input("Digite o número 1: "))
            n2=int(input("Digite o número 2: "))

            if n1<n2:

                for i in range(n1+1, n2):
                    print(i)
            else:
                for i in range(n2+1, n1):
                    print(i)
        #Somatório 1-100
        elif opcao == 2:
            soma=0
            for i in range(0, 1000):
                
                soma=soma+i
            print("Somatório: ", soma)
            
            print("")
        #Números positivos
        elif opcao == 3:
            print("Digite números positivos e pares:")
            soma=0
            while True:
                n=int(input())
            
                if n > 0 and (n % 2 == 0):
                    soma= soma + n
                else:
                    print("Soma= ", soma)
                    break
        #LOGIN
        elif opcao == 4:
            print("LOGIN")
            tentativas=0
            while True:
                user=input("Usuário: ")
                password=input("Senha: ")

                if user == "USER10" and password == "PASSWORD1234":
                    print("Login efetuado com sucesso!")
                    break
                else:
                    tentativas+=1
                    if tentativas == 3:
                        print("Número máximo de tentativas escedido!")
                        break
                    else:
                        print("Usuário ou/e senha incorretos")
        #Fatorial
        elif opcao == 5:
            print("Opção 5: Fatorial")
            n=int(input("Digite um número: "))
            fatorial=1

            if n == 0:
                print("A fatorial de zero é 1")
            else:
                for i in range(1, n+1):
                    fatorial= fatorial*i
            print("Fatorial: ", fatorial)
        #Número Primo
        elif opcao == 6:
            print("O número é primo?")

            n=int(input("Digite um número: "))
            divisores=0
            
            for i in range (1, n+1):
                if n%i == 0: 
                    divisores+=1

            print("Nmr de divisores: ", divisores) 
            
            if divisores <= 2:
                print("É número primo!")
            else:
                print("Não é número primo")
        #Separar o joio do trigo
        elif opcao == 7:
            joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio"]
            joio=[]
            trigo=[]
            for i in joioETrigo:
                if i == "joio":
                    joio.append(i)
                else:
                    trigo.append(i)

            print(joio,"\n ___\n", trigo)
                
# FimPrograma