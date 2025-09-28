print("========================")
print("Indetificador de Geração")
print("========================")

ano_nascimento = int(input("Em que ano você nasceu? "))

if ano_nascimento >= 1883 and ano_nascimento <= 1900:
    print("Ah, Geração Perdida… você literalmente começou o rolê da modernidade e ainda teve que lidar com duas guerras no caminho. Respeito total, pioneiro!")
elif ano_nascimento >= 1901 and ano_nascimento <= 1927:
    print("Você é da Geração Grandiosa, raiz de verdade. Se hoje a gente reclama de Wi-Fi lento, vocês já encararam crise mundial e sobreviveram firme.")
elif ano_nascimento >= 1928 and ano_nascimento <= 1945:
    print("Geração Silenciosa… mas de silêncio não tinha nada. Vocês só deixaram as ações falarem mais alto que as palavras.")
elif ano_nascimento >= 1946 and ano_nascimento <= 1964:
    print("Ah, Baby Boomer! Vocês são o manual vivo de ‘no meu tempo era diferente’… e ainda fundaram praticamente tudo que a gente usa hoje.")
elif ano_nascimento >= 1965 and ano_nascimento <= 1980:
    print("Você é da Geração X, o verdadeiro modo hard: cresceu sem internet, mas aprendeu a sobreviver em qualquer época.")
elif ano_nascimento >= 1981 and ano_nascimento <= 1996:
    print("Geração Millennial! Sobreviventes do Orkut, dos GIFs piscantes e ainda inventaram a cultura do meme. Vocês foram o tutorial da vida online.")
elif ano_nascimento >= 1997 and ano_nascimento <= 2012:
    print("Ah, Gen Z… vocês já nasceram swipando tela e postando stories. Se a bateria cai, parece o fim do mundo.")
elif ano_nascimento >= 2013 and ano_nascimento <= 2025:
    print("Geração Alpha! Nem aprenderam a falar e já sabem desbloquear o celular dos pais. O futuro é literalmente touchscreen pra vocês.")
else:
    print("Ei, esse ano não bate com nenhuma geração conhecida… você deve ser uma entidade interdimensional do tempo. 👾")