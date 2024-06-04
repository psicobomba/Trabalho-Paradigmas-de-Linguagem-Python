#Exercicio da forca no Python
#Carregando o Modulo Aleatorio
import random

#Escolha de palavras pelo sistema aleatorio
def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "programacao", "tendencias", "python", "openai"]
    return random.choice(palavras)

#Desenho da forca pelo numero de tentativas
def exibir_forca(tentativas):
    forca = [
        """
           _____
          |     |
                |
                |
                |
                |
        ============
        """,
        """
           _____
          |     |
          O     |
                |
                |
                |
        ============
        """,
        """
           _____
          |     |
          O     |
          |     |
                |
                |
        ============
        """,
        """
           _____
          |     |
          O     |
         /|     |
                |
                |
        ============
        """,
        """
           _____
          |     |
          O     |
         /|\\    |
                |
                |
        ============
        """,
        """
           _____
          |     |
          O     |
         /|\\    |
         /      |
                |
        ============
        """,
        """
           _____
          |     |
          O     |
         /|\\    |
         / \\    |
                |
        ============
        """
    ]
    print(forca[tentativas])

#Função principal do jogo
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    letras_tentadas = []
    tentativas = 0
    
    print("Bem-vindo ao Jogo da Forca!,Cada palavra errada te deixa mais perto do enforcamento")
    print("Adivinhe a palavra, so nao vai errar heim ha ha")
    print(" ".join(palavra_oculta))
    
    while tentativas < 6:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou esta letra. Tente outra.")
            continue
        
        letras_tentadas.append(letra)
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print(" ".join(palavra_oculta))
        else:
            tentativas += 1
            exibir_forca(tentativas)
        
        if "_" not in palavra_oculta:
            print("Parabéns! Você ganhou!,por enquanto...")
            break
    
    if "_" in palavra_oculta:
        print("Você perdeu!, Que pena. A palavra era:", palavra)
    
    print("Obrigado por jogar!,Até mais!")

# Chamada da função para iniciar o jogo
jogar()
