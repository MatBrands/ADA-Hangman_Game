import os
import sys
sys.path.insert(1, '../')
from model.Words import *
from unidecode import unidecode

def hangman_art(path = './controller/arts.txt') -> list:
    with open(path, 'r', encoding='utf-8') as file:
        art: list = file.read().split(';')
        
    for i in range(len(art)):
        art[i] = art[i].strip('\n')
        
    return art

class Game:
    def __init__(self) -> None:
        self.victory = 0
        self.defeat = 0
        self.word_class = Words()
        self.art = hangman_art()
        
    def hangman(self) -> bool:
        word = self.word_class.random_word()
        erro = 0
        
        hidden_word = ['_']*len(word)
        
        for i, character in enumerate(word):
            if character in [' ', '-']: hidden_word[i] = character
        
        while True:
            os.system('clear')
            tentative = ''.join(hidden_word)
            print(self.art[erro])
            for item in tentative:
                print(item, end=' ')
            
            key = unidecode(input('\nDigite uma letra ou a palavra: '))
            if key not in word:
                if len(key) == 1:
                    input("Letra incorreta !\n")
                else:
                    input("Palavra incorreta !\n")
                erro += 1
            elif key in tentative:
                input("Letra já foi utilizada !\n")
                erro += 1
            elif len(key) > 1:
                if key == word:
                    input("Acerto !\n")
                    for i, item in enumerate(word):
                        hidden_word[i] = item
                else:
                    input("Palavra incorreta !\n")
                    erro += 1
            else:
                input("Acerto !\n")
                for i in range(len(word)):
                    for item in key:
                        if word[i] == item:
                            hidden_word[i] = item
            
            if erro == 7 or ''.join(hidden_word) == word:
                break
            
        os.system("clear")
        
        if word == ''.join(hidden_word):
            print(f"Parabéns !\nVocê acertou a palavra: {word} com {erro} tentativa(s) errada(s)")
            return True
        else:
            print(f"Não foi dessa vez, a palavra era: {word}")
            return False