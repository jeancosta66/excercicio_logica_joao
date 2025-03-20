# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra

print("Digite quantas maçãs você desejar: ")
num_macas = int(input())
valor = 0 
if num_macas <= 12 :
    valor = 1.30
    print("Valor de cada maça é R$1,00")
else:
    valor = 1.00
    print("Valor de cada maçã é R$1,30")
