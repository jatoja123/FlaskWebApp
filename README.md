# Instrukcja uruchamiania aplikacji

## Wymagane oprogamowania :smile: :
* Python 3.6+ 
* Git 
* Visual Studio Code

## Instrukcja pobierania :+1: :
1. **"Forknij"** repozytorium
2. **Sklonuj** forknięte repo na swój komputer (**git clone link_do_repo**)
3. Przełącz się na **branch'a** swojej grupy (np. **git checkout sr18**) lub 
    Połącz branch'a **master** z branchem twojej grupy (**git merge branch_grupy**)
4. Otwórz folder z repozytorium w Visual Studio Code (**code .** lub **Open Folder** w aplikacji)

## Instrukcja instalacji wirtualnego środowiska :alien:
1. W Visual Studio Code sprawdź czy konsola **cmd**(windows) **/** **bash**(mac/linux) wskazuje na pobrany wcześniej folder(**FlaskWebApp**)
2. W konsoli:
    * Windows : **python -m venv venv**
    * Mac/Linux : **python3 -m venv venv**
3. Uruchamiamy środowisko:
    * Windows : **venv\Scripts\activate**
    * Mac/Linux : **source venv/bin/activate**
## Instalacja Flaska :sheep:
1. Sprawdź czy masz uruchomione wirtualne środowisko
2. Wpisz do konsoli w Visual Studio Code:
    * (*jeżeli posiadasz plik requirments.txt*) **pip install -r requirments.txt** 
    * **pip install flask** 

## Uruchamianie aplikacji :elephant:
1. W konsoli wpisz:
    * **python webapp.py**
2. Twój serwer działa
3. :space_invader: :space_invader: :space_invader: :space_invader: