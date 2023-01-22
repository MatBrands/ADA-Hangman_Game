import os
from view.Menu import *
from view.Game import *
from view.interface import *

if __name__ == '__main__':
    title = ['Bem vindo ao nosso jogo da forca !\n', 'Selecione uma opção a seguir para iniciarmos\n']
    params = ['Iniciar o jogo', 'Palavras', 'Sobre o jogo', 'Sair']
    
    hangmanGame = Game()
    wordsClass = Words()
    while True:
        option = start_menu(title, params)
        if option == 0:
            if not len(wordsClass.get_words()):
                input("Erro ! Não existem palavras registradas em nosso banco de dados\n")
            else:
                status = hangmanGame.hangman()
                if status:
                    hangmanGame.victory += 1
                else:
                    hangmanGame.defeat += 1
                os.system("clear")
                input()
        elif option == 1:
            words_menu(wordsClass)
        elif option == 2:
            input("Para mais informações visite o repositorio do projeto: https://github.com/MatBrands/ADA-Hangman_Game\n")
        else:
            print("Fim de jogo !")
            input(f"Saldo: {hangmanGame.victory} vitória(s), {hangmanGame.defeat} derrota(s)\n")
            os.system("clear")
            break