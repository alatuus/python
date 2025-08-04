# 2 – A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:

# a) O preço final para compra à vista tem um desconto de 20%.

# b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.

valor_carro = float(input("Informe o valor do carro: "))

print("O preço final para compra à vista com desconto de 20% é: " + str(valor_carro * 0.8))
percentual_acrescimo = 0.03


for i in range(6, 61, 6):
    valor_total = valor_carro * (1 + percentual_acrescimo)
    valor_parcela = valor_total / i
    print(f"O preço final parcelado em {i}x é {valor_total:.2f} com parcelas de R$ {valor_parcela:.2f}")
    percentual_acrescimo = percentual_acrescimo + 0.03