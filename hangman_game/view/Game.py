import os
import sys
sys.path.insert(1, '../')
from model.Words import *
from unidecode import unidecode

def hangman_art(path = './controller/arts.txt') -> list:
    with open(path, 'r', encoding='utf-8') as file:
        art: str = file.read()
    return art.split(';')

class Game:
    def __init__(self) -> None:
        self.victory = 0
        self.defeat = 0
        self.word_class = Words()
        self.art = hangman_art()
        
    def hangman(self) -> bool:
        word = self.word_class.random_word()
        erro = 0
        
        hidden_word = []
        for character in word:
            if character in [' ', '-']: hidden_word.append(character)
            else: hidden_word.append('_')
        
        while True:
            os.system('clear')
            tentative = ''.join(hidden_word)
            print(self.art[erro])
            for item in tentative:
                print(item, end=' ')
            print()
            
            key = input('Digite uma letra ou a palavra: ')
            key = unidecode(key)
            if key not in word:
                if len(key) == 1:
                    input("Letra incorreta !\n")
                else:
                    input("Palavra incorreta !\n")
                erro += 1
            elif key in tentative:
                input("Letra já foi utilizada !\n")
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
            print(f"Parabéns !\nVocê acertou a palavra: {word} com {erro} tentativa(s)")
            return True
        else:
            print(f"Não foi dessa vez, a palavra era: {word}")
            return False