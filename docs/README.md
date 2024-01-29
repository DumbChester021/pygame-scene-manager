
---

# Pygame Scene Manager

![Pygame Scene Manager Logo](../assets/logo.png)

A flexible and efficient scene manager for Pygame, allowing easy organization and switching between different scenes in your game.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Creating New Scenes](#creating-new-scenes)
    - [Switching Scenes](#switching-scenes)
- [Scenes](#scenes)
  - [Main Menu Scene](#main-menu-scene)
  - [Settings Scene](#settings-scene)
- [Optimizations](#optimizations)
- [Production QA](#production-qa)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Pygame Scene Manager is designed to simplify the management of different scenes within a Pygame-based game or application. It allows you to seamlessly switch between scenes, handle events, and maintain clean code organization.

## Features

- Scene switching with cleanup for efficient resource management.
- Conditional rendering to optimize performance by rendering only active scenes.
- Proper event handling, ensuring that only the active scene processes events.
- Consistent coding style and clear documentation for ease of use and maintenance.
- Basic scenes included (Main Menu and Settings), with the ability to expand for custom scenes.

## Getting Started

### Installation

To use the Pygame Scene Manager, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/pygame-scene-manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pygame-scene-manager
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Import the `SceneManager` and your desired scenes:

   ```python
   from sceneManager import SceneManager
   from mainMenuScene import MainMenuScene
   from settingsScene import SettingsScene
   ```

2. Initialize Pygame and create a Pygame display:

   ```python
   import pygame

   pygame.init()

   screen = pygame.display.set_mode((800, 600))
   ```

3. Create an instance of the `SceneManager`:

   ```python
   scene_manager = SceneManager(MainMenuScene, screen)
   ```

4. Add the scenes to the `SceneManager` :
   ```python
   main_menu_scene = MainMenuScene(screen, scene_manager)
   scene_manager.add_scene("MainMenuScene", main_menu_scene)

   settings_scene = SettingsScene(screen, scene_manager)
   scene_manager.add_scene("SettingsScene", settings_scene)

   new_game_scene = NewGameScene(screen, scene_manager)
   scene_manager.add_scene("NewGameScene", new_game_scene)
   
   ```

5. Set the initial scene and Run the game loop with the `run_current_scene` method:

   ```python
   #Set the Initial Scene
   scene_manager.switch_scene("MainMenuScene")

   while True:
       scene_manager.run_current_scene()
       pygame.display.flip()
   ```

#### Creating New Scenes

You can create custom scenes by following these steps:

1. **Create a New Scene Class:**
   - Create a new Python file for your scene, e.g., `customScene.py`.
   - Define a class for your scene, inheriting from the base `Scene` class in `scene.py`.
   - Implement the necessary methods (`setup`, `update`, `render`, `handle_event`) in your scene class.

   Example:
   ```python
   # customScene.py

   import pygame
   from scene import Scene

   class CustomScene(Scene):
       def setup(self):
           # Initialize any scene-specific variables or resources here
           pass

       def update(self):
           # Update logic for your scene
           pass

       def render(self):
           # Render objects for your scene
           pass

       def handle_event(self, event):
           # Handle events for your scene
           pass
   ```

2. **Import and Use the New Scene:**
   - Import the new scene in your main script.
   - Add the custom scene to scenemanager at main.

   Example:
   ```python
   from sceneManager import SceneManager
   from customScene import CustomScene

   custom_scene = CustomScene(screen, scene_manager)
   ```

#### Switching Scenes

You can switch between scenes in your game:

- Call the `switch_scene` method on the `SceneManager` instance.
- Pass the name of the scene you want to switch to (needs to match the name you registered it to when adding it in the main.py).

Example:
```python
# Switch to the CustomScene
scene_manager.switch_scene("CustomScene")
```

## Scenes

### Main Menu Scene

The main menu scene provides a basic menu structure with options for continuing the game, starting a new game, accessing settings, and quitting the game.

### Settings Scene

The settings scene allows the user to toggle debug mode on and off, providing essential details for developers, such as FPS and other debugging information.

### New Game Scene

The New Game scene is a blank example of another scene that you can use and copy to create new custom scenes

## Optimizations

The Pygame Scene Manager includes optimizations for:

- Memory Management
- Render Efficiency
- Event Handling
- Adding Custom Scenes
- Switching Scenes
- Code Cleanup and Clarity
- Consistency and Readability

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

