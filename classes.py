import pygame
import random
import numpy as np 

def movement(directionx, directiony,x, y, speed,size):

        speed = speed//10
        
        if directionx > 0:

            x += speed + random.randint(-1, 1)
            if x > 800-size:
                x = 800-size

        elif directionx < 0:

            x -=speed  + random.randint(-1, 1)
            if x < 0:
                x= 0

        if directiony > 0:

            y +=speed  + random.randint(-1, 1)
            if y > 600-size:
                y = 600-size

        elif directiony < 0:

            y -=speed  + random.randint(-1, 1)
            if y < 0:
                y = 0

        return x, y

def all_colors():
    white = (255, 255, 255)
    blue  = (0,0,255)
    red = (255,0,0)
    lime = (0,255,0)
    yellow = (255,215,0)
    orange = (255,165,0)
    turquasie = (0, 255,255)
    purple = (255,0,255)
    black = (0,0,0)
    magenta = (255,0,255)
    maroon = (128,0,0)
    olive = (128,128,0)
    green = (0,128,0)
    navy = (0,0,128)
    teal = (0,128,128)
    purple = (128,0,128)
    silver = (192,192,192)

    colors = [green, black, white, blue, lime, maroon, olive, red, magenta, yellow, orange, navy, teal, purple, silver]
    return colors

class GA:

    def __init__(self, parents):

        
        self.parents = parents

    def crossover(self):

        parent1 = self.parents[0]
        parent2 = self.parents[1]
        
        parentlen = len(parent1)

        gene1 = np.concatenate((parent1[:parentlen-1], parent2[parentlen-1:]))
        gene2 = np.concatenate((parent2[:parentlen-1], parent1[parentlen-1:]))

        return gene1, gene2

    def mutation(self, gene, rate):
        
        
        for idx, x in enumerate(gene):

            if random.randint(0, rate) == rate:

                randomvalue = np.random.uniform(0.4,1.6)
                
                gene[idx] = gene[idx] * randomvalue
                
        
        return gene

