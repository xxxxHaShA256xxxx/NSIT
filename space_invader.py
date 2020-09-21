import pygame
import random
import space
import sys

class joueur:
    def __init__(self):
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = sens
        self.vitesse = 10
        self.score = 0
    def deplacer(self):
        if self.sens == 'droite' and self.positions < 740:
            self.positions += vitesse
        elif self.sens == 'gauche' and self.positions > 0:
            self.positions -= vitesse
    def tirer(self):
        pass
    def marquer(self):
        self.score = self.score + 1
class Balle:
    def __init__(self):
        self.tireur = tireur
        self.depart = tireur.positions + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "charger"
        self.vitesse = 5
    def bouger(self):
        if self.etat == "attendre":
            self.depart = self.tireur.positions + 16
            self.hauteur = 492
        elif self.etat == "tirer":
            self.hauteur -= 5
        if self.hauteur < 0:
            self.etat = "charger"
    def Blesser(self):
        pass
class Ennemi:
    Nombre_Ennemie = 10
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if(self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif(self.type == 2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
            
    def avancer(self):
        self.hauteur += self.vitesse
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  self.type == 1:
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif self.type ==2:
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2

pygame.init() 


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jeux dans L'espace") 

fond = pygame.image.load('background.png')


player = space.Joueur()

tir = space.Balle(player)
tir.etat = "charger"

listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
    

running = True 

while running : 
    
    screen.blit(fond,(0,0))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            running = False 
            sys.exit() 
       
       
        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_LEFT:
                player.sens = "gauche" 
            if event.key == pygame.K_RIGHT :  
                player.sens = "droite" 
            if event.key == pygame.K_SPACE : 
                player.tirer()
                tir.etat = "tirer"

   
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            ennemi.disparaitre()
            player.marquer()
    print(f"Score = {player.score} points")
    
    
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur])        
    
    tir.bouger()
    screen.blit(player.image,[player.position,500]) 
    
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) 
        
    pygame.display.update() 

