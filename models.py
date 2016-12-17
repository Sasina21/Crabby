import arcade.key
class Basket:

	DIR_UP = 0
	DIR_DOWN = 1
	DIR_LEFT = 2
	DIR_RIGHT = 3

	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y
		self.direction = Basket.DIR_UP


	def animate(self, delta):
		if self.direction == Basket.DIR_UP:
			if self.y > self.world.height:
				self.y = 0
			self.y += 5
		if self.direction == Basket.DIR_DOWN:
			if self.y < 0:
				self.y = 600
			self.y += -5
			
		if self.direction == Basket.DIR_LEFT:
			if self.x < 0:
				self.x = 600
			self.x += -5
			
		if self.direction == Basket.DIR_RIGHT:
			if self.x > self.world.width:
				self.x = 0
			self.x += 5
			
class World:
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
 
		self.basket = Basket(self, 100, 100)
 
 
	def animate(self, delta):
		self.basket.animate(delta) 

	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.LEFT :
			self.basket.direction = Basket.DIR_LEFT
		if key == arcade.key.RIGHT:
			self.basket.direction = Basket.DIR_RIGHT
		if key == arcade.key.UP:
			self.basket.direction = Basket.DIR_UP
		if key == arcade.key.DOWN:
			self.basket.direction = Basket.DIR_DOWN
			
