import pygame
import random

pygame.init()


class Projectile1(pygame.sprite.Sprite):

    def __init__(self, Player1):
        super().__init__()
        self.Player1 = Player1
        self.game = game
        self.velocity = 5
        self.image = pygame.image.load('tir.png')
        self.image = pygame.transform.scale(self.image, (50, 130))
        self.rect = self.image.get_rect()
        self.rect.x = Player1.rect.x + 140
        self.rect.y = Player1.rect.y - 30

    def remove(self):
        self.Player1.all_projectile1.remove(self)

    def move(self):
        if self.game.cheeck_collision(self, self.game.all_players2):
            if self.game.player2.health <= 0:
                self.game.is_playing = 5
                self.game.pointage_un += 1
                self.game.game_over2()
            else:
                self.game.player2.damage(2)
                self.remove()
        else:
            self.rect.x += self.velocity


class Projectile2(pygame.sprite.Sprite):

    def __init__(self, Player2):
        super().__init__()
        self.Player2 = Player2
        self.game = game
        self.velocity = 5
        self.image = pygame.image.load('tir.png')
        self.image = pygame.transform.scale(self.image, (50, 130))
        self.rect = self.image.get_rect()
        self.rect.x = Player2.rect.x - 25
        self.rect.y = Player2.rect.y - 30

    def remove(self):
        self.Player2.all_projectile2.remove(self)

    def move2(self):
        if self.game.cheeck_collision(self, self.game.all_players1):
            if self.game.player1.health <= 0:
                self.game.pointage_deux += 1
                self.game.is_playing = 5
                self.game.game_over2()
            else:
                self.game.player1.damage(2)
                self.remove()
        else:
            self.rect.x -= self.velocity


class Player1(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('Player 2.PNG')
        self.image = pygame.transform.scale(self.image, (186, 270))
        self.rect = self.image.get_rect()
        self.rect.y = 345
        self.health = 150
        self.max_health = 150
        self.all_projectile1 = pygame.sprite.Group()
        self.power_launch = False

    def launch_projectile1(self):
        if self.power_launch == True:
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.all_projectile1.add(Projectile1(self))
            self.power_launch = False
        else:
            self.all_projectile1.add(Projectile1(self))

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y, self.health, 10])

    def left(self):
        if not self.rect.x == 0:
            self.rect.x -= 2

    def right(self):
        if not self.game.cheeck_collision(self, self.game.all_players2):
            self.rect.x += 2

    def damage(self, amount):
        self.health -= amount
        if self.health == 74:
            self.power_launch = True


class Player2(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('Player 1.PNG')
        self.image = pygame.transform.scale(self.image, (186, 270))
        self.rect = self.image.get_rect()
        self.rect.y = 345
        self.rect.x = 870
        self.health = 150
        self.max_health = 150
        self.all_projectile2 = pygame.sprite.Group()
        self.power_launch = False

    def launch_projectile2(self):
        if self.power_launch == True:
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.all_projectile2.add(Projectile2(self))
            self.power_launch = False
        else:
            self.all_projectile2.add(Projectile2(self))

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 45, self.rect.y, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 45, self.rect.y, self.health, 10])

    def left(self):
        if not self.game.cheeck_collision(self, self.game.all_players1):
            self.rect.x -= 2

    def right(self):
        if not self.rect.x == 930:
            self.rect.x += 2

    def damage(self, amount):
        self.health -= amount
        if self.health == 74:
            self.power_launch = True


