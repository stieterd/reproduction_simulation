import pygame
import random
import numpy as np 
import classes
import csv


screenspecs = (800,600)

pygame.init()

colors = classes.all_colors()

screen = pygame.display.set_mode(screenspecs)
running = True
clock=pygame.time.Clock()
font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 25)
popsize = 600

pop = []

i = 0
mutationrate = 2

while i < popsize:  #x_pos 1                     #y_pos 2                    #size 3               #speed 4                 #deathrate 5        #reproduction 6   #age 7  #id 8        #color 9
    pop.append([random.randint(50, 800-50),random.randint(60,600-60),random.randint(5, 10), random.randint(10,40),  random.randint(3000, 21000),random.randint(10,20),  0    , i, random.choice(colors[3:])]) #first x and second y , third is size, forth is speed, fifth is death, then age, sixth reproduction, sixth id, seventh color
    i+=1





while running:

        avv_all = [0,0,0,0]
        avv_score = 0

        
        clock.tick(60)
        screen.fill((colors[2]))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        new = []
        remlist = []

        for index, element1 in enumerate(pop):
            
            rect_1 = pygame.Rect(element1[0], element1[1], element1[2], element1[2])
            for element2 in pop[index + 1:]:
                
                rect_2 = pygame.Rect(element2[0], element2[1], element2[2], element2[2])
                if rect_1.colliderect(rect_2) == 1 :
                    if element1 != element2:
                        if element1[-2] != element2[-2]:
                            if element1[-3] > 100 and element2[-3] > 800:

                                id_b = random.randint(0,2000)
                                id_b = random.choice([element1[-2], element2[-2]])
                            
                                ga = classes.GA((element1[2:-3], element2[2:-3]))
                                genes = list(ga.crossover())
                                i = 0
                                
                                while i < (element1[-4] + element2[-4])// 20:
                                    
                                    baby = ga.mutation(random.choice(genes), mutationrate)
                                    baby = list(baby)
                                    color = element1[-1]
                                    baby.append(0)
                                    baby.append(id_b)
                                    
                                    
                                    baby.append(color)
                                    
                                    baby.insert(0,element1[1])
                                    baby.insert(0,element1[0])
                                    
                                    #baby.insert(0,random.randint(50, 600-60))
                                    #baby.insert(0,random.randint(60,800-50))
                                    
                                    
                                    pop.append(baby)
                                    i +=1
                                if element1 not in remlist: 
                                    remlist.append(element1)
                                if element2 not in remlist:
                                    remlist.append(element2)
                                
                                
            for element in remlist:
                try:
                    pop.remove(element)  
                except:
                    pass   
            
            avlist = [element1[2],element1[3], element1[4],element1[5]]

            avv_all = [sum(pair) for pair in zip(avv_all, avlist)]
            avv_score+=1
            
            
            directionx = random.randint(-1,1)
            directiony = random.randint(-1,1)
            element1[0], element1[1] = classes.movement(directionx, directiony,element1[0], element1[1], element1[3], element1[2])
            plrfill = screen.fill(element1[-1], (element1[0], element1[1], element1[2], element1[2]))
            plr = pygame.draw.rect(screen, colors[1], (element1[0], element1[1], element1[2], element1[2]), 1)
            element1[-3] +=1
            if element1[-3] > element1[-5]:
                if element1 in pop:
                    pop.remove(element1)
                            
                        
            
        
        avv_all = [el//avv_score for el in avv_all]
        
        
        fps = str(int(clock.get_fps()))
        average = font2.render((f"The average is:"), True, pygame.Color('orange'))
        screen.blit(average, (490, 20))
        specs1 = font2.render(f"Size = {avv_all[0]}; speed = {avv_all[1]/10};", True, pygame.Color('orange'))
        screen.blit(specs1, (490, 40))
        specs2 = font2.render(f"Deathrate = {avv_all[2]}; reproduction = {avv_all[3]/10}", True, pygame.Color('orange'))
        screen.blit(specs2, (490, 60))
        text = font.render((f"FPS: {fps}"), True, pygame.Color('red'))
        screen.blit(text, (20, 20))
        poplentext = font.render((f"Amount of creatures: {len(pop)}"), True, pygame.Color('red'))
        screen.blit(poplentext, (20, 40))

        

        pygame.display.flip()