print("Vamos encontrar seu Chapéu de Palha favorito! ⚓")
print()
print("Responda 'Sim' ou 'Não' e siga as pistas para descobrirmos quem é o seu personagem preferido!")
print()

resposta = input("Seu personagem favorito é feito de borracha? ")

if resposta == "Sim":
    print("É o \033[31mLuffy\033[0m, nosso capitão sonhador e incansável!")
else:
    print("Ah, então não é o nosso capitão... prossiga para a próxima pergunta.")
    
    resposta = input("Ele usa espadas para lutar? ")
    if resposta == "Sim":
        print("É o \033[32mZoro\033[0m, o espadachim que nunca de ser o melhor do mundo!")
    else:
        print("Hmm, então não é o caçador de piratasn...")
        
        resposta = input("Ele é o maior mulherengo da tripulação? ")
        if resposta == "Sim":
            print("Só pode ser o \033[33mSanji\033[0m, o cozinheiro dos pés de fogo e coração ardente!")
        else:
            print("Ah, então não é o mestre da culinária... bora pra próxima.")
            
            resposta = input("Seu personagem toca instrumentos e anima a galera com música? ")
            if resposta == "Sim":
                print("É o \033[30mBrook\033[0m, o esqueleto músico que nunca perde a piada! Yohohoho")
            else:
                print("Ops, então não é o senhor das canções... próxima pergunta!")
                
                resposta = input("Ele adora navegar e sonhar em desenhar o mapa do mundo? ")
                if resposta == "Sim":
                    print("É a Nami, a navegadora que guia o bando pelos mares tempestuosos.")
                else:
                    print("Então não é a gata ladra... seguimos.")
                    
                    resposta = input("Ele é um mentiroso carismático e ótimo atirador? ")
                    if resposta == "Sim":
                        print("É o Usopp, o atirador que transforma medo em coragem!")
                    else: 
                        print("Não é o rei dos atiradores? Vamos adiante.")
                        
                        resposta = input("Seu personagem é o médico da tripulação(e também uma rena fofa)? ")
                        if resposta == "Sim":
                            print("É o Chopper, o doutorzinho mais adorável dos mares!")
                        else:
                            print("Então não é o médico prodígio... próxima.")
                            
                            resposta = input("Ela é uma arqueóloga inteligente, misteriosa e com passado sombrio? ")
                            if resposta == "Sim":
                                print("É a \033[35mRobin\033[0m, a guardiã da história do mundo!")
                            else:
                                print("Não é a sombria estudiosa... bora seguir.")
                                
                                resposta = input("Ele é um ciborgue construtor de navios, cheio de estilo e colas? ")
                                if resposta == "Sim":
                                    print("É o \033[36mFranky\033[0m, o capinteiro SUPERRR da tripulação!")
                                else:
                                    print("Então não é o mestre das invenções, próxima pergunta.")
                                    
                                    resposta = input("Ele é o mais novo timoneiro, com habilidades de peixe e coração gigante? ")
                                    if resposta == "Sim":
                                        print("É o \033[34mJinbe\033[0m, o cavaleiro do mar leal e poderoso!")
                                    else:
                                        print("Parece que o seu favorito não é nenhum dos Chapéus de Palha... talvez você seja fã de outro pirata, de um marinheiro ou até de um vilão lendário que cruza o caminho deles!")