class game:

    def __init__(self):
        self.player1 = Player1(self)
        self.player2 = Player2(self)
        self.round = 1
        self.is_playing = 1
        self.pointage_un = 0
        self.pointage_deux = 0
        self.all_players1 = pygame.sprite.Group()
        self.all_players2 = pygame.sprite.Group()
        self.all_players1.add(self.player1)
        self.all_players2.add(self.player2)
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_laser = pygame.sprite.Group()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.score = 0
        self.best_score = 0
        self.laser_evites = 0
        self.power = 1
        self.bar_power = bar_power(self)
        self.percent_speed = 5
        self.percent = 0
        self.in_usage = False
        self.mod = False
        self.comet = comet(self)
        self.all_comet = pygame.sprite.Group()
        self.spawn_comet()
        self.spawn_comet()
        self.spawn_comet()
        self.spawn_comet()
        self.spawn_comet()
        self.Laser = Laser(self)
        self.use = False


    def power_1(self):
        self.all_laser = pygame.sprite.Group()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.bar_power.percent = 0

    def power_2(self):
        self.player.health = 150
        self.score += 2000
        self.bar_power.percent = 0

    def power_3(self):
        self.bar_power.percent = 0
        self.in_usage = True

    def power_4(self):
        self.bar_power.percent = 0
        self.use = True
        self.score += 3000

    def game_over(self):
        self.bar_power.reset_percent()
        self.all_laser = pygame.sprite.Group()
        self.player.rect.x = 0
        self.player.rect.y = 400
        self.player.health = self.player.max_health
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()
        self.spawn_laser()

    def game_over2(self):
        self.mod = False
        self.player1.rect.x = 0
        self.player2.rect.x = 870
        self.player2.health = self.player2.max_health
        self.player1.health = self.player1.max_health
        self.player1.all_projectile1 = pygame.sprite.Group()
        self.player2.all_projectile2 = pygame.sprite.Group()
        self.all_comet = pygame.sprite.Group()
        self.spawn_comet()
        self.spawn_comet()
        self.spawn_comet()
        self.spawn_comet()
        self.spawn_comet()
        self.player1.power_launch = False
        self.player2.power_launch = False

    def start2(self):
        self.mod = True

    def start(self):
        self.power = 1
        self.score = 0
        self.laser_evites = 0

    def update(self, screen):

        if self.mod == False:
            self.font1 = pygame.font.SysFont("monospace", 30)
            self.score_text = font.render(f"Score: {self.score}", 1, (0, 0, 0))
            screen.blit(self.player.image, self.player.rect)

            screen.blit(self.score_text, (50, 50))

            self.player.update_health_bar(screen)
            self.bar_power.update_bar(screen)

            if self.bar_power.is_full_loaded():
                self.in_usage = False

            if self.bar_power.is_full_loaded():
                self.use = False

            for laser in self.all_laser:
                laser.move()

            self.all_laser.draw(screen)

            if self.pressed.get(pygame.K_UP):
                self.player.fly_up()

            if self.pressed.get(pygame.K_DOWN):
                self.player.fly_down()
            if self.pressed.get(pygame.K_LEFT):
                self.player.left()
            if self.pressed.get(pygame.K_RIGHT):
                self.player.right()

        elif self.mod == True:
            self.font2 = pygame.font.SysFont("Cartoon", 80)
            self.score1 = font2.render(f"Score P1: {self.pointage_un}", 1, (0, 0, 0))
            self.score2 = font2.render(f"Score P2: {self.pointage_deux}", 1, (0, 0, 0))
            screen.blit(self.player1.image, self.player1.rect)
            screen.blit(self.player2.image, self.player2.rect)
            self.power_launch_text1 = font2.render(f"P1 unlock the super laser", 1, (0, 0, 0))
            self.power_launch_text2 = font2.render(f"P2 unlock the super laser", 1, (0, 0, 0))
            self.player1.update_health_bar(screen)
            self.player2.update_health_bar(screen)
            self.player1.all_projectile1.draw(screen)
            self.player2.all_projectile2.draw(screen)
            self.all_comet.draw(screen)
            screen.blit(self.score1, (0, 0))
            screen.blit(self.score2, (800, 0))

            if self.player1.power_launch == True:
                screen.blit(self.power_launch_text1, (0, 550))
            if self.player2.power_launch == True:
                screen.blit(self.power_launch_text2, (700, 550))

            for Projectile1 in self.player1.all_projectile1:
                Projectile1.move()

            for Projectile2 in self.player2.all_projectile2:
                Projectile2.move2()

            for comet in self.all_comet:
                comet.move()


            if self.pressed.get(pygame.K_LEFT):
                self.player2.left()
            if self.pressed.get(pygame.K_RIGHT):
                self.player2.right()
            if self.pressed.get(pygame.K_a):
                self.player1.left()
            if self.pressed.get(pygame.K_d):
                self.player1.right()



    def cheeck_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_laser(self):
        laser = Laser(self)
        self.all_laser.add(laser)

    def spawn_comet(self):
        Comet = comet(self)
        self.all_comet.add(Comet)


