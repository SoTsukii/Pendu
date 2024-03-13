mot_secret = "linguistique" # Ici on définie quel est le mot secret 
mot_devine = ""

for mot in range(0, len(mot_secret)): # On fait une boucle pour ajouter "_" en fonction du nombre de lettre dans le mot secret 
    mot_devine = mot_devine + "_"

tentatives = 0 # Compteur de tentatives 

while True: # Boucle while pour demander a l'utilisateur d'entre une lettre tant qu'il lui reste des tentatives 
    print("Tu es a : ", tentatives," erreurs sur 8")
    print("Le mot à deviner est : ", mot_devine)
    lettre_proposee = input("Entrez une lettre : ") # On définie la variable lettre_propose par l'entre d'une lettre par l'utilisateur 
    lettre_trouvee = False # On part du principe que la lettre saisie est fausse mais si on la trouve contenue dans le mot alors on transforme la chose en vrai si c'est bel et bien False alors on ajoute une erreur 

    for mot in range(len(mot_secret)): # On fait une boucle pour modifier le "_" par la lettre que l'utilisateur entre si elle est contenue dans le mot secret 
        if lettre_proposee == mot_secret[mot]:
            mot_devine = mot_devine[:mot] + lettre_proposee + mot_devine[mot + 1:]
            lettre_trouvee = True # Change la variable en True pour savoir si on ajoute une erreurs ou non 

    if not lettre_trouvee: # Si la lettre n'es pas dans le mot secret alors on rajoute 1 au compteur d'erreurs 
        tentatives += 1

    if tentatives == 8: # Si l'utilisateur a fait 8 erreurs le jeu s'arrête et affiche le mot 
        print("Tu as atteint 8 erreurs. Tu as perdu, le mot était :", mot_secret)
        break
    elif mot_secret == mot_devine: # Si l'utilisateur trouve alors il a gagné 
        print("Tu as gagné. Le mot était :", mot_devine)
        break

