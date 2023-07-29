cont=1
maior=posicao=0
soma=0
pos=0
menor=float('inf')

while(cont<=5): 
    voltaTempo= float(input("Digite o tempo : ")) 
    soma+=voltaTempo
    if (voltaTempo>maior):
        maior=voltaTempo
        posicao=cont
    if voltaTempo<menor:
        menor=voltaTempo
        pos=cont
    cont=cont+1
print(f'O valor de pior tempo é {maior}')
print(f'O valor de pior tempo está foi na volta {posicao}')
print(f'A Média das voltas é desses tempos anotados {soma/5}')
print(f'{menor} na posição {pos}')






 
