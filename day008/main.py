print("Máquina de Positividade Saudável!")
print()

nome = input("Quem é você? ")

objetivo = input("O que você deseja alcançar? ")

resposta = int(input("Em uma escala de 1 a 10, como você se sente hoje?  (1: 😔, 10: 😃) "))

if resposta == 1:
    print(f"Mesmo nos dias difíceis {nome}, lembrar de {objetivo} é a fáisca que poder reacender a sua chama.")
elif resposta == 2:
    print(f"Hoje pode parecer pesado {nome}, mas cada passo, mesmo pequeno, aproxima você de {objetivo}.")
elif resposta == 3:
    print(f"Se a energia está baixa, use-a para refletir: {objetivo} ainda pulsa dentro de você, isso já é força {nome}.")
elif resposta == 4:
    print(f"Você está levantando, {nome}! Continue firme, {objetivo} merece essa perseverança.")
elif resposta == 5:
    print(f"Equilibrado(a), nem no topo nem no fundo, o importante é que {objetivo} segue sendo seu norte.")
elif resposta == 6:
    print(f"Hey, {nome}. Você já sente que o vento sopra a favor: {objetivo} está mais perto do que parece.")
elif resposta == 7:
    print(f"Boa vibração, {nome}! Canalize essa energia e avance com confiança rumo a {objetivo}.")
elif resposta == 8:
    print(f"Você está em alta, {nome}! Aproveite esse ritmo para dar passos sólidos em direção a {objetivo}!")
elif resposta == 9:
    print(f"Quase no auge, ein {nome}? Essaa motivação é o combustível perfeito para conquistar {objetivo}.")
elif resposta == 10:
    print(f"Plenitude total {nome}! Nada pode parar você, {objetivo} já é parte do seu destino!")