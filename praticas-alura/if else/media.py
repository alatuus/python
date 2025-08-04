# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
5.3
media = (n1 + n2 + n3 ) / 3
print(f"media: {media:.2f}")

if media >= 7:
    print("aprovado")
elif media < 7 and media >= 5:
    print("recuperacao")
else:
    print("reprovado")