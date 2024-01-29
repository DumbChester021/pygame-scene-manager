# main.py

import pygame
from sceneManager import SceneManager
from mainMenuScene import MainMenuScene

pygame.init()

screen = pygame.display.set_mode((800, 600))  # Adjust the resolution as needed

scene_manager = SceneManager(MainMenuScene, screen)

while True:
    scene_manager.run_current_scene()
    pygame.display.flip()