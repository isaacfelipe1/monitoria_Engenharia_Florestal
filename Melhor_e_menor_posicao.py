cont = 1
maior = posicao_maior = 0
menor = posicao_menor = 0
soma = 0

while cont <= 5:
    voltaTempo = float(input("Digite o tempo: "))
    soma += voltaTempo
    
    if cont == 1:  # Primeira iteração, considera o tempo como o menor e o maior
        menor = voltaTempo
        maior = voltaTempo
    else:
        if voltaTempo > maior:
            maior = voltaTempo
            posicao_maior = cont
        if  voltaTempo < menor:
            menor = voltaTempo
            posicao_menor+=1
    cont += 1

print(f'O valor do pior tempo é {maior}')
print(f'O pior tempo foi na volta {posicao_maior}')
print(f'O valor do melhor tempo é {menor}')
print(f'O melhor tempo foi na volta {posicao_menor + 1 }')
print(f'A Média das voltas é desses tempos anotados: {soma / 5}')
