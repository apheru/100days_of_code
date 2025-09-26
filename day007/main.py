print("Caçador de Fã Nutella")
print("=====================")
print()
nome_anime = input("Qual é teu anime favorito? ").strip().lower()

if nome_anime == "one piece":
    nome_personagem = input("Ah, é mesmo?! Então manda aí o nome de um dos Mugiwaras!").strip().lower()
    if nome_personagem == "luffy":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "capitão":
            print("Mandou bem! Luffy é o nosso destemido Capitão!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "zoro":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "espadachim":
            print("Mandou bem! Zoro é o nosso temido Espadachim!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "sanji":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "cozinheiro":
            print("Mandou bem! Sanji, além de mulherengo é um excelente cozinheiro!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")   
    elif nome_personagem == "usopp":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "atirador":
            print("Mandou bem! Usopp é o nosso incrivel Atirador!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "nami":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dela no navio? ").strip().lower()
        if nome_funcao == "navegadora":
            print("Mandou bem! Nami é a nossa incrivel Navegadora!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "chopper":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "médico":
            print("Mandou bem! Chopper é o nosso habilidoso Médico!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "robin":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dela no navio? ").strip().lower()
        if nome_funcao == "arqueologa":
            print("Mandou bem! Robin é o nossa sombria e adorável Arqueologa!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "franky":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "carpinteiro":
            print("Mandou bem! Franky é o nosso SUPERRR Carpinteiro!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "brook":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "músico":
            print("Mandou bem! Brook é o nosso Músico! Yohohoho")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    elif nome_personagem == "jinbe":
        nome_funcao = input("Hahaha!, acertou na cagada. Beleza... e qual é a função dele no navio? ").strip().lower()
        if nome_funcao == "espadachim":
            print("Mandou bem! Jinbe é o nosso habilidoso Timoneiro!")
        else:
            print("Aí ó! Peguei Fã de ENFEITE de One Piece!")
    else:
        print("Aí ó! Peguei! Fã de ENFEITE de One Piece!")
        
else:
    print(f"Legal cara! {nome_anime}, é um bom anime!")
