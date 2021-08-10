n=1
somatorio=0

while (n<201):
    div=2
    primo=True
    while(div<n):
        if n % div == 0: 
            primo=False
            break
        div+= 1
    if primo:
        somatorio=somatorio+n
    n+=1

print("Somatório dos primos de 1-200: ", somatorio)