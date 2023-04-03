from game import ImagesBG, Bird

import pygame
import random
import time



class Display:

    def __init__(self):
        
        pygame.init()

        self.n_samples = 1

        self.bird_color = "yellow" # blue / red / yellow
        self.birds_sample = [Bird(self) for _ in range(self.n_samples)]
        self.bird = self.birds_sample[0]

        window_size = (400, 700)
        self.window = pygame.display.set_mode(window_size)
    
        self.pipe_list = []
        self.pipe_heights = [250, 350, 450, 550]
        
        type_bg = "day"       # day / night
        self.img = ImagesBG(type_bg, window_size)
        self.floor_rect = pygame.Rect((0, 620, 400, 110)) 
        self.floor_x = 0
    
    @staticmethod
    def quit():
        pygame.quit()

    def create_pipe(self, img_pipe):
        random_height = random.choice(self.pipe_heights)
        top_pipe = img_pipe.get_rect(midtop = (450, random_height))
        bottom_pipe = img_pipe.get_rect(midbottom = (450, random_height - 200))
        return top_pipe, bottom_pipe 

    def move_pipes(self):
        for pipe in self.pipe_list:
            pipe.x -= 2

    def draw_floor(self):
        self.window.blit(self.img.floor, (self.floor_x, 600))
        self.window.blit(self.img.floor, (self.floor_x + 400, 600))

    def draw_bird(self, all=False):
        if all:
            for bird in self.birds_sample:
                self.window.blit(bird.img, bird.surface)
                break
        else:
            self.window.blit(self.bird.img, self.bird.surface)

    def draw_pipes(self):
        for pipe in self.pipe_list:
            if pipe.top <= 0:
                pipe_fliped = pygame.transform.flip(self.img.pipe, False, True)
                self.window.blit(pipe_fliped, pipe)
            else:
                self.window.blit(self.img.pipe, pipe)

    def draw_score(self):
        if self.bird.score - 1 < 10:
            i = self.bird.score
            if self.bird.score == 0: i = 1
            self.window.blit(self.img.numbers[i-1], (200-15, 50))
        elif self.bird.score - 1 < 100:
            number = self.bird.score - 1
            i1 = str(number)[0]
            i2 = str(number)[1]
            self.window.blit(self.img.numbers[int(i1)], (200-33, 50))
            self.window.blit(self.img.numbers[int(i2)], (200+3, 50))
        elif self.bird.score - 1 < 1000:
            number = self.bird.score - 1
            i1 = str(number)[0]
            i2 = str(number)[1]
            i3 = str(number)[2]
            self.window.blit(self.img.numbers[int(i1)], (200-60, 50))
            self.window.blit(self.img.numbers[int(i2)], (200-20, 50))
            self.window.blit(self.img.numbers[int(i3)], (200+20, 50))

    def update(self, die, game_active):
        self.window.blit(self.img.bg_window, (0,0))
        
        if game_active:
            # Bird
            self.bird.movement += self.bird.gravity
            self.bird.surface.y += self.bird.movement 
            if self.bird.movement < 0:
                self.bird.img = self.bird.images.bird_up
            elif self.bird.movement == 0:
                self.bird.img = self.bird.images.bird_mid
            else:
                self.bird.img = self.bird.images.bird_down
            # Pipes
            if not die: 
                self.move_pipes()
            self.draw_pipes()
            # Floor
            self.floor_x -= 1
            if self.floor_x == -400: self.floor_x = 0
        else:
            self.window.blit(self.img.mesage, (50, 50))

        self.draw_bird()
        self.draw_floor()
        if die: 
            self.window.blit(self.img.game_over, (50,270))
        if game_active: self.draw_score()
        pygame.display.update()

    def play(self):
        clock = pygame.time.Clock()
        die = False
        run = True
        game_active = False
        SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(SPAWNPIPE, 1200)

        while run:

            clock.tick(120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                if not game_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key  == pygame.K_SPACE:
                            game_active = True
                elif game_active and not die:
                    if event.type == pygame.KEYDOWN:
                        if event.key  == pygame.K_SPACE:
                            self.bird.movement = 0
                            if self.bird.surface.top > 0: self.bird.movement -= 5 
                    if event.type == SPAWNPIPE:
                        new_pipe = self.create_pipe(self.img.pipe)
                        self.pipe_list.extend(new_pipe)
                        self.bird.score += 1
                elif die:
                    if event.type == pygame.KEYDOWN:
                        if event.key  == pygame.K_SPACE:
                            self.pipe_list.clear()
                            self.bird.surface.center = (120, 350)
                            game_active = False
                            die = False
                            self.bird.gravity = 0.25
                            self.bird.score = 0
                            self.img.bg_window = self.img.bg_day

            # Collides 
            if self.bird.surface.colliderect(self.floor_rect):
                self.bird.movement = 0
                self.bird.gravity = 0
                die = True
            for pipe in self.pipe_list:
                if self.bird.surface.colliderect(pipe):
                    die = True

            # Update frame
            self.update(die, game_active)