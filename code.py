import pygame
from pygame.locals import*
import time
import random
import sys

SIZE = 40

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((700, 520))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            sound=pygame.mixer.Sound(r"C:\Users\Poojitha Surla\Desktop\Snake_Game\ding.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.apple.move()

        if(self.snake.x[0]<0 or self.snake.x[0]>699  or self.snake.y[0]<0 or self.snake.y[0]>519):
         sound1=pygame.mixer.Sound(r"C:\Users\Poojitha Surla\Desktop\Snake_Game\crash.mp3")
         pygame.mixer.Sound.play(sound1)
         raise "Collision Occured"
            
        for i in range(2, self.snake.length):
            if (self.snake.x[0]>=self.snake.x[i] and self.snake.x[0]<self.snake.x[i]+SIZE):
              if(self.snake.y[0]>=self.snake.y[i] and self.snake.y[0]<self.snake.y[i]+SIZE):
                sound1=pygame.mixer.Sound(r"C:\Users\Poojitha Surla\Desktop\Snake_Game\crash.mp3")
                pygame.mixer.Sound.play(sound1)
                raise "Collision Occured"
            

    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple = Apple(self.surface)
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 == x2 :
            if y1 == y2 :
                return True
        return False
    
    def display_score(self):
        font = pygame.font.SysFont('arial',20)
        score = font.render(f"Score: {self.snake.length}",True,(255, 255, 255))
        self.surface.blit(score,(550,10))

    def show_game_over(self):
        self.surface.fill((110,110,5))
        font = pygame.font.SysFont('arial', 26)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (140, 140))

        pygame.display.flip()

    def run(self):
        running = True
        pause= False

        while running:
            for event in pygame.event.get():
                 if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:

                     if event.key == K_LEFT:
                        self.snake.move_left()

                     if event.key == K_RIGHT:
                        self.snake.move_right()

                     if event.key == K_UP:
                        self.snake.move_up()

                     if event.key == K_DOWN:
                        self.snake.move_down()

                 elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            
            time.sleep(.3)


class Snake:
    def __init__(self, surface,length):
        self.parent_screen = surface
        self.image = pygame.image.load(r"C:\Users\Poojitha Surla\Desktop\Snake_Game\block.jpg").convert()
        self.direction = 'down'
        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self): 
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
    
        self.draw()

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)


    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load(r"C:\Users\Poojitha Surla\Desktop\Snake_Game\apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,10)*SIZE
        self.y = random.randint(0,10)*SIZE

if __name__ == '__main__':
    game = Game()
    game.run()
