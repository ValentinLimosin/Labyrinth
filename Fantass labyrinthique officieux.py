from random import *
from tkinter import *
import random
import time
COLORS = ['red', 'orange',
    'yellow', 'green', 'blue', 'purple']
####################################################
# N = 1/S = 3/E = 4/W = 2
#
#           Fait par:Jean-Baptiste Labat
#           le : 20/02/2017
#           mis a jour le: 01/03/2017
#
####################################################

def imp(verif,x,y):                   #Fait la vérification pour chacune des cases du labyrinthe.
    global maze
    if maze[y][x].N == False:   #Verifie si i il n'y a pas de mur au point cardinal conce`rné et si la case n'est pas visitée
        if maze[y-1][x].ID == 1:
            verif.append(0)     #Rempli la liste verif avec le numéro associé au point cardinal si les conditions sont respectées       
    if maze[y][x].W == False:
        if maze[y][x-1].ID == 1:
            verif.append(1)             
    if maze[y][x].S == False:
        if maze[y+1][x].ID == 1:
            verif.append(2)             
    if maze[y][x].E == False:
        if maze[y][x+1].ID == 1:
            verif.append(3)
    return(verif)

def resolv(x,y):                 #Fonction mère qui se charge de la résolution du labyrinthe qui renvoit la liste des coordonnées des cases traversées.
    global width
    global height
    global maze
    global coords

    coords=[0,0]
    if height == 0 or width == 0 :        #Condition vérifiant la taille du labyrinthe initial est de 0*0 qui arrête le programme.
            print("Error : 404")
            return(False)
    while y != height-1 or x != width-1 :   #Tant que les coordonnées ne sont pas arrivées à leur maximum, continuer la boucle Tant que.
        verif = []
        verif = imp(verif,x,y)                #Utilisation de la fonction de vérification.
        maze[y][x].ID = 2
        if len(verif) > 0 :
            b = random.choice(verif)    #Si la liste renvoyée contient des éléments, sélectionner un élément aléatoire.
            if b == 2 :
                coords.extend((x,y+1))  #Ajoute les coordonnées suivantes à la liste principale. Ici, les coordonnées de la case au Sud.
            elif b == 3 :
                coords.extend((x+1,y))
            elif b == 0 :
                coords.extend((x,y-1))
            elif b == 1 :
                coords.extend((x-1,y))
        else :
            del coords[-2:]         #Si la liste n'est composée d'aucun élément, suppression des 2 derniers éléments de la listes : les coordonnées de la case où le programme est bloqué.
        x = coords[len(coords)-2]   #Refait la boucle av-ec les deux derniers éléments de la nouvelle liste à savoir les deux coordonnées de la case d'après.
        y = coords[len(coords)-1]
    return (coords) #Fin de la fonction, renvoi de la liste de coordonnées qui est exploitée par l'affichage.

def initresolv():
    if height != 0 or width != 0 :
        resolv(0,0)
        drawresult()
        impresolv()
    else :
        return (False) 

####################################################
# N = 1/S = 3/E = 4/W = 2
#
#           Fait par:Valentin Limousin
#           le : 20/02/2017
#           mis a jour le: 28/02/2017
#
####################################################

class Cell:                 #Classe représentant une case
    def __init__(self):
        self.N = True       #Mur du Nord
        self.S = True       #Mur du Sud
        self.E = True       #Mur de l'Est
        self.W = True       #Mur de l'Ouest
        self.ID = 0         #Id de la case (visité ou non)

def gen(x,y):
    global height
    global width
    global maze
    if height == 0 or width == 0:   #si il n'y a pas de l'abyrinthe on sort du programme
        return(False)
    i = 0
    backtrack = [(y,x)]             #initialisation de la variable contenant la coordoné des case ou l'on est passé
    while backtrack:
        maze[y][x].ID = 1           #Set de la case actuel comme vue
        check = []                  #Initialisation de la variable contenant l'orientation des cases non visité autour
        if x > 0 and maze[y][x-1].ID == 0:          #Si il y a une case non visité a l'Ouest
            check.append('W')
        if y > 0 and maze[y-1][x].ID == 0:          #Si il y a une case non visité au Nord
            check.append('N')
        if x < width-1 and maze[y][x+1].ID == 0:    #Si il y a une case non visité au Est
            check.append('E')
        if y < height-1 and maze[y+1][x].ID == 0:   #Si il y a une case non visité au Sud
            check.append('S')
        if len(check):                              #Si il reste toujours une case non visité autour
            backtrack.append([y,x])
            index = randrange(0,len(check),1)       #On choisie aléatoirement une case autour
            if check[index] == 'N':
                maze[y][x].N = False
                y -= 1
                maze[y][x].S = False
            if check[index] == 'W':
                maze[y][x].W = False
                x -= 1
                maze[y][x].E = False
            if check[index] == 'S':
                maze[y][x].S = False
                y += 1
                maze[y][x].N = False
            if check[index] == 'E':
                maze[y][x].E = False
                x += 1
                maze[y][x].W = False
        else:
            y,x = backtrack.pop()                   #sinon on ressort une autre coordonnée

