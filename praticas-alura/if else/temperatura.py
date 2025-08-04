# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

print("temperatura: ")
temp = float(input())

if temp > 25:
    print("alerta")
else:
    print("ok")