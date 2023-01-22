import os
from model.Words import *
from view.Menu import *

def start_menu(titulo: list, itens: list) -> int:
    menu = Menu()
    menu.setTitle(titulo)
    menu.setItems(itens)
    option = menu.startMenu()
    return option

def words_menu(wordsClass: Words):
    title = 'Selecione uma opção: \n'
    params = ['Palavras registradas', 'Adicionar palavra', 'Alterar palavra', 'Excluir palavra', 'Retornar']
    
    while True:
        option = start_menu(title, params)
        
        os.system("clear")
        if option == 0:
            words = wordsClass.get_words()
            for item in words:
                print(item)
                
            input()
        elif option == 1:
            word = input("Digite a palvra para registrar: ")
            wordsClass.set_word(word)
            input("Palavra registrada com sucesso !\n")
            
        elif option == 2:
            words = wordsClass.get_words()
            alter_option = start_menu('', words)
            
            new_word = input("Digite a nova palavra: ")
            if wordsClass.replace_word(words[alter_option], new_word):
                input("Alteração realizada com sucesso !\n")
            else:
                input("Erro !")
        elif option == 3:
            words = wordsClass.get_words()
            alter_option = start_menu('', words)
            
            if wordsClass.remove_word(words[alter_option]):
                input("Exclusão realizada com sucesso !\n")
            else:
                input("Erro !\n")
        else:
            break