def initcrea():
    global maze
    global height
    global width
    global coords
    hauteur = h.get()
    largeur = w.get()
    height = int(hauteur)
    width = int(largeur)
    if maze:
        can1.delete("all")
        del maze
    maze = []
    maze = [[Cell() for i in range(0,width,1)] for j in range(0,height,1)]
    gen(0,0)
    drawngen()


####################################################
# N = 1/S = 3/E = 4/W = 2
#
#           Fait par:Etienne Simao
#           le : 20/02/2017
#           mis a jour le: 21/02/2017
#
####################################################
def disablecrea():
    global b1
    b1.config(state=DISABLED)
def enablecrea():
    global b1
    b1.config(state=NORMAL)

    
def drawngen():
    global width
    global height
    global maze
    global can1
    x1 = 0
    y1 = 0
    if width == 66 and height == 66 : #1er Easter egg 66*66
        can1.create_rectangle(0, 0, w.winfo_screenwidth(), w.winfo_screenheight()-100, fill ='red')
    if width == 9 and height == 11 :  #2ème Easter egg 9*11
        can1.create_rectangle(w.winfo_screenwidth()-1500, w.winfo_screenheight()-1000, w.winfo_screenwidth()-1100, w.winfo_screenheight()-100, fill ='grey96', outline="")
        can1.create_rectangle(w.winfo_screenwidth()-900, w.winfo_screenheight()-1000, w.winfo_screenwidth()-500, w.winfo_screenheight()-100, fill ='grey95', outline="")
    if width == 42 and height == 42 : #3ème Easter egg 420*420
        if height>=width:
            rapport=w.winfo_screenheight()/height
        if width>height:
            rapport=w.winfo_screenwidth()/width
        for y in range(height):
            for x in range(width):
                if maze[y][x].N == True:
                    can1.create_line(x1,y1,x1+((w.winfo_screenwidth())/width),y1,width=rapport/7,fill=random.choice(COLORS))
                if maze[y][x].W == True:
                    can1.create_line(x1,y1,x1,y1+((w.winfo_screenheight()-100)/height),width=rapport/7,fill=random.choice(COLORS))
                if maze[y][x].E == True:
                    can1.create_line(x1+((w.winfo_screenwidth())/width),y1,x1+((w.winfo_screenwidth())/width),y1+((w.winfo_screenheight()-100)/height),width=rapport/7,fill=random.choice(COLORS))
                if maze[y][x].S == True:
                    can1.create_line(x1,y1+((w.winfo_screenheight()-100)/height),x1+((w.winfo_screenwidth())/width),y1+((w.winfo_screenheight()-100)/height),width=rapport/7,fill=random.choice(COLORS))
                x1 = x1+((w.winfo_screenwidth())/width)
            y1 = y1 + ((w.winfo_screenheight()-100)/height)
            x1 = 0
    else :
        if height>=width:
            rapport=w.winfo_screenheight()/height
        if width>height:
            rapport=w.winfo_screenwidth()/width
        for y in range(height):
            
            for x in range(width):
                
                if maze[y][x].N == True:
                    can1.create_line(x1,y1,x1+((w.winfo_screenwidth())/width),y1,width=rapport/7,fill="Black")
                if maze[y][x].W == True:
                    can1.create_line(x1,y1,x1,y1+((w.winfo_screenheight()-100)/height),width=rapport/7,fill="Black")
                if maze[y][x].E == True:
                    can1.create_line(x1+((w.winfo_screenwidth())/width),y1,x1+((w.winfo_screenwidth())/width),y1+((w.winfo_screenheight()-100)/height),width=rapport/7,fill="Black")
                if maze[y][x].S == True:
                    can1.create_line(x1,y1+((w.winfo_screenheight()-100)/height),x1+((w.winfo_screenwidth())/width),y1+((w.winfo_screenheight()-100)/height),width=rapport/7,fill="Black")
                x1 = x1+((w.winfo_screenwidth())/width)
            y1 = y1 + ((w.winfo_screenheight()-100)/height)
            x1 = 0
    can1.create_rectangle(0,0,((w.winfo_screenwidth())/width),((w.winfo_screenheight()-100)/height),fill = "cyan", outline="")
    can1.create_rectangle((width-1)*((w.winfo_screenwidth())/width),(height-1)*((w.winfo_screenheight()-100)/height),(width-1)*((w.winfo_screenwidth())/width)+((w.winfo_screenwidth())/width),(height-1)*((w.winfo_screenheight()-100)/height)+((w.winfo_screenheight()-100)/height),fill = "green", outline="")
    if width == 11 and height == 11 :  #4ème Easter egg 11*11
        can1.create_text(w.winfo_screenwidth()-75, w.winfo_screenheight()-125, text="BIG UP AU STAGIAIRE", fill="red")
        
