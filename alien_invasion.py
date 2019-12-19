import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf


def run_game():
	"""Game init and create display obj"""
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Create button "Play"
	play_button = Button(ai_settings, screen, "Play")
	
	# Creating ship
	ship = Ship(ai_settings, screen)

	# Creating an instance to store game statistics.
	stats = GameStats(ai_settings)

	# Creating group for bullets
	bullets = Group()

	# Creating Alien
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# run game
	while True:
		# FPS control
		clock = pygame.time.Clock()
		clock.tick(ai_settings.fps)
		# Mouse and keyboard detect
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
