linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))

for l in range(0, linhas):
    for c in range(0,colunas):
        if c == 0:
            print("\n* ", end="")
        else:
            print("* ", end="")

print("\n")