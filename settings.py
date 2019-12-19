class Settings:
	"""Class for store settings of the game"""

	def __init__(self):
		"""Init game settings"""
		# Screen settings
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		self.fps = 60
		# Ship settings
		self.ship_speed_factor = 7.5
		self.ship_limit = 3
		# Bullet settings
		self.bullet_speed_factor = 10
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		# Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction = 1 move right, -1 move left
		self.fleet_direction = 1
