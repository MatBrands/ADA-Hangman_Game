# ADA-Hangman_Game
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

- Instituição: Let's Code
- Curso: Data4All
- Disciplina: Lógica de Programação I
- Professores: Henrique Assis Cordeiro & Wenderson Alexandre de Sousa Silva
- Alunos: Matheus Miranda Brandão.

Este projeto tem como objetivo a conclusão do módulo I do curso Data4All. Ela consiste na implementação do Jogo da Forca.

A especificação completa do projeto pode ser encontrada em: [Projeto Extra](https://github.com/MatBrands/ADA-Hangman_Game/blob/master/utils/Projeto%20Extra.ipynb)

## Conteúdo

- Integrantes
- Recomendações
- Tecnologias
- Instalação
- Organização do projeto
- Contribuições

## Integrantes
Projeto desenvolvido pelo Dev:

- [Matheus Miranda Brandão](https://github.com/MatBrands)

## Recomendações
- Ao desenvolver uma nova funcionalidade o dev deverá solicitar o Pull Request comentando o que foi feito.
- Em relação aos commits será utilizado um padrão
    - Commits de novas features. Ex: git commit -m "New: Readme"
    - Commits de updates. Ex: git commit -m "Updated: Readme"
    - Commits de remoção. Ex: git commit -m "Removed: Readme"

## Tecnologias

- python=3.9.15
- json
- os
- sys
- termcolor
- pynput


## Instalação

### Conda
No desenvolvimento foi utilizado o gerenciador de pacotes e ambientes [Conda](https://conda.io/). Portanto para prosseguir necessita-se de sua [instalação](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navegar até a pasta de destino
```sh
cd utils
```

- Instalar dependências
```sh
conda env create environment.yml
```

- Ativar
```sh
conda activate hangman_game_venv
```

- Desativar
```sh
conda deactivate
```

### Requirements
Pode-se utilizar o arquivo requiremets.txt para criar o ambiente virtual.

- Navegar até a pasta de destino
```sh
cd utils
```

- Criar ambiente virtual
```sh
python -m venv hangman_game_venv
```

- Ativar
```sh
source ./hangman_game_venv/bin/activate
```

- Instalar dependências
```sh
pip install -r requirements.txt
```

- Desativar
```sh
deactivate
```


## Organização do projeto
```sh
...
```


## Contribuições