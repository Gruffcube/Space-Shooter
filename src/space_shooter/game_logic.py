from space_shooter.engine import GameLoop, Entity, AssetManager
import space_shooter.entities
import pygame
import random


def run_game_logic():
    pygame.init()
    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    asset_manager = AssetManager()
    
    game = SpaceShooter(screen, asset_manager)
    
    del asset_manager, screen
    
    game.run()


class SpaceShooter(GameLoop):
    def __init__(self, screen, asset_manager, **kwargs):
        super().__init__(screen, asset_manager, **kwargs)
    
    def _update(self):
        pass
