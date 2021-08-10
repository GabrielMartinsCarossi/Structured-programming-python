print("")
print("+---CÁLCULO DE MÉDIA DA DISCIPLINA---+")
                            
atividadePraticaGrauA = float(input("|  Insira a nota da A. Prática:      |"))
atividadeTeoricaGrauA = float(input("|  Insira a nota da A. Teórica:      |"))
provaLaboratorioGrauB = float(input("|  Insira a nota da Prova em Lab:    |"))
testeTeoricoGrauB     = float(input("|  Insira a nota do Testes Teórico:  |"))
trabalhoExClasseGrauB = float(input("|  Insira a nota do Trab. ExClasse:  |"))

grauA = (atividadePraticaGrauA * 0.45)+(atividadeTeoricaGrauA*0.55)
grauB = (provaLaboratorioGrauB * 0.6)+(testeTeoricoGrauB*0.2)+(trabalhoExClasseGrauB * 0.2)

notaFinal = grauA*0.33 + grauB*0.67 

print("|                                    |")
print("|   Sua nota final é:                |")
print("|   +-----+""                          |")
print("|   |%.2f" % notaFinal, "|""                          |")
print("|   +-----+""                          |")
print("|                                    |")
print("+------------------------------------+")
