import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	"""Game init and create display obj"""
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Create ship
	ship = Ship(ai_settings, screen)
	# Create group for bullets
	bullets = Group()
	
	# run game
	while True:
		# Mouse and keyboard detect
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()

		# Delete bullets
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)

		gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
