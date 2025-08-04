# Na oferta de um produto de crédito aos clientes, três informações são muito importantes apresentar ao cliente: valor da dívida, a taxa de juros e o número de parcelas para pagamento do empréstimo contraído junto à Fintech. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:

 

# - Valor da dívida, valor do juros, quantidade de parcelas e valor da parcela.

valor_divida = float(input("Digite o valor da dívida: "))
print(f"Valor: R$ {valor_divida:.2f} | Juros: R$ 0,00 | Número de parcelas: 1 | Valor da parcela: R$ {valor_divida:.2f}")

valor_juros = 0.10

for i in range(3, 13, 3):
    valor_total = valor_divida * (1 + valor_juros)
    print(f"Valor: R$ {valor_total:.2f} | Juros: {(valor_total - valor_divida)} | Número de parcelas: {i} | Valor da parcela: R$ {(valor_total / i):.2f}")
    valor_juros += 0.05
