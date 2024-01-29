# mainMenuScene.py

import pygame
import sys
from settingsScene import SettingsScene

class MainMenuScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # You can adjust the font size

        self.title_text = self.font.render("Game Title", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(screen.get_width() // 2, 100))

        self.menu_options = [
            "Continue",
            "New Game",
            "Settings",
            "Quit"
        ]
        self.selected_option = 0

        # Instantiate settings scene but don't render it initially
        self.settings_scene = SettingsScene(screen)
        self.show_settings = False

    def setup(self):
        pass

    def cleanup(self):
        # Clean up resources when switching away from this scene
        pass

    def update(self):
        if self.show_settings:
            self.settings_scene.update()

    def render(self):
        self.screen.fill((0, 0, 0))  # Set background color

        self.screen.blit(self.title_text, self.title_rect)

        if not self.show_settings:
            for i, option in enumerate(self.menu_options):
                color = (255, 255, 255) if i == self.selected_option else (150, 150, 150)
                text = self.font.render(option, True, color)
                rect = text.get_rect(center=(self.screen.get_width() // 2, 200 + i * 50))
                self.screen.blit(text, rect)
        else:
            self.settings_scene.render()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.menu_options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.menu_options)
            elif event.key == pygame.K_RETURN:
                self.handle_selection()

    def handle_selection(self):
        if not self.show_settings:
            if self.selected_option == 0:
                print("Continue selected")
                # Add continue logic here
            elif self.selected_option == 1:
                print("New Game selected")
                # Add new game logic here
            elif self.selected_option == 2:
                print("Settings selected")
                self.show_settings = True
            elif self.selected_option == 3:
                print("Quit selected")
                pygame.quit()
                sys.exit()
        else:
            self.show_settings = False