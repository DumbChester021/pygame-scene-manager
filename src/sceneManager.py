# sceneManager.py

import pygame
import sys

class SceneManager:
    def __init__(self, initial_scene, screen):
        self.current_scene = initial_scene(screen)

    def switch_scene(self, new_scene):
        # Clean up the current scene before switching
        self.current_scene.cleanup()

        # Instantiate the new scene with the screen parameter
        self.current_scene = new_scene(screen)

    def run_current_scene(self):
        # Handle events for the active scene
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.current_scene.handle_event(event)

        # Update and render the active scene
        self.current_scene.update()
        self.current_scene.render()