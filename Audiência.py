#Gabriel M Carossi

Continuar=True

while(Continuar):
    n = int (input("Digite a a quantidade de índices de audiência que serão digitados: \n"))

    audSempreCrescente = False
    somaAud=0

    for i in range (0, n):
        #lê audiência
        aud = float(input())
        somaAud= somaAud + aud
        
        if i>0:
            #se a audiência é maior que a anterior
            if aud > audAnterior:
                audSempreCrescente = True
            else:
                audSempreCrescente = False

        audAnterior=aud

    if audSempreCrescente:
        print("AUDIÊNCIA SEMPRE CRESCENTE")
    else:
        print("AUDIÊNCIA NEM SEMPRE CRESCENTE")

    print("\nMédia: %.1f" % (somaAud/n))

    print("\nDeseja continuar? [S/N]")
    if input()=="N":
        Continuar=False