# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

print("Informe o número de maçãs vendidas:")
vendas_macas = int(input())

print("Informe o número de bananas vendidas:")
vendas_bananas = int(input())

if vendas_bananas > vendas_macas:
    print("As bananas tiveram maior quantidade de vendas")
elif vendas_bananas == vendas_macas:
    print("Mesma quantidade de vendas")
else:
    print("As macas tiveram maior quantidade de vendas")