class bar_power:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 3
        self.game = game

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface):
        if not self.is_full_loaded():
            self.add_percent()

        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 570,
            surface.get_width(),
            10
        ])

        pygame.draw.rect(surface, (255, 0, 0), [
            0,
            surface.get_height() - 570,
            (surface.get_width() / 100) * self.percent,
            10
        ])


class comet(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 2
        self.image = pygame.image.load('ball.PNG')
        self.image = pygame.transform.scale(self.image, (112, 112))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = - random.randint(20, 350)

    def remove(self):
        self.rect.x = random.randint(0, 1000)
        self.rect.y = - random.randint(20, 350)


    def move(self):
        self.rect.y += self.velocity
        if self.game.cheeck_collision(self, self.game.all_players2):
            self.remove()
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            self.game.player2.damage(2)
            if self.game.player2.health <= 0:
                self.game.pointage_un += 1
                self.game.is_playing = 5
                self.game.game_over2()
        elif self.game.cheeck_collision(self, self.game.all_players1):
            self.remove()
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            self.game.player1.damage(2)
            if self.game.player1.health <= 0:
                self.game.pointage_deux += 1
                self.game.is_playing = 5
                self.game.game_over2()
        elif self.rect.y > 600:
            self.image = pygame.image.load('ball.PNG')
            self.image = pygame.transform.scale(self.image, (112, 112))
            self.remove()
        elif self.rect.y > 500:
            self.image = pygame.image.load('explosion.PNG')
        elif self.rect.y > -100:
            self.image = pygame.image.load('ball.PNG')
            self.image = pygame.transform.scale(self.image, (112, 112))


class Laser(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 2
        self.image = pygame.image.load('tir.png')
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1100, 1200)
        self.rect.y = random.randint(0, 430)

    def removing(self):
        self.rect.x = random.randint(1100, 1200)
        self.rect.y = random.randint(0, 430)

    def move(self):
        if not self.game.cheeck_collision(self, self.game.all_players):
            if self.rect.x <= 0:
                self.game.laser_evites += 1
                self.game.score += 73
                self.rect.x = random.randint(1080, 1500)
                self.rect.y = random.randint(-20, 455)

            else:
                if self.game.use == False:
                    self.rect.x -= self.velocity
        else:
            self.removing()
            if self.game.in_usage == False:
                self.game.player.damage(50)
                self.game.score -= 24
                if self.game.player.health == 0:
                    if self.game.score >= self.game.best_score:
                        self.game.best_score = self.game.score
                    self.game.is_playing = 3
                    self.game.game_over()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (240, 168))
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.game = game
        self.health = 150
        self.max_health = 150

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 45, self.rect.y, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 45, self.rect.y, self.health, 10])

    def fly_up(self):
        if self.rect.y >= -20:
            self.rect.y -= 2

    def fly_down(self):
        if self.rect.y <= 455:
            self.rect.y += 2

    def left(self):
        if self.rect.x >= 0:
            self.rect.x -= 2

    def right(self):
        if self.rect.x <= 870:
            self.rect.x += 2

    def damage(self, amount):
        self.health -= amount


