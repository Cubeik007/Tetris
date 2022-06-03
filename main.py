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
TIME = 0.5

TOP_LEFT_X = LEFT_SPACE*BLOCK_SIZE
TOP_LEFT_Y = UP_SPACE*BLOCK_SIZE


# SHAPE FORMATS

S = [['.00',
      '00.'],
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
      '.0',
      '00',
      '0.',
        ]]

I = [['0',
      '0',
      '0',
      '0',
        ],
     [ 
      '0000',
       
       
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
            self.current_shape = None
            self.orientation = 0
            self.my_shape = None
            self.coordinates =  [0, PLAY_WIDTH_BLOCKS // 2]
            self.shapes = [S, Z, I, O, J, L, T]
            self.shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
            self.time = TIME
            self.level = 1
            self.cleared_lines = 0
            self.points = [40, 100, 300, 1200]
            self.score = 0
            self.faster_time = self.time
            self.next_shape = [None, None]
            self.the_end = False
            self.highest_score = 0

      def draw_grid(self):
            for y in range(PLAY_HEIGHT_BLOCKS): #(PLAY_HEIGHT_BLOCKS):
                  # print(y, TOP_LEFT_Y+y*BLOCK_SIZE)
                  if self.current_shape != None:
                        self.draw_shape() 
                  for x in range(PLAY_WIDTH_BLOCKS):
                        # print(TOP_LEFT_X+x*BLOCK_SIZE, y)
                        rect = pygame.Rect(TOP_LEFT_X+x*BLOCK_SIZE, TOP_LEFT_Y+y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                        if self.grid[y][x] == ".":  
                                    pygame.draw.rect(self.surface, (255, 0, 0), rect, 1)
                        else:
                              color = self.grid[y][x]
                              pygame.draw.rect(self.surface, color, rect, 0)
            


      def get_shape(self):
            self.current_shape = self.next_shape[0]
            self.orientation = self.next_shape[1]
            self.next_shape[0] = random.randint(0, len(self.shapes)-1)
            self.next_shape[1] = random.randint(0, len(self.shapes[self.next_shape[0]])-1)
            

      def draw_shape(self):
            self.my_shape = self.shapes[self.current_shape][self.orientation]
            height_of_shape = len(self.my_shape)
            width_of_shape = len(self.my_shape[height_of_shape-1])
            for y in reversed(range(height_of_shape)):
                  for x in range(width_of_shape):
                        if self.my_shape[y][x] != ".":
                              if y+self.coordinates[0]+1 >= PLAY_HEIGHT_BLOCKS:
                                    self.update_grid()
                                    self.current_shape = None
                                    return None
                              elif self.grid[y+self.coordinates[0]+1][x+self.coordinates[1]] != ".":
                                    if self.coordinates[0] == 0:
                                          self.the_end = True
                                    self.update_grid()
                                    self.current_shape = None
                                    return None
                  for x in range(width_of_shape):
                        #self.active_grid[][x + self.coordinates[1]] = self.shapes[self.current_shape][self.orientation][y][x]
                        if self.my_shape[y][x] != ".":
                              cord_x = TOP_LEFT_X + (x+self.coordinates[1])*BLOCK_SIZE
                              cord_y = TOP_LEFT_Y + (y+self.coordinates[0])*BLOCK_SIZE
                              rect = pygame.Rect(cord_x, cord_y, BLOCK_SIZE, BLOCK_SIZE)
                              pygame.draw.rect(self.surface, self.shape_colors[self.current_shape], rect, 0)

      def update_grid(self):
            if self.my_shape == None:
                  return None
            for y in range(len(self.my_shape)):
                  for x in range(len(self.my_shape[y])):
                        # print(self.my_shape,x, y)
                        if self.my_shape[y][x] != ".":
                              # print(y+self.coordinates[0],x+self.coordinates[1])
                              # print(self.grid[y+self.coordinates[0]][x+self.coordinates[1]])
                              self.grid[y+self.coordinates[0]][x+self.coordinates[1]] = self.shape_colors[self.current_shape]

      def move_shape_left(self):
            if self.coordinates[1] == 0:
                  return None
            for y in range(len(self.my_shape)):
                  if self.grid[y+self.coordinates[0]][self.coordinates[1]-1] != ".":
                        return None
            self.coordinates[1] -= 1

      def move_shape_right(self):
            if self.coordinates[1]+len(self.my_shape[0]) ==  PLAY_WIDTH_BLOCKS:
                  return None
            for y in range(len(self.my_shape)):
                  if self.grid[y+self.coordinates[0]][self.coordinates[1]+len(self.my_shape[0])] != ".":
                        return None
            self.coordinates[1] += 1

      def check_full_lines(self):
            all_cleared = 0
            for y in range(PLAY_HEIGHT_BLOCKS):
                  counter = 0
                  for x in range(PLAY_WIDTH_BLOCKS):
                        if self.grid[y][x] == ".":
                              break
                        else:
                              counter += 1
                  if counter == PLAY_WIDTH_BLOCKS:
                        all_cleared += 1
                        self.grid.pop(y)
                        self.grid.insert(0, ["." for _ in range(PLAY_WIDTH_BLOCKS)])
            if all_cleared > 0:
                  self.cleared_lines += all_cleared
                  self.level = self.cleared_lines // 10 +1
                  self.score += self.points[all_cleared-1]*self.level

            
      def display_score(self):
            font = pygame.font.SysFont("arial", BLOCK_SIZE-5)
            current_score = font.render(f"Score:{self.score}", True, WHITE)
            lines_score = font.render(f"Lines:{self.cleared_lines}", True, WHITE)
            level = font.render(f"Level:{self.level}", True, WHITE)
            scores = [current_score, lines_score, level]
            for index, i in enumerate(scores):
                  index += 3
                  self.surface.blit(i, (10, index*BLOCK_SIZE))

            if self.score > self.highest_score:
                  self.highest_score = self.score
            highest = font.render(f"Highest score:{self.score}", True, WHITE)
            self.surface.blit(highest, ((LEFT_SPACE+PLAY_WIDTH_BLOCKS+2)*BLOCK_SIZE, UP_SPACE*BLOCK_SIZE))
            


      def game_over(self):
            font = pygame.font.SysFont("arial", 30)
            game_over_text = font.render(f"YOO LOST! Score:{self.score}, press R to restart", True, BLACK, WHITE)
            self.surface.blit(game_over_text, (10, 10))
            pygame.display.update()
            while True:
                  for event in pygame.event.get():
                        if event.type == QUIT:
                              pygame.quit()
                        if event.type == KEYDOWN and event.key == K_r:
                              self.restart_game()
                              return None

      def restart_game(self):
            self.grid = [["." for x in range(PLAY_WIDTH_BLOCKS)] for y in range(PLAY_HEIGHT_BLOCKS)]
            self.current_shape = None
            self.orientation = None
            self.my_shape = None
            self.score = 0
            self.cleared_lines = 0
            self.the_end = False
            self.coordinates =  [0, PLAY_WIDTH_BLOCKS // 2]


      def rotate_shape(self):
            if self.current_shape != None:
                  possible_orientations = len(self.shapes[self.current_shape])
                  self.my_shape = self.shapes[self.current_shape][self.orientation]
                  my_types = [ (_ +self.orientation) %  possible_orientations for _ in range(possible_orientations)]
                  necessary_change = [x for x in range(len(self.my_shape))]
                  necessary_change.extend([-x for x in reversed(range(1, len(self.my_shape)+1))])
                  for change in necessary_change:            
                        for i in my_types:
                              if i != self.orientation:
                                    flag = False
                                    for y in range(len(self.shapes[self.current_shape][i])):
                                          for x in range(len(self.shapes[self.current_shape][i][y])):
                                                if y+self.coordinates[0] >= PLAY_HEIGHT_BLOCKS or x+self.coordinates[1]+change < 0 or x+self.coordinates[1]+change >= PLAY_WIDTH_BLOCKS:
                                                      flag = True
                                                elif self.grid[y+self.coordinates[0]][x+self.coordinates[1]+change] != ".":
                                                      flag = True
                                                if flag == True:
                                                      break
                                          if flag == True:
                                                break
                                    if flag == False:
                                          self.orientation = i
                                          self.coordinates[1] += change
                                          return None

      def draw_small_grid(self):
            size = 6
            font = pygame.font.Font('freesansbold.ttf', 32)
            new_text = font.render('Next block', True, WHITE, BLACK)
            new_textRect = new_text.get_rect()
            new_textRect.center = (TOP_LEFT_X+(PLAY_WIDTH_BLOCKS+6)*BLOCK_SIZE, TOP_LEFT_Y+BLOCK_SIZE*3)
            self.surface.blit(new_text, new_textRect)
            #self.draw_small_grid = [["." for _ in range(size)] for i in range(size)]
            for y in range(size): #(PLAY_HEIGHT_BLOCKS):
                  # print(y, TOP_LEFT_Y+y*BLOCK_SIZE) 
                  for x in range(size):
                        # print(TOP_LEFT_X+x*BLOCK_SIZE, y)
                        rect = pygame.Rect(TOP_LEFT_X+(PLAY_WIDTH_BLOCKS+x+3)*BLOCK_SIZE, TOP_LEFT_Y+(y+5)*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                        if x>0 and y>0:
                              if y-1 < len(self.shapes[self.next_shape[0]][self.next_shape[1]]):
                                    if x-1 < len(self.shapes[self.next_shape[0]][self.next_shape[1]][y-1]):
                                          print("here tooo")
                                          if self.shapes[self.next_shape[0]][self.next_shape[1]][y-1][x-1] != ".": 
                                                color = self.shape_colors[self.next_shape[0]]
                                                pygame.draw.rect(self.surface, color, rect, 0) 
                                                continue
                        pygame.draw.rect(self.surface, (255, 0, 0), rect, 1)

      def run(self):
            running = True
            while running:
                  self.surface.fill(BLACK)
                  self.surface.blit(self.text, self.textRect)
                  for event in pygame.event.get():
                        if event.type == QUIT:
                              running = False
                        if event.type == KEYDOWN:
                              if event.key == K_LEFT:
                                    self.move_shape_left()
                              if event.key == K_RIGHT:
                                    self.move_shape_right()
                              if event.key == K_UP:
                                    self.rotate_shape()
                              if event.key == K_DOWN:
                                    self.faster_time = 0.05
                        if event.type == KEYUP:
                              if event.key == K_DOWN:
                                    self.faster_time = self.time
                  if self.current_shape == None:
                        self.get_shape()
                        self.coordinates = [0, PLAY_WIDTH_BLOCKS // 2]
                  self.draw_grid()
                  self.draw_small_grid()
                  self.check_full_lines()
                  self.display_score()
                  if self.the_end:
                        self.game_over()
                  #self.update_active_grid()
                  pygame.display.update()
                  self.coordinates[0] += 1
                  # print(self.coordinates)
                  time.sleep(self.faster_time)
                  #self.faster_time = self.time



if __name__ == "__main__":
    game = Game()
    game.run()
