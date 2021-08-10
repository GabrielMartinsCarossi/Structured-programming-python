# Ex 2 
idade = int(input("Qual a sua idade mona? "))

if idade >= 0 :
    if idade <= 13: 
        print("Você ainda é criança")
    if idade > 13 or idade < 18:
        print("Você é adolescente")
    else:
        print("Você já é adulta")

else:
    print("Melhor digitar uma idade válida")
