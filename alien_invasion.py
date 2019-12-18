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

	# Create Alien
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# run game
	while True:
		# FPS control
		clock = pygame.time.Clock()
		clock.tick(ai_settings.fps)
		# Mouse and keyboard detect
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
