
# # Vous pouvez placer le script de votre jeu dans ce fichier.

# #variable 
# default Nolate = True
# default bad = 0


# # Déclarez sous cette ligne les images, avec l'instruction 'image'
# # ex: image eileen heureuse = "eileen_heureuse.png"
# # Déclarez les personnages utilisés dans le jeu.
# define narateur = Character('Narateur', color="#f10707")
# define saki = Character('Saki', color="#ffc8ed")
# define yamato = Character('yamato', color="#4dda91")



# Le jeu commence ici
label start:
    
    # scene:ajouter un fond = background
    scene bg f
    
    show screen dragN
    # pour la musique de fond :
    # play music "audio/musique.mp"

    # metre des lien meme si sa a pas vraiment d'utilité
    "???" '{a= https://www.youtube.com/watch?v=8WFoBbCYcI8} lien vers le tuto texte psk j\'ai pas mis toute les balise texte{/a}'

    "dev" "{a=jump:menui}aller au test menu{/a}"

    # ecrire le nom du perso et entre cote sont dialogue/ les point d'interogation coresponde au nom d'un perso non defini 
    "???" "c'etais une beau jour d'ete..... "

    # les anti slash sont la pour metre des guillement pour metre en avant le nom d'un perso
    "???" "\"saki\""

    # la balise {b} pour metre en gras {i}italique {u} souligner et {s}barrer et pas oublier de bien les fermer avec un slach
    "???" "{b}etais{/b}"

    #pour jouer avec la transparence des texte
    "???" "{alpha=0.5}sous un soleil de plond{/alpha}"

    # changer la couleur des texte
    "???" "{color=#8f4dda}puis{/color}"

    # le cps c pour aficher le texte letre par letre et choisir sa vitesse
    "???" "{cps=1}tout à coups{/cps}"

    # le {p} pour aller a la ligne mais le texte va se stoper et le joueur devra cliquer pour le refaire defiler on peut mettre un timer exemple {p=1.5}
    "???" "desbuit de plus en plus chelou {p} survin"

    # \n pour aller a la ligne basique
    saki 'il \n se passe quoi '

    #metre une variable dans un texte
    saki "j'ai bu [nb_verre]verres"

    # et le lien pour jump a une autre label 
    "???" "{a=jump:pub}aller directement au bar {/a}"

    # show pour montrer le png du perso 
    show screen no_idea
    show eileen concerned
    saki "fait chaud putin"
    # exemple de choix
    menu:
        "rester en foret":
            # pour changer de label (exemple changer de lieu passer de la ville a la foret)
            jump test
            # le jump test ma persi de passer sur le script 2 grace au inculde
        "aller boire un verre":
            jump pub

    # label on va dire que c'est egale au differante scene du jeu
    label foret:
        # hide pour cacher le png du perso
        hide eileen concerned
        narateur "toujours a la foret"
    return

    label pub :
        #on change la variable car saki eera en retard
        $ Nolate = False
        $ bad = 100
        scene bg v
        # with est une transition il existe dissove ou fade
        with dissolve
        # pour jouer un bruit comme par exemple des de voiture on peut faire: play sound "audio/nom du fichier.mp3" et quel que reglage volume0.25 noloop
        show eileen concerned
        saki "jai soif, allons au bar"
    
        narateur "apres avoir bu un verre saki retourne dans la foret"
        jump test
  