game = game()
pygame.display.set_caption("dont die")
screen = pygame.display.set_mode((1080, 600))
bg = pygame.image.load('desertbg.jpg')
bg = pygame.transform.scale(bg, (1080, 600))
font = pygame.font.SysFont("monospace", 30)
font2 = pygame.font.SysFont("Cartoon", 50)
start_screen = font2.render(f"press <space> to start the game", 1, (0, 0, 0))
fond_fin = pygame.image.load('fond.PNG')
fond_fin = pygame.transform.scale(fond_fin, (1080, 600))
banner = pygame.image.load('banner2.PNG')
banner = pygame.transform.scale(banner, (420, 420))


running = True

while running:
    laser_esquive = font2.render(f"Lasers dodged: {game.laser_evites}", 1, (0, 0, 0))
    score_text = font2.render(f"Score: {game.score}", 1, (0, 0, 0))
    best_scores = font2.render(f"best score: {game.best_score}", 1, (0, 0, 0))
    un = font2.render(f"power n°{game.power}", 1, (0, 0, 0))
    p1 = font2.render(f"Player 1 got: {game.pointage_un}", 1, (0, 0, 0))
    p2 = font2.render(f"Player 2 got: {game.pointage_deux}", 1, (0, 0, 0))
    press_start = font2.render(f"Press SPACE to go on the home screen", 1, (0, 0, 0))
    press_start2 = font2.render(f"Press SPACE to go on the home screen", 1, (255, 255, 255))

    screen.blit(bg, (0, 0))

    if game.is_playing == 1:
        screen.blit(banner, (320, 50))
        screen.blit(start_screen, (50, 50))
    elif game.is_playing == 2:
        game.update(screen)
        screen.blit(un, (350, 50))
    elif game.is_playing == 3:
        screen.blit(fond_fin, (0, 0))
        screen.blit(score_text, (430, 400))
        screen.blit(best_scores, (430, 300))
        screen.blit(laser_esquive, (430, 500))
        screen.blit(press_start2, (230, 550))
    elif game.is_playing == 4:
        game.update(screen)
    elif game.is_playing == 5:
        screen.blit(fond_fin, (0, 0))
        screen.blit(p1, (430, 400))
        screen.blit(p2, (430, 300))
        screen.blit(press_start, (230, 500))


    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("la fenêtre s'est fermée")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE and game.is_playing == 1:
                game.is_playing = 2
                game.start()
            elif event.key == pygame.K_SPACE and game.is_playing == 3:
                game.is_playing = 1
            elif event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                print("la fenêtre s'est fermée")
            elif event.key == pygame.K_z and game.is_playing == 2:
                game.power = 1
            elif event.key == pygame.K_x and game.is_playing == 2:
                game.power = 2
            elif event.key == pygame.K_c and game.is_playing == 2:
                game.power = 3
            elif event.key == pygame.K_v and game.is_playing == 2:
                game.power = 4
            elif event.key == pygame.K_SPACE and game.is_playing == 2:
                if game.bar_power.is_full_loaded():
                    if game.power == 1:
                        game.power_1()
                    elif game.power == 2:
                        game.power_2()
                    elif game.power == 3:
                        game.power_3()
                    elif game.power == 4:
                        game.power_4()
            elif event.key == pygame.K_BACKSPACE and game.is_playing == 1 and game.mod == False:
                game.start2()
                game.is_playing = 4
            if event.key == pygame.K_BACKSPACE and game.is_playing == 4 and game.mod == True:
                game.player2.launch_projectile2()
            if event.key == pygame.K_SPACE and game.is_playing == 4 and game.mod == True:
                game.player1.launch_projectile1()
            elif event.key == pygame.K_1 and game.is_playing == 4 and game.mod == True:
                game.is_playing = 1
                game.game_over2()
            elif event.key == pygame.K_r and game.is_playing == 1 and game.mod == False:
                game.pointage_un = 0
                game.pointage_deux = 0
            elif event.key == pygame.K_SPACE and game.is_playing == 5:
                game.is_playing = 1
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
