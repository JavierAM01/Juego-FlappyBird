import pygame, os




class Bird:
    def __init__(self, enviroment):
        self.gravity = 0.25
        self.movement = 0
        self.score = 0   
        self.images = ImagesBird(enviroment.bird_color)
        self.img = self.images.bird_mid
        self.surface = self.img.get_rect(center = (120, 350))
        self.t = 0



class Images:
    def load_image(self, name, size = False):
        image = pygame.image.load(os.path.join("images", name))
        if size != False: image = pygame.transform.scale(image, size)
        return image


class ImagesBird(Images):

    def __init__(self, color):
        
        size_bird = (45, 38)
        bird_mid_red = self.load_image("redbird-midflap.png", size_bird)#.convert()
        bird_down_red = self.load_image("redbird-downflap.png", size_bird)#.convert()
        bird_up_red = self.load_image("redbird-upflap.png", size_bird)#.convert()
        bird_mid_yellow = self.load_image("yellowbird-midflap.png", size_bird)#.convert()
        bird_down_yellow = self.load_image("yellowbird-downflap.png", size_bird)#.convert()
        bird_up_yellow = self.load_image("yellowbird-upflap.png", size_bird)#.convert()
        bird_mid_blue = self.load_image("bluebird-midflap.png", size_bird)#.convert()
        bird_down_blue = self.load_image("bluebird-downflap.png", size_bird)#.convert()
        bird_up_blue = self.load_image("bluebird-upflap.png", size_bird)#.convert()
        self.birds = dict()
        self.birds["blue"] = [bird_up_blue, bird_mid_blue, bird_down_blue]
        self.birds["red"] = [bird_up_red, bird_mid_red, bird_down_red]
        self.birds["yellow"] = [bird_up_yellow, bird_mid_yellow, bird_down_yellow]
        self.change_color(color)
        
    def change_color(self, color):
        self.bird_up = pygame.transform.rotate(self.birds[color][0], 5)
        self.bird_mid = self.birds[color][1]
        self.bird_down = pygame.transform.rotate(self.birds[color][2], -5)


class ImagesBG(Images):

    def __init__(self, str_bg, window_size):

        # background
        self.bg_day = self.load_image("background-day.png", window_size)#.convert()
        self.bg_night = self.load_image("background-night.png", window_size)#.convert()
        self.bg_window = self.load_image("background-" + str_bg + ".png", window_size)#.convert()
        self.floor = self.load_image("base.png", (400, 110))#.convert()
        self.pipe = self.load_image("pipe-green.png", (70, 400))#.convert()

        # numbers
        self.numbers = {}
        for i in range(10): self.numbers[i] = self.load_image(str(i) + ".png", (40, 50))

        # extra info
        self.mesage = self.load_image("message.png", (300,500))
        self.game_over = self.load_image("gameover.png", (300, 100))

