

label test :
    scene bg f
    #condition pour cheker la valeur de Nolate
    if Nolate:
        show eileen concerned at right 
        saki '...'
        hide eileen concerned
        show yamato at left
        yamato 'a l\'heure comme toujours'
    else :
        show yamato at right
        with dissolve
        yamato 'sa fait des heures que je t\'attend '
        show eileen concerned at left
        with dissolve
        saki 'déso... j\'etais partie boire un verre en ville j\'avais soif'

    if bad == 100:
        narateur'game over'
        return
    else :
        show eileen concerned at right
        with fade
        saki 'du coup??'
        yamato 'ya un dunjon droit devant allons y c pas la'
        call screen map_tp

        saki "la carte ?"
    return        
   
