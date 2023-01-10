# définir un écran nommé "no_idea" pour cree un btn image clicable

screen no_idea: 
    # définir un cadre
    frame:
        #technique pour chacher la frame
        xpos -75
        ypos -75
        
        # définir un bouton d'image
        imagebutton:
            # les pos pour repositioner le button
            xpos 80
            ypos 80
            idle "btn.png" 
            hover "btnn.png"
            # définir l'action du bouton
            action [Hide("no_idea"),Jump('test')]
# faire une map pour pouvoir se tp d'un point A a un point B            
screen map_tp:
    imagemap:
        ground "map.png"
        #bonne chance pour trouver les bonne coordonée et trouver un moyen de fair comprendre ou cliquer
        hotspot (0,0,500,500) action [Hide("map_tp"),Jump('dunj')]
        hotspot (200,200,200,0) action [Hide("map_tp"),Jump('test')]     
        hotspot (500,0,500,500) action [Hide("map_tp"),Jump('pub')]
# drag'n Drop 
 
init python:
    def fct1(drags,drop):
        if not drop:
            return
        else:
            if drop.drag_name == "bag" and drop.droppable:
                # The element is valid, do something with it
                pass
            else:
                # Handle the case where the element is not dropped on a valid hotspot......(si j'aurais voulu fair un jump en function j'airais du faire python_jump)
                pass
    def fct2(drags,drop):
        if drop.drag_name != "bag":
            cancel_drag() 
        

screen dragN :
    draggroup:
        drag:
            drag_name "pomme"
            child "pom.png" 
            xalign 0.1
            yalign 0.1 
            #droppable c'est pour savoir si on peut metre des truc dessu (alors c soit comme un inventaire sois de la combinaison d'object j'ai âs tout compris) 
            droppable False 
            #function dragged : pour savoir comment sa reagis quand on le deplace 
            dragged fct1
            #function dropped qui dit comment il reagis quand on met quel que chose sur lui
            dropped fct2
            #elle sert pendant que on deplace l'object mais j'ai pas trop compris 
            # activated fct3
        drag: 
            drag_name "bag"
            child "bag.png"
            xalign 0.5
            yalign 0
            droppable True 
            draggable False
            


