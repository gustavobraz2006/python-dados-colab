print("--------------------------------------------------")
print("Bem-vindo ao Jokenpô!")
print("--------------------------------------------------") 
import random  
opcoes_validas = ('pedra', 'papel', 'tesoura') 
while True:
    jogador = input(f"Escolha uma dessas opções {opcoes_validas} ou 'sair' para encerrar: ").lower().strip()
    if jogador == 'sair':
        print("Obrigado por jogar! Até a próxima.")
        break
    if jogador not in opcoes_validas:
        print("Opção inválida. Tente novamente.")
        continue 
    computador = random.choice(opcoes_validas)
    print(f"Computador escolheu: {computador}")
    if jogador == computador:
        print("Empate!")
        continue
    elif jogador == 'pedra' and computador == 'tesoura':
        print("Parabéns, você venceu!!!!!")
        continue
    elif jogador == 'papel' and computador == 'pedra':
        print("Parabéns, você venceu!!!!!")
        continue
    elif jogador == 'tesoura' and computador == 'papel':
        print("Parabéns, você venceu!!!!!")
        continue
    elif computador == 'pedra' and jogador == 'tesoura':
        print("Que pena, não foi dessa vez...")
        continue
    elif computador == 'papel' and jogador == 'pedra':
        print("Que pena, não foi dessa vez...")
        continue
    elif computador == 'tesoura' and jogador == 'papel':
        print("Que pena, não foi dessa vez...")
        continue
    else:
        break