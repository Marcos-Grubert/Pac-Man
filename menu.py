import pygame
import constant
import sprite
import os


class Menu:
    def __init__(self):
        #Criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.display = pygame.display.set_mode((constant.DISPLAY_WIDTH, constant.DISPLAY_HEIGHT))
        #Titulo para a tela
        pygame.display.set_caption(constant.GAME_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.match_font(constant.FONT)
        self.load_files()

    def new_game(self):
        #instance all class of the game
        self.all_sprites = pygame.sprite.Group()
        self.run()

    def run(self):
        #game loop
        self.gaming = True
        while self.gaming:
            self.clock.tick(constant.FPS)
            self.events()
            #funcao responsável pela colisão e movimento dos sprites
            self.update_sprites()
            #funcão responsável por desenhar os sprites
            self.draw_sprites()

    def events(self):
        #define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.gaming:
                    # quebra o while jogando
                    self.gaming = False
                self.running = False

    def update_sprites(self):
        #atualizar sprites
        self.all_sprites.update()

    def load_files(self):
        #Carrega arquivos de audio e imagens utilizando a biblioteca OS
        images_directory = os.path.join(os.getcwd(), 'assets', 'images')
        #print(images_directory)
        self.sounds_directory = os.path.join(os.getcwd(), 'assets', 'sounds')
        #print(sounds_directory)
        self.spritesheet = os.path.join(images_directory,constant.SPRITESHEET)
        self.menu_logo = os.path.join(images_directory,constant.LOGO)
        self.menu_logo = pygame.image.load(self.menu_logo).convert()

    def show_text(self, text, fontsize, color, position_x, position_y):
        #Exibe texto no menu do jogo
        font = pygame.font.Font(self.font, fontsize)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.midtop = (position_x, position_y)
        self.display.blit(text, text_rect)

    def show_menu_logo(self, position_x, position_y):
        start_logo_rect = self.menu_logo.get_rect()
        start_logo_rect.midtop = (position_x, position_y)
        self.display.blit(self.menu_logo, start_logo_rect)

    def draw_sprites(self):
        #desenhar sprites
        self.display.fill(constant.BLACK) #limpando a tela
        self.all_sprites.draw(self.display) #desenhando as sprites
        pygame.display.flip()

    def show_start_screen(self):
        self.show_menu_logo(constant.DISPLAY_WIDTH/2, 20)
        pygame.mixer.music.load(os.path.join(self.sounds_directory, constant.MENU_MUSIC))
        pygame.mixer.music.play()
        self.show_text('Pressione uma tecla para jogar', 32, constant.YELLOW,constant.DISPLAY_WIDTH / 2, 320)
        self.show_text('Desenvolvido por Marcos Grubert', 19, constant.WHITE, constant.DISPLAY_WIDTH / 2, 570)
        pygame.display.flip()
        self.waiting_player()

    def waiting_player(self):
        waiting = True
        while waiting:
            self.clock.tick(constant.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.sounds_directory, constant.MENU_START)).play()

    def show_end_screen(self):
        pass



