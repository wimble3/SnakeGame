import pygame
import random
import sys


class SnakeGame(object):
    def __init__(self):
        self.check_errors = None
        self.game_window = None
        self.fps_controller = None
        self.speed = 8
        self.SQUARE_SIZE = 60
        self.FRAME_SIZE_X = 1380
        self.FRAME_SIZE_Y = 840
        self.direction = "RIGHT"
        self.head_pos = [120, 60]
        self.snake_body = [[120, 60]]
        self.food_pos = [random.randrange(1, (self.FRAME_SIZE_X // self.SQUARE_SIZE)) * self.SQUARE_SIZE,
                         random.randrange(1, (self.FRAME_SIZE_Y // self.SQUARE_SIZE)) * self.SQUARE_SIZE]
        self.food_spawn = True
        self.score = 0
        self.colors = {'black': pygame.Color(0, 0, 0),
                       'white': pygame.Color(255, 255, 255),
                       'red': pygame.Color(255, 10, 10),
                       'green': pygame.Color(10, 255, 10),
                       'blue': pygame.Color(10, 10, 255),
                       }

    def main(self):
        self.check_errors = pygame.init()
        pygame.display.set_caption("Snake")
        self.game_window = pygame.display.set_mode((self.FRAME_SIZE_X, self.FRAME_SIZE_Y))
        self.fps_controller = pygame.time.Clock()
        self.__loop()

    def __loop(self):
        self.__show_score()
        while True:
            self.__check_buttons()
            self.__set_head_pos()
            self.__set_score()

            self.game_window.fill(self.colors['black'])
            for pos in self.snake_body:
                pygame.draw.rect(self.game_window, self.colors['green'], pygame.Rect(
                    pos[0] + 2, pos[1] + 2,
                    self.SQUARE_SIZE - 2, self.SQUARE_SIZE - 2))

            pygame.draw.rect(self.game_window, self.colors['red'], pygame.Rect(self.food_pos[0],
                                                                               self.food_pos[1], self.SQUARE_SIZE,
                                                                               self.SQUARE_SIZE))

            for block in self.snake_body[1:]:
                if self.head_pos[0] == block[0] and self.head_pos[1] == block[1]:
                    a = SnakeGame()
                    a.main()

            self.__show_score()
            pygame.display.update()
            self.fps_controller.tick(self.speed)

    def __set_head_pos(self):
        if self.direction == "UP":
            self.head_pos[1] -= self.SQUARE_SIZE
        elif self.direction == "DOWN":
            self.head_pos[1] += self.SQUARE_SIZE
        elif self.direction == "LEFT":
            self.head_pos[0] -= self.SQUARE_SIZE
        else:
            self.head_pos[0] += self.SQUARE_SIZE
        if self.head_pos[0] < 0:
            self.head_pos[0] = self.FRAME_SIZE_X - self.SQUARE_SIZE
        elif self.head_pos[0] > self.FRAME_SIZE_X - self.SQUARE_SIZE:
            self.head_pos[0] = 0
        elif self.head_pos[1] < 0:
            self.head_pos[1] = self.FRAME_SIZE_Y - self.SQUARE_SIZE
        elif self.head_pos[1] > self.FRAME_SIZE_Y - self.SQUARE_SIZE:
            self.head_pos[1] = 0

    def __set_score(self):
        self.snake_body.insert(0, list(self.head_pos))
        if self.head_pos[0] == self.food_pos[0] and self.head_pos[1] == self.food_pos[1]:
            self.score += 1
            self.food_spawn = False
        else:
            self.snake_body.pop()
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, (self.FRAME_SIZE_X // self.SQUARE_SIZE)) * self.SQUARE_SIZE,
                             random.randrange(1, (self.FRAME_SIZE_Y // self.SQUARE_SIZE)) * self.SQUARE_SIZE]
            self.food_spawn = True

    def __check_buttons(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == ord("w")
                        and self.direction != "DOWN"):
                    self.direction = "UP"
                elif (event.key == pygame.K_DOWN or event.key == ord("s")
                      and self.direction != "UP"):
                    self.direction = "DOWN"
                elif (event.key == pygame.K_LEFT or event.key == ord("a")
                      and self.direction != "RIGHT"):
                    self.direction = "LEFT"
                elif (event.key == pygame.K_RIGHT or event.key == ord("d")
                      and self.direction != "LEFT"):
                    self.direction = "RIGHT"

    def __show_score(self):
        score_font = pygame.font.SysFont('consol', 40)
        score_surface = score_font.render("Score: " + str(self.score), True, self.colors['white'])
        score_rect = score_surface.get_rect()
        score_rect.midtop = (self.FRAME_SIZE_X / 10, 15)
        self.game_window.blit(score_surface, score_rect)


if __name__ == '__main__':
    a = SnakeGame()
    a.main()
