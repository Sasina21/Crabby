import arcade.key
from random import randint, random

class Model:
	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y
		self.angle = 0

	def hit(self, other, hit_size):
		return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

	def random_location(self):
		self.x = randint(0, self.world.width - 1)
		self.y = randint(0, self.world.height - 1)

class Crab(Model):
	def __init__(self, world, x, y, vx, vy):
		super().__init__(world, x, y)
		self.vx = vx
		self.vy = vy
		

	def random_direction(self):
		self.vx = 5 * random()
		self.vy = 5 * random()

	def animate(self, delta):
		if (self.x < 0) or (self.x > self.world.width):
			self.vx = - self.vx
       
		if (self.y < 0) or (self.y > self.world.height):
			self.vy = - self.vy
       
		self.x += self.vx
		self.y += self.vy

class Monster(Model):
	def __init__(self, world, x, y, vx, vy):
		super().__init__(world, x, y)
		self.vx = vx
		self.vy = vy
		

	def random_direction(self):
		self.vx = 7 * random()
		self.vy = 7 * random()

	def animate(self, delta):
		global flip

		if (self.x < 0) or (self.x > self.world.width):
			self.vx = - self.vx
			flip = 1
       
		if (self.y < 0) or (self.y > self.world.height):
			self.vy = - self.vy
			flip = 0

       
		self.x += self.vx
		self.y += self.vy
		

class Basket(Model):

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
		self.angle = 0
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
	NUM_MONSTER = 2
	NUM_CRAB = 5
	
	def __init__(self, width, height):
		self.width = width
		self.height = height
 
		self.basket = Basket(self, 100, 100)

		self.crabs = []
		for i in range(World.NUM_CRAB):
			crab = Crab(self, 0, 0, 0, 0)
			crab.random_direction()
			self.crabs.append(crab)

		self.monsters = []
		for i in range(World.NUM_MONSTER):
			monster = Monster(self, 0, 0, 0, 0)
			monster.random_direction()
			self.monsters.append(monster)

		self.score = 0
		self.time = 30
 
 
	def animate(self, delta):
		self.basket.animate(delta) 

		self.time -=delta
		
		for monster in self.monsters:
			monster.animate(delta)
			if self.basket.hit(monster, 70):
				self.score -= 3
				monster.x = 0
				monster.y = 0
				monster.random_direction()

		for crab in self.crabs:
			crab.animate(delta)
			if self.basket.hit(crab, 50):
				self.score += 2
				crab.x = 0
				crab.y = 0
				crab.random_direction()

	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.LEFT :
			self.basket.direction = Basket.DIR_LEFT
		if key == arcade.key.RIGHT:
			self.basket.direction = Basket.DIR_RIGHT
		if key == arcade.key.UP:
			self.basket.direction = Basket.DIR_UP
		if key == arcade.key.DOWN:
			self.basket.direction = Basket.DIR_DOWN
			
