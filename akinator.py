import time
import sys

#Restart
def restart():
    answer = []
    intro()
    game()
    results()
    outro()

#Introduction du jeu
def intro():
    start = "Bienvenue dans Akinator devine une couleur! Pense à une couleur simple (pas bleu ciel, etc.)."
    waiting = "Aller, pense à cette couleur"
    tip = "Réponds à la question avec 1 pour Oui et 2 pour Non"
    begin = "Tu es prêt? C'est parti"
    for i in start:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')
    for i in waiting:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')
    for i in tip:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')
    for i in begin:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')

#Le jeu
def game():
    not_used = ['Votre couleur est-elle une couleur primaire?', 
    'Votre couleur est-elle une couleur primaire de pigment?', 
    'Pouvez-vous trouver votre couleur dans le ciel?',
    'Votre couleur est-elle métallique?',
    'Votre couleur est-elle sur le drapeau américain?',
    'Votre couleur absorbe-t-elle OU réfléchit-elle TOUTE la lumière en tant que pigment?',
    'Votre couleur est-elle une des couleurs de l\'école d\'Ayala?',
    'Votre couleur est-elle l\'une des couleurs actuelles de la classe d\'Ayala?',
    'Votre couleur commence-t-elle par un B?',
    'Votre couleur se termine-t-elle par une voyelle?',
    'Votre couleur se termine-t-elle par une consonne?',
    'Cette couleur est-elle dans l\'arc-en-ciel?',
    'Les arbres sont-ils de cette couleur à l\'automne?',
    'Votre couleur est-elle monochrome?',
    'Votre couleur es-elle une couleur froide?',
    'Votre couleur commence-t-elle avec un G?',
    'Votre couleur est-elle associée avec la Saint Valentin? (rouge, violet, rose,blanc, magenta, etc.)']

    for question in not_used:
        for i in question:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        print('')
        reply = int(input('Réponse: '))
        if reply == 1:
            answer.append(reply)
        elif reply == 2:
            answer.append(reply)
        else:
            print('Merci de répondre par 1 ou 2!')
            reply = int(input('Réponse: '))
        print('')

#Comparaison des résultats
def results():
    if answer == red:
        print('Je pense que tu as choisis la couleur rouge!')
    elif answer == orange:
        print('Je pense que tu as choisis la couleur orange!')
    elif answer == yellow:
        print('Je pense que tu as choisis la couleur jaune!')
    elif answer == green:
        print('Je pense que tu as choisis la couleur verte!')
    elif answer == blue:
        print('Je pense que tu as choisis la couleur bleu!')
    elif answer == purple:
        print('Je pense que tu as choisis la couleur violete!')
    elif answer == pink:
        print('Je pense que tu as choisis la couleur rose!')
    elif answer == brown:
        print('Je pense que tu as choisis la couleur marron!')
    elif answer == black:
        print('Je pense que tu as choisis la couleur noire!')
    elif answer == white:
        print('Je pense que tu as choisis la couleur blanche!')
    elif answer == grey:
        print('Je pense que tu as choisis la couleur grise!')
    elif answer == silver:
        print('Je pense que tu as choisis la couleur argent!')
    elif answer == gold:
        print('Je pense que tu as choisis la couleur or!')
    elif answer == magenta:
        print('Je pense que tu as choisis la couleur magenta!')
    else:
        print('Tu est trop fort je ne trouve pas!')

def outro():
    thanks = 'Merci d\'avoir joué!'
    repeat = 'Tu veux rejouer?'
    bye = 'Au revoir! A bientôt!'
    for i in thanks:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')
    for i in repeat:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')
    decision = int(input('Réponse: '))
    if decision == 1:
        restart()
    else:
        print('')
        for i in bye:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
        sys.exit()

#MAIN	
#Initialisation
red = [1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1] 
orange = [2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2]
yellow = [2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2]
green = [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 2]
blue = [1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2]
purple = [2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1]
pink = [2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1]
brown = [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2]
black = [2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2]
white = [2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1]
grey = [2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2]
silver = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
gold = [2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2]
magenta = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]  
answer = []

#Début du programme
intro()
game()
results()
outro()