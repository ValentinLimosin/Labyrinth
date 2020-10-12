import pygame
from pygame.locals import QUIT,KEYDOWN,K_KP_PLUS,K_KP_MINUS,MOUSEBUTTONDOWN
from random import randrange

class Cell:				 #Classe représentant une case
	def __init__(self):
		self.N = True	   #Mur du Nord
		self.S = True	   #Mur du Sud
		self.E = True	   #Mur de l'Est
		self.W = True	   #Mur de l'Ouest
		self.ID = 0		 #Id de la case (visité ou non)

def drawMaze(maze,screen,tailleX,tailleY,ratio):
	
	for i in range(tailleY):
		for j in range(tailleX):
			if maze[i][j].N:
				pygame.draw.line(screen,(0,0,0),(ratio*j,ratio*i),(ratio*j+ratio,ratio*i),ratio//6)
			if maze[i][j].W:
				pygame.draw.line(screen,(0,0,0),(ratio*j,ratio*i),(ratio*j,ratio*i+ratio),ratio//6)


def drawTree(maze,screen,tailleX,tailleY,ratio):
	for i in range(tailleY):
		for j in range(tailleX):
			if not maze[i][j].N:
				pygame.draw.line(screen,(0,0,255),(ratio*j+(ratio//2),ratio*i+(ratio//2)),(ratio*j+(ratio//2),ratio*i-(ratio//2)),ratio//6)
			if not maze[i][j].W:
				pygame.draw.line(screen,(0,0,255),(ratio*j+(ratio//2),ratio*i+(ratio//2)),(ratio*j-(ratio//2),ratio*i+(ratio//2)),ratio//6)
	for i in range(tailleY):
		for j in range(tailleX):
			pygame.draw.circle(screen,(255,0,0),(ratio*j+(ratio//2),ratio*i+(ratio//2)),ratio//6)


def gen(x,y):
	pygame.init()
	screen = pygame.display.set_mode((1280,720))
	clock = pygame.time.Clock()
	FPS = 15
	tailleX = 16
	tailleY = 9
	ratio = 1280//tailleX
	maze = [[Cell() for i in range(0,tailleX,1)] for j in range(0,tailleY,1)]
	screen.fill((255,255,255))
	#drawMaze(maze,screen,tailleX,tailleY,ratio)
	drawTree(maze,screen,tailleX,tailleY,ratio)
	pygame.display.flip()
	yes = False
	backtrack = [(y,x)]
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == KEYDOWN:
				if event.key == K_KP_PLUS:
					FPS = FPS + 10 if FPS+10 < 75 else 75
				if event.key == K_KP_MINUS:
					FPS = FPS - 10 if FPS-10 > 0 else 1
			if event.type == MOUSEBUTTONDOWN:
				yes = False if yes else True
		if not backtrack:
			yes = False
		if yes:
			screen.fill((255,255,255))
			#drawMaze(maze,screen,tailleX,tailleY,ratio)
			drawTree(maze,screen,tailleX,tailleY,ratio)
			pygame.display.flip()
			maze[y][x].ID = 1
			check = []
			if x > 0 and maze[y][x-1].ID == 0:
				check.append('W')
			if y > 0 and maze[y-1][x].ID == 0:
				check.append('N')
			if x < tailleX-1 and maze[y][x+1].ID == 0:
				check.append('E')
			if y < tailleY-1 and maze[y+1][x].ID == 0:
				check.append('S')
			if len(check):
				backtrack.append([y,x])
				index = randrange(0,len(check),1)
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
				pygame.draw.rect(screen,(255,255,0),(ratio*x+1,ratio*y+1,ratio,ratio),0)
				pygame.display.flip()
			else:
				y,x = backtrack.pop()
				pygame.draw.rect(screen,(100,100,255),(ratio*x+1,ratio*y+1,ratio,ratio),0)
				pygame.display.flip()
		clock.tick(FPS)
		
gen(0,0)
