import arcade
from models import Basket, World

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
	def __init__(self, *args, **kwargs):
		self.model = kwargs.pop('model', None)
 
		super().__init__(*args, **kwargs)
 
	def sync_with_model(self):
		if self.model:
			self.set_position(self.model.x, self.model.y)
			self.angle = self.model.angle
 
	def draw(self):
		self.sync_with_model()
		super().draw()
 
class CrabbyGameWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
 
		arcade.set_background_color(arcade.color.BISQUE)
		self.basket_sprite = arcade.Sprite('images/basket.png')
		self.world = World(width, height)
		self.basket_sprite = ModelSprite('images/basket.png',model=self.world.basket)
		

		self.monster_sprites = []
		for monster in self.world.monsters:
			self.monster_sprites.append(ModelSprite('images/monster.png',model=monster))

		self.crab_sprites = []
		for crab in self.world.crabs:
			self.crab_sprites.append(ModelSprite('images/crab2.png',model=crab))
	
	def draw_game_over(self):
        
        	arcade.draw_text("Game Over", 90, 295, arcade.color.BRICK_RED, 54)
		

	def on_draw(self):
		if (self.world.time < 0) :

			self.draw_game_over()

		else:
			arcade.start_render()
		
			self.basket_sprite.draw()

			for sprite in self.monster_sprites:
				sprite.draw()

			for sprite in self.crab_sprites:
				sprite.draw()

			arcade.draw_text(str(self.world.score),self.width - 60, self.height - 30,arcade.color.BURNT_SIENNA, 20)

			arcade.draw_text(str(self.world.time),self.width - 55, self.height - 70,arcade.color.BRICK_RED, 20)

			
		
	def animate(self, delta):
		self.world.animate(delta)

	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)

 
if __name__ == '__main__':
	window = CrabbyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()
