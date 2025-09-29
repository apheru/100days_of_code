print("Calculadora de Gorjeta")
print("======================")
valor_gasto = int(input("Quanto você gastou? "))

porcentagem_gorjeta = int(input("Qual porcentagem você quer deixar de gorjeta? "))
gorjeta = valor_gasto * (porcentagem_gorjeta / 100)
valor_total = valor_gasto + gorjeta

pessoas = int(input("Quantas pessoas estão no seu grupo? "))
valor_pagar = valor_total / pessoas

if pessoas > 1:
    print(f"Cada um deve R$ {valor_pagar:.2f}")
else:
    print(f"Você deve pagar R$ {valor_pagar:.2f}")
