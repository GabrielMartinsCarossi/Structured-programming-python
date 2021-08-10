#   Programa M2 Gabriel   #

import datetime

try:
    # Captura nome do usuário
    import os
    print(f'\nOlá, {os.getlogin()}')
except:
    # Se não conseguir o nome do usuário
    print("Olá, usuário ")

print("\nEscolha entre as opções:\n1) Verificar triângulo\n2) Calcular equação do segundo grau\n3) Conferir data")
print("4) Verificar tamanho do texto\n5) Analisar CPF\n6) Contar caracteres\n7) Sair\n")

# Laço esperando entradas do usuário- Só acaba quando o usuário digitar 7
while True:

    opcaoValida = False
    print("\nDigite a opção(1-7) desejada: ")
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
        print("")
        # SAIR
        if opcao == 7:
            print("Obrigado por utilizar nosso sistema!\n")
            # Quebra o laço
            break
        # Verificar Triângulo
        elif opcao == 1:
            print("Opcao 1: Verificar Triângulo ")
            try:
                l1 = int(input("Digite lado 1: "))
                l2 = int(input("Digite lado 2: "))
                l3 = int(input("Digite lado 3: "))
            except ValueError:
                print("Erro: Digite um número!")
                continue

            # Verifica se é triângulo
            a = l2-l3
            b = l1-l3
            c = l1-l2
            if (abs(a) < l1 and l1 < (l2+l3) and
                abs(b) < l2 and l2 < (l1+l3) and
                abs(c) < l3 and l3 < (l1+l2)):
                # Verifica se é equilátero
                if (l1 == l2 and
                        l2 == l3):
                    print("\nÉ triângulo equilátero.")
                # Verifica se é isósceles
                elif ((l2 == l3) or
                        (l1 == l3) or
                        (l1 == l2)):
                    print("\nÉ triângulo isósceles.")
                else:
                    print("\nÉ triângulo escaleno.")
            else:
                print("\nNão é um triângulo!")
        # Calcular equação do segundo grau
        elif opcao == 2:
            print("Opção 2: Calcular equação do segundo grau")
            try:
                a = float(input("Digite a:"))
                b = float(input("Digite b:"))
                c = float(input("Digite c:"))
            except ValueError:
                print("Erro: Digite um número!")
                continue

            if a != 0:
                delta = ((b**2) - 4*a*c)
                # Tem duas raízes
                if delta > 0:
                    raiz1 = ((b*-1) + (delta**(1/2)))/(2*a)
                    raiz2 = ((b*-1) - (delta**(1/2)))/(2*a)
                    print("\nRaiz 1 é: %.2f" % raiz1)
                    print("Raiz 2 é: %.2f" % raiz2)
                # Tem uma raiz
                elif delta == 0:
                    raiz = (b*-1)/(2*a)
                    print("\nA equação tem apenas uma raiz:")
                    if raiz == -0.0 or raiz == 0.0:
                        print("Raiz: 0")
                    else:
                        print("Raiz: %.2f" % raiz)
                # Não tem raízes reais
                else:
                    print("\nEquação não possui raízes reais!")
            else:
                print("\nErro: Não é equação do segundo grau.'a' não pode ser zero!")
        # Conferir data
        elif opcao == 3:
            print("Opcão 3: Conferir data")
            dia = (input("Insira o dia:"))
            mes = (input("Insira o mês:"))
            ano = (input("Insira o ano:"))
            # Data
            data = '{}-{}-{}'.format(ano, mes, dia)
            format = "%Y-%m-d"

            DataValida = True
            try:
                datetime.datetime(int(ano), int(mes), int(dia))
            except:
                DataValida = False

            if DataValida:
                print("\nA data é válida")
            else:
                print("\nA data não é válida")
        # Verificar tamanho do texto
        elif opcao == 4:
            print("Opção 4: Verificar tamanho do texto")
            texto = input("Digite o texto: ")
            char = len(texto)

            if char < 5:
                print("O texto é muito pequeno")
            elif char >= 5 and char < 15:
                print("O texto é de tamanho médio")
            elif char >= 15 and char < 20:
                print("O texto é grande")
            else:
                print("O texto é inválido")
        # Analisar CPF
        elif opcao == 5:
            print("Opção 5:Analisar CPF")
            cpf = input("Insira o CPF:")

            if cpf.isdigit():
                if len(cpf) == 11:
                    print("CPF Válido")
                else:
                    print("CPF Inválido. O CPF deve ter 11 dígitos.")
            else:
                print("CPF Inválido. O CPF deve conter somente dígitos(números).")
        # Contar Caracteres
        elif opcao == 6:
            print("Opção 6: Contar Caracteres")
            texto = input("Insira o texto: ")

            vogais = 0
            consoantes = 0
            charEsp = 0
            espacos = 0
            numeros = 0

            for i in texto:
                # Se for letra
                if i.isalpha():
                    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                        vogais += 1
                    else:
                        consoantes += 1
                # Se for número
                elif i.isdigit():
                    numeros += 1
                elif i == " ":
                    espacos += 1
                else:
                    charEsp += 1

            outros = consoantes+charEsp+numeros

            print("\nVogais: ", vogais)
            print("Espaços: ", espacos)
            print("Outros :", outros)

            print("    Consoantes: ", consoantes)
            print("    Caracteres Especiais: ", charEsp)
            print("    Números: ", numeros)

        print("")

# FimPrograma