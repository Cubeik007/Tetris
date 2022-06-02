from tarfile import BLOCKSIZE
from tkinter import LEFT
import pygame
import random
from pygame.locals import *
import time

pygame.font.init()

# GLOBALS VARS
BLOCK_SIZE = 25
PLAY_WIDTH_BLOCKS = 10
PLAY_HEIGHT_BLOCKS = 20
LEFT_SPACE = 5
RIGHT_SPACE = 10
UP_SPACE = 3
DOWN_SPACE = 4
S_WIDTH = (PLAY_WIDTH_BLOCKS+LEFT_SPACE+RIGHT_SPACE)*BLOCK_SIZE
S_HEIGHT = (PLAY_HEIGHT_BLOCKS+UP_SPACE+DOWN_SPACE)*BLOCK_SIZE
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

TOP_LEFT_X = LEFT_SPACE*BLOCK_SIZE
TOP_LEFT_Y = UP_SPACE*BLOCK_SIZE


# SHAPE FORMATS

S = [['.00.',
      '00..'],
     [ 
      '0.',
      '00',
      '.0',
        ]]

Z = [[ 
       
      '00.',
      '.00',
        ],
     [ 
      '.0.',
      '00.',
      '0..',
        ]]

I = [['0',
      '0',
      '0',
      '0',
        ],
     [ 
      '0000.',
       
       
        ]]

O = [[  
      '00',
      '00',
        ]]

J = [[ 
      '0..',
      '000',     
        ],
     [ 
      '00',
      '0.',
      '0.',
        ],
     [ 
       
      '000',
      '..0',
        ],
     [ 
      '.0.',
      '.0.',
      '00.',
        ]]

L = [[ 
      '..0',
      '000',   
        ],
     [ 
      '0.',
      '0.',
      '00',
        ],
     [ 
       
      '000',
      '0..',
        ],
     [ 
      '00',
      '.0',
      '.0',
        ]]

T = [[ 
      '.0.',
      '000',
        ],
     [ 
      '0.',
      '00',
      '0.',
        ],
     ['000',
      '.0.',
        ],
     [ 
      '.0',
      '00',
      '.0',
      ]]


# index 0 - 6 represent shape



class Game:
      def __init__(self):
            pygame.init()
            self.surface = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
            self.surface.fill(BLACK)
            font = pygame.font.Font('freesansbold.ttf', 32)
            self.text = font.render('Tetris', True, WHITE, BLACK)
            self.textRect = self.text.get_rect()
            self.textRect.center = (TOP_LEFT_X+PLAY_WIDTH_BLOCKS*BLOCK_SIZE/2, 32)
            self.grid = [["." for x in range(PLAY_WIDTH_BLOCKS)] for y in range(PLAY_HEIGHT_BLOCKS)]
            self.active_grid = [["." for x in range(PLAY_WIDTH_BLOCKS)] for y in range(PLAY_HEIGHT_BLOCKS)]
            self.current_shape = None
            self.orientation = 0
            self.coordinates =  [0, PLAY_WIDTH_BLOCKS // 2]
            self.shapes = [S, Z, I, O, J, L, T]
            self.shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
            self.time = 0.5

      def draw_grid(self):
            for y in range(PLAY_HEIGHT_BLOCKS): #(PLAY_HEIGHT_BLOCKS):
                  # print(y, TOP_LEFT_Y+y*BLOCK_SIZE)
                  for x in range(PLAY_WIDTH_BLOCKS):
                        # print(TOP_LEFT_X+x*BLOCK_SIZE, y)
                        rect = pygame.Rect(TOP_LEFT_X+x*BLOCK_SIZE, TOP_LEFT_Y+y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                        if self.grid[y][x] == ".":
                              if self.active_grid[y][x] == ".":  
                                    pygame.draw.rect(self.surface, (255, 0, 0), rect, 1)
                              else:
                                    color = self.shape_colors[self.current_shape]
                                    pygame.draw.rect(self.surface, color, rect, 0)
                        else:
                              color = self.grid[y][x]
                              pygame.draw.rect(self.surface, color, rect, 0)

      def draw_object(self, object, orientation, position_x, position_y):
            object = object[orientation]

      def get_shape(self):
            self.current_shape = random.randint(0, len(self.shapes)-1)

      def update_active_grid(self):
            print(self.shapes[self.current_shape])
            height_of_shape = len(self.shapes[self.current_shape][self.orientation])
            width_of_shape = len(self.shapes[self.current_shape][self.orientation][height_of_shape-1])
            for y in range(height_of_shape):
                  for x in range(width_of_shape):
                        self.active_grid[y+self.coordinates[0]][x + self.coordinates[1]] = self.shapes[self.current_shape][self.orientation][y][x]



      def run(self):
            running = True
            while running:
                  self.surface.fill(BLACK)
                  self.surface.blit(self.text, self.textRect)
                  for event in pygame.event.get():
                        if event.type == QUIT:
                              running = False
                        self.draw_grid()
                        if self.current_shape == None:
                              time.sleep(self.time)
                              self.get_shape()
                              self.coordinates = [0, PLAY_WIDTH_BLOCKS // 2]
                  self.update_active_grid()
                  pygame.display.update()
                  self.coordinates[0] += 1
                  print(self.coordinates)
                  time.sleep(self.time)



        


def create_grid(locked_positions={}):
      grid = [[BLACK for _ in range(10)] for x in range(20)]

      


def convert_shape_format(shape):
	pass

def valid_space(shape, grid):
	pass

def check_lost(positions):
	pass

def get_shape():
	pass


def draw_text_middle(text, size, color, surface):
	pass
   
def draw_grid(surface, row, col):
	pass

def clear_rows(grid, locked):
    pass


def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
	pass

def main():
	pass

def main_menu():
	pass

if __name__ == "__main__":
    game = Game()
    game.run()