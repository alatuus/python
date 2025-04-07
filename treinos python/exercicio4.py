# Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve calcular a alíquota de imposto de renda (IR) que deve ser aplicada sobre aquele resgate, levando em consideração o número de dias que o valor permaneceu aplicado, de acordo com a tabela abaixo:

# É o que acontece, por exemplo, com o Certificado de Depósito Bancário (CDB), uma aplicação de renda fixa comumente oferecida pelas Fintechs. Outros investimentos em renda fixa, como LCI e LCA, respectivamente, Letra de Crédito Imobiliário e Letra de Crédito do Agronegócio são isentos de imposto de renda. Escreva um programa que receba o tipo de investimento do qual se deseja realizar um resgate (1 para CDB, 2 para LCI e 3 para LCA), o valor a ser resgatado e o número de dias que esse valor permaneceu investido e, se for o caso, calcule o valor referente ao imposto de renda.

# Atenção! O programa deve consistir se o investimento fornecido é válido, ou seja, 1, 2 o 3.

print("Escolha o tipo de investimento:")
print("1 - CDB")
print("2 - LCI")
print("3 - LCA")

tipo_investimento = int(input("Digite o tipo de investimento: "))
valor_resgate = float(input("Digite o valor a ser resgatado: "))
dias_investido = int(input("Digite o número de dias que o valor permaneceu investido: "))

if(tipo_investimento == 1):
    if(181 <= dias_investido <= 360):
        valor_imposto = valor_resgate * 0.2
        print(f"O valor do imposto de renda a ser pago é: R${valor_imposto:.2f}")
    elif(361 <= dias_investido <= 720):
        valor_imposto = valor_resgate * 0.175
        print(f"O valor do imposto de renda a ser pago é: R${valor_imposto:.2f}")
    elif(721 <= dias_investido):
        valor_imposto = valor_resgate * 0.15
        print(f"O valor do imposto de renda a ser pago é: R${valor_imposto:.2f}")    
elif(tipo_investimento == 2 or tipo_investimento == 3):
    print("Esse tipo de investimento é isento de imposto de renda.")
else:
    print("O número fornecido não é válido.")