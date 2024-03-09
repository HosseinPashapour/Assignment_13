import random
import arcade

class Fighter(arcade.Sprite):
    def __init__(self, game, name):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")        
        self.center_x = game.width // 2
        self.center_y = 90
        self.width = 70
        self.height = 60
        self.speed = 12

class Enemy(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0, width)
        self.center_y = height + 24
        self.angle = 180
        self.width = 70
        self.height = 60
        self.speed = 2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height= 800, title= "StarWars 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Fighter(self, "Hossein Jet")
        self.them = Enemy(self.width, self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 ,0 ,self.width ,self.height , self.background)
        self.me.draw()
        self.them.draw()

    def on_key_press(self, symbol, modifiers: int):
        print(symbol)
        if symbol == 97 or symbol == 65361:
            self.me.center_x -= self.me.speed
        elif symbol == 100 or symbol == 65363:
            self.me.center_x += self.me.speed
        elif symbol == 119 or symbol == 65362:
            self.me.center_y += self.me.speed
        elif symbol == 115 or symbol == 65364:
            self.me.center_y -= self.me.speed

    def on_update(self, delta_time: float):
        self.them.center_y -= self.them.speed


window = Game()
arcade.run()
