nroAtletas = int(input("Número de Atletas: "))

somaAlturas=0

for i in range (0, nroAtletas):

    nome = input("Nome: ")
    idade= int(input("Idade: "))
    altura= float(input("Altura: "))
    print("")
    if i == 0:
        maisVelho= nome
        idadeMaisVelho= idade
        maisBaixo=nome
        alturaMaisBaixo=altura
    else:
        if (idade>idadeMaisVelho):
            maisVelho= nome
            idadeMaisVelho=idade
        if (altura<alturaMaisBaixo):
            maisBaixo= nome
            alturaMaisBaixo=altura
    somaAlturas= somaAlturas + altura

print("Mais velho: ", maisVelho)
print("Mais baixo: ", maisBaixo)
print("Média das alturas: ", (somaAlturas/nroAtletas))