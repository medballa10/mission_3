import turtle
x=turtle.Turtle()
def rectangle(width,hight,color):
    """trace un rectangle de longueur 'width' et de largeur 'hight' et de couleur 'color'
        pre: `color` spécifie une couleur.
        La tortue `x` est initialisée.
        La tortue est placée à un sommet et orientée en direction d'un côté du rectangle.
        post: Le rectangle a été tracé sur la droite du premier côté.
        La tortue est à la même position et orientation qu'au départ.
        """
    x.color(color)
    x.pendown()
    x.begin_fill()
    for i in range(2):
        x.forward(width)
        x.left(90)
        x.forward(hight)
        x.left(90)
    x.penup()
    x.end_fill()
def emptystar(size,color):
    """ pre:fonction qui trace une étoile vide de cinq arêtes, chacune de taille "size" et de couleur "color"
        post:l'étoile vide a été tracé sur la droite du premier côté d'un degré de 144 
    """
    x.pencolor(color)
    x.pensize(6)
    x.pendown()
    for i in range(5):
        x.forward(size)
        x.right(144)
    x.penup()   

def fullstar(size,color):
    """ pre:fonction qui trace une étoile pleine de cinq arêtes, chacune de taille "size" et de couleur "color"
        post:l'étoile pleine a été tracé sur la droite du premier côté d'un degré de 144 
    """
    x.color(color)
    x.pendown()
    x.begin_fill()
    for i in range(5):
        x.forward(size)
        x.left(144)
    x.penup()
    x.end_fill()
    
def fullstar_2(size,color):
    """ pre:fonction qui trace une étoile pleine de cinq arêtes, chacune de taille "size" et de couleur "color"
        post:l'étoile pleine a été tracé sur la gauche du premier côté d'un degré de 144 
    """
    x.color(color)
    x.pendown()
    x.begin_fill()
    for i in range(5):
        x.forward(size)
        x.right(144)
    x.penup()
    x.end_fill()
    
def disk(radius,color):
    """ fonction qui trace un disque de rayon 'radius' et de couleur 'color'
       pre: `color` spécifie une couleur..
        post: Le disque a été tracé sur la droite du premier côté.
        La tortue est à la même position et orientation qu'au départ.
        """ 
    x.color(color)
    x.pendown()
    x.begin_fill()
    x.circle(radius)
    x.penup()
    x.end_fill()
    

def croissant(radius_1,color_1,radius_2,color_2):
    """fonction qui trace un croissant à l"aide de deux disque, par l'intermidiaire de la fonction disk
        pre: 'color_1' spécifie la couleur de disque 1
             'color_2' spécifie la couleur de disque 2
             la methode goto est utulié pour décaler le deuxieme disque du premier
        post: le croissant est tracé par la superposition de deux diques
        """
    disk(radius_1,color_1)
    x.goto(150,60)
    disk(radius_2,color_2)

def morrocan_flag(width):
    x.penup()
    x.goto(-800,100)
    x.pendown()
    rectangle((3/2)*width,width,"red")
    x.goto(-560,340)
    emptystar((1/3)*width,"green")

    
def algerian_flag(width):
    x.penup()
    x.goto(400,100)
    x.pendown()
    rectangle((3/2)*width,width,"green")
    x.penup()
    x.goto(700,100)
    x.pendown()
    rectangle((3/4)*width,width,"white")
    x.goto(700,170)
    x.pendown()
    disk((1/3)*width,"red")
    x.goto(740,200)
    x.pendown()
    disk((1/4)*width,"white")
    x.goto(700,280)
    x.pendown()
    fullstar((1/4)*width,"red")
morrocan_flag(400)
algerian_flag(400)
