# ADA-Hangman_Game
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

[Portuguese Version](https://github.com/MatBrands/ADA-Hangman_Game/blob/master/Readme.md)

- Institution: Let's Code
- Course: Data4All
- Discipline: Programming Logic I
- Teachers: Henrique Assis Cordeiro & Wenderson Alexandre de Sousa Silva
- Student: Matheus Miranda Brandão.

This project has the objective the conclusion of the module I from the course Data4All. It consists in the implementation of the Hangman Game.

The complete specification from this project can be found in: [Projeto Extra](https://github.com/MatBrands/ADA-Hangman_Game/blob/master/utils/Projeto%20Extra.ipynb)

## Contents

- Members
- Recomendations
- Tecnologies
- Instalation
- Organization of the project

## Members
Project developed by the Dev:

- [Matheus Miranda Brandão](https://github.com/MatBrands)

## Recomendations
- When developing a new feature, the dev must request the Pull Request commenting on what was done.
- Regarding commits, a pattern will be used
    - Commits from new features. Ex: git commit -m "New: Readme"
    - Commits from updates. Ex: git commit -m "Updated: Readme"
    - Commits from remoção. Ex: git commit -m "Removed: Readme"

## Tecnologies

- python=3.9.15
- os
- sys
- termcolor
- pynput
- unidecode


## Instalation

### Conda
In development, the package and environment manager [Conda](https://conda.io/) was used. So to proceed you need your [installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Navigate to destination folder
```sh
cd utils
```

- Install the dependencies
```sh
conda env create environment.yml
```

- activate
```sh
conda activate hangman_game_venv
```

- Deactivate
```sh
conda deactivate
```

### Requirements
Can be used the file requirements.txt to create a virtual environment.

- Navigate to destination folder
```sh
cd utils
```

- Create the virtual enviroment
```sh
python -m venv hangman_game_venv
```

- Activate
```sh
source ./hangman_game_venv/bin/activate
```

- Install the dependencies
```sh
pip install -r requirements.txt
```

- Deactivate
```sh
deactivate
```


## Organization of the project
```sh
├── ADA-Hangman_Game
│   ├── hangman_game
│   │   ├── __init__.py
│   │   ├── controller
│   │   │   ├── arts.txt
│   │   │   └── words.txt
│   │   ├── model
│   │   │   └── Words.py
│   │   └── view
│   │       ├── Game.py
│   │       ├── interface.py
│   │       ├── Menu.py
│   ├── utils
│   │   ├── environment.yml
│   │   ├── Projeto Extra.ipynb
│   │   └── requirements.txt
│   ├── License
│   └── Readme.md
```