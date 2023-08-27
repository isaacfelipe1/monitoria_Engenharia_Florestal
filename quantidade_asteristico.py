cont=0
quantidade=int(input("Digite um valor: "))
for x in range (quantidade+1):
    for y in range (x):
        print("*", end="")
        cont=cont+1
    print()
print(f'Quantidade de *= {cont} ')
