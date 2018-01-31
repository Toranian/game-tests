# game-tests

class Player:

    def __init__(self, size, colour, speed):
        self.size = size
        self.colour = colour
        self.loc_x = (WIDTH / 2) - size
        self.loc_y = (HEIGHT / 2) - size
        self.dir_x = 0
        self.dir_y = 0
        self.speed = speed

    def update(self):

        for event in pygame.event.get():

            if event == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.dir_y = -self.speed

                if event.key == pygame.K_s:
                    self.dir_y = self.speed

                if event.key == pygame.K_a:
                    self.dir_x = -self.speed

                if event.key == pygame.K_d:
                    self.dir_x = self.speed

            self.loc_x += self.dir_x
            self.loc_y += self.dir_y
            pygame.draw.rect(GAME_DISPLAY, self.colour, [self.loc_x, self.loc_y, self.size, self.size])
            print("updated")
