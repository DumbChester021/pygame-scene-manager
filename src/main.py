# main.py

import pygame
from sceneManager import SceneManager
from mainMenuScene import MainMenuScene
from settingsScene import SettingsScene
from newGameScene import NewGameScene

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Instantiate SceneManager
scene_manager = SceneManager(screen)

# Add scenes to the SceneManager
main_menu_scene = MainMenuScene(screen, scene_manager)
scene_manager.add_scene("MainMenuScene", main_menu_scene)

settings_scene = SettingsScene(screen, scene_manager)
scene_manager.add_scene("SettingsScene", settings_scene)

new_game_scene = NewGameScene(screen, scene_manager)
scene_manager.add_scene("NewGameScene", new_game_scene)

# Set the initial scene
scene_manager.switch_scene("MainMenuScene")

while True:
    scene_manager.run_current_scene()
    pygame.display.flip()