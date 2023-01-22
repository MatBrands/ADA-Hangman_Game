from random import randint
from unidecode import unidecode

class Words:
    def __init__(self, path = './controller/words.txt'):
        self.path = path
        
    def set_word(self, word) -> None:
        path = self.path
        with open(path, 'a', encoding='utf-8') as file:
            file.write(unidecode(word) + '\n')
        return
    
    def get_words(self) -> list:
        path = self.path
        
        result = []
        with open(path, 'r', encoding='utf-8') as file:
            line = True
            while line:
                line = file.readline()
                if line:
                    line = line.replace('\n', '')
                    result.append(line)
                
        return result
    
    def replace_word(self, old_word, new_word) -> bool:
        path = self.path
        
        words = []
        with open(path, 'r', encoding='utf-8') as file:
            line = True
            while line:
                line = file.readline()
                if line:
                    line = line.replace('\n', '')
                    words.append(line)
                    
        if not old_word in words:
            return False
        
        idx = words.index(old_word)
        
        words = words[:idx]+[new_word]+words[idx+1:]
        
        with open(path, 'w', encoding='utf-8') as file:
            for item in words:
                file.write(item + '\n')
                
        return True
    
    def remove_word(self, word) -> bool:
        path = self.path
        
        words = []
        with open(path, 'r', encoding='utf-8') as file:
            line = True
            while line:
                line = file.readline()
                if line:
                    line = line.replace('\n', '')
                    words.append(line)
                    
        if not word in words:
            return False
        
        idx = words.index(word)
        
        words = words[:idx]+words[idx+1:]
        
        with open(path, 'w', encoding='utf-8') as file:
            for item in words:
                file.write(item + '\n')
                
        return True
    
    def random_word(self) -> str:
        path = self.path
        
        words = []
        with open(path, 'r', encoding='utf-8') as file:
            line = True
            while line:
                line = file.readline()
                if line:
                    line = line.replace('\n', '')
                    words.append(line)
                
        return words[randint(0, len(words)-1)]
        