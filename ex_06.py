#. Menu - Elabore um programa que mostre o seguinte menu na tela:
Cadastro de Clientes
0 - Fim
1 - Inclui
2 - Altera
3 - Exclui
4 - Consulta

print("Cadastro de um cliente: ")
cliente = input()
print("Digite um numero entre 0 até 4")
numero = int(input())
if  numero == 0:
    print("fim da consutar")
elif numero == 1:
    print("Incluir o usuário")
elif numero == 2:
    print("Alterar usuário")
elif numero == 3:
    print("Excluir usuário")
elif numero == 4:
    print("Consulta usuário")
else:
    print("Esse numero não custar no banco de dados")
