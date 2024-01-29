# SceneManager.py

import pygame
import sys

class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene_name, scene):
        self.scenes[scene_name] = scene

    def switch_scene(self, scene_name):
        if self.current_scene:
            self.current_scene.cleanup()

        self.current_scene = self.scenes.get(scene_name)

        if self.current_scene:
            self.current_scene.setup()

    def run_current_scene(self):
        if self.current_scene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.current_scene.handle_event(event)

            self.current_scene.update()
            self.current_scene.render()
