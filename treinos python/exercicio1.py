# A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar suas fontes de receitas, gastos, dívidas e investimentos.
# Ela precisa realizar uma votação para escolher qual dia da semana é o melhor para a realização das lives com o time da mentoria financeira.
# Desenvolva um programa em que os colaboradores informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira)
# da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.

# Observação: Verifique o número de colaboradores que irão participar da votação para programar sua estrutura de repetição.

# Ponto de atenção: É importante o programa validar a possibilidade de empate.

print("Informe o número de colaboradores que irão participar da votação:")
num_colaboradores = int(input())


votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}


for i in range(num_colaboradores):
    print(f"Colaborador {i + 1}, informe o dia da semana de sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira):")
    voto = input().strip().lower()
    if voto in votos:
        votos[voto] += 1
    else:
        print("Dia inválido. Por favor, informe um dia válido.")

max_votos = (votos.values())
dias_mais_votados = [dia for dia, qtd in votos.items() if qtd == max_votos]

if len(dias_mais_votados) > 1:
    print("Houve um empate entre os seguintes dias:")
    for dia in dias_mais_votados:
        print(f"- {dia} com {max_votos} votos")
else:
    print(f"O dia escolhido foi {dias_mais_votados[0]} com {max_votos} votos.")
