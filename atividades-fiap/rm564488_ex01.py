# Programa para votação do melhor dia da semana para lives

print("Informe o número de colaboradores que irão participar da votação:")
num_colaboradores = int(input())

# Inicializando contadores para cada dia da semana
dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
votos = [0, 0, 0, 0, 0]

# Loop para coletar os votos
for i in range(num_colaboradores):
    print(f"Colaborador {i + 1}, informe o dia da semana de sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira):")
    voto = input().strip().lower()
    
    voto_valido = False
    for j in range(len(dias)):
        if voto == dias[j]:
            votos[j] += 1
            voto_valido = True
            break
    
    if not voto_valido:
        print("Dia inválido. Por favor, informe um dia válido.")

# Encontrando o maior número de votos
maior_voto = 0
for voto in votos:
    if voto > maior_voto:
        maior_voto = voto

# Verificando quais dias tiveram o maior número de votos
dias_mais_votados = []
for i in range(len(dias)):
    if votos[i] == maior_voto:
        dias_mais_votados.append(dias[i])

# Exibindo o resultado
if len(dias_mais_votados) > 1:
    print("Houve um empate entre os seguintes dias:")
    for dia in dias_mais_votados:
        print(f"- {dia} com {maior_voto} votos")
else:
    print(f"O dia escolhido foi {dias_mais_votados[0]} com {maior_voto} votos.")