def drawresult():
    global height
    global width
    global coords, coordsx, coordsy
    x = width - 1
    y = height - 1
    while len(coords) != 2:
        x1 = x*((w.winfo_screenwidth())/width)
        y1 = y*((w.winfo_screenheight()-100)/height)
        coordsx.append(x1)
        coordsy.append(y1)
        del coords[-2:]
        x = coords[len(coords)-2]
        y = coords[len(coords)-1]
    del coords
    coordsx.append(0)
    coordsy.append(0)
    

def impresolv():
    global coordsx, coordsy, height, width, b1
    disablecrea()
    if height>=width:
        rapport=w.winfo_screenheight()/height
    if width>height:
        rapport=w.winfo_screenwidth()/width
    if len(coordsx) > 0 :
        if height == 66 and width == 66 :
            can1.create_line(coordsx[len(coordsx)-1]+(((w.winfo_screenwidth())/width)/2),coordsy[len(coordsx)-1]+(((w.winfo_screenheight()-100)/height)/2),coordsx[len(coordsx)-2]+(((w.winfo_screenwidth())/width)/2),coordsy[len(coordsx)-2]+(((w.winfo_screenheight()-100)/height)/2),width=int(rapport/7),fill="white")
        elif height == 42 and width == 42 or height == 420 and width ==420: #Pour les Easter eggs 42*42 et 420*420
            can1.create_line(coordsx[len(coordsx)-1]+(((w.winfo_screenwidth())/width)/2),coordsy[len(coordsx)-1]+(((w.winfo_screenheight()-100)/height)/2),coordsx[len(coordsx)-2]+(((w.winfo_screenwidth())/width)/2),coordsy[len(coordsx)-2]+(((w.winfo_screenheight()-100)/height)/2),width=int(rapport/7),fill=random.choice(COLORS))
        else :
            can1.create_line(coordsx[len(coordsx)-1]+(((w.winfo_screenwidth())/width)/2),coordsy[len(coordsx)-1]+(((w.winfo_screenheight()-100)/height)/2),coordsx[len(coordsx)-2]+(((w.winfo_screenwidth())/width)/2),coordsy[len(coordsx)-2]+(((w.winfo_screenheight()-100)/height)/2),width=int(rapport/7),fill="red")
        del coordsy[-1:]
        del coordsx[-1:]
        can1.after(3, impresolv)
    else :
        enablecrea()
    return(True)
        

#création d'une fenetre principale
        
fenetre = Tk()
maze = []
height = 0
width = 0
coords=[]
coordsy=[]
coordsx=[]
fenetre.title('Le générateur et le solveur de labyrinthe')

# création de widgets 'Button':
b1 = Button(fenetre, text ='Générer ', command=initcrea ,relief=RAISED)
b2 = Button(fenetre, text ='Résoudre ',command=initresolv, relief=RAISED)
b3 = Button(fenetre, text ='Quitter ', command=fenetre.destroy, relief=RAISED)

w = Entry(fenetre)
h = Entry(fenetre)

# création d'un widget 'Canvas' :
can1 = Canvas(fenetre, width = w.winfo_screenwidth(), height = w.winfo_screenheight()-100, bg ='white')
    

 
# Mise en page à l'aide de la méthode 'grid' :
w.insert(0, 'Largeur')
h.insert(0, 'Hauteur')
b1.grid(row=1,column = 0)
w.grid(row=1,column = 1)
h.grid(row=1,column = 2)
b2.grid(row=1,column = 3)
b3.grid(row=1,column = 4)

can1.grid(row=0,column = 0,columnspan = 5)

# démarrage :
fenetre.mainloop()
