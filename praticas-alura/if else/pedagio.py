# Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

# Até 100 km: R$ 10,00
# Entre 100 km e 200 km: R$ 20,00
# Acima de 200 km: R$ 30,00
# Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.

distancia = float(input("distancia percorrida: "))

if distancia <= 100:
    print("10 reais")
elif distancia > 100 and distancia <= 200:
    print("20 reais")
else:
    print("30 reais")