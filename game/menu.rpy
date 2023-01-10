default boucl1 = 0

label menui :
    'test menu'
    menu boucle :
        saki "fait un choix"

        "toi":
            saki 'non'
            jump boucle
        "moi":
            saki "viiii"
            'serieux ?'
            saki 'non je deconne'
            jump boucle
        "le monde":
            saki 'peut-etre'
            jump suite

label suite :
    'la valeur de la var est [boucl1]'
    menu boucle2 :

        saki "qui meurt"

        "je meurt" if boucl1 == 0 :

            saki "non"

            $ boucl1 +=1

            jump boucle2
        "tu meurt" if boucl1 == 1 :

            saki "viiii"

            'serieux ?'

            saki 'non je deconne tjr'

            $ boucl1 +=1

            jump boucle2
        "le monde meurt" if boucl1 == 2 :

            saki 'peut-etre'
            'test'
            'test2'

            jump suite2

label suite2 :  
    saki "enfin j'ai la logic je crois"           
