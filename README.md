# 🐍 Snake Game

```
    ╔══════════════════════════════════════╗
    ║              SNAKE GAME              ║
    ║                                      ║
    ║    ████  ███   █   █  █  █ ████      ║
    ║    █     █  █  █   █  █ █  █         ║
    ║    ███   █  █  █████  ██   ███       ║
    ║       █  █  █  █   █  █ █  █         ║
    ║    ████  ███   █   █  █  █ ████      ║
    ║                                      ║
    ║        Classic Arcade Experience     ║
    ╚══════════════════════════════════════╝
```

## 🎯 Game Features

### 🚀 **Core Gameplay**
- **Classic Snake Mechanics**: Control a growing snake that gets longer with each food item consumed
- **Collision Detection**: Game ends when hitting walls or the snake's own body
- **Score System**: Earn 10 points for each food item eaten
- **Real-time Length Tracking**: Monitor your snake's growth

### ⚡ **Speed Options**
Navigate through three difficulty levels:
- **🐌 Slow Mode**: Perfect for beginners (200ms delay)
- **🏃 Medium Mode**: Balanced gameplay (120ms delay) 
- **⚡ Fast Mode**: Challenge for experts (80ms delay)

### 🎮 **Enhanced Controls**
- **Menu Navigation**: Use ↑↓ arrow keys to select speed
- **Intuitive Selection**: Visual highlighting with arrow indicators
- **Game Controls**: Arrow keys for directional movement
- **Quick Actions**: Enter/Space to select, ESC for menu/quit

### 🎨 **Visual Design**
- **High-Quality Graphics**: Detailed snake with animated eyes
- **Food Animation**: Shimmering food items with shine effects
- **Grid System**: Subtle grid overlay for better navigation
- **Color-Coded Interface**: Different colors for menu states and game elements

### 🏆 **Game States**
1. **Main Menu**: Speed selection with visual feedback
2. **Active Gameplay**: Real-time action with HUD display
3. **Game Over Screen**: Final statistics and restart options

## 🛠️ Technical Requirements

### Prerequisites
- **Python 3.7+** (Tested on Python 3.13.0)
- **Pygame Library** (Automatically installable)

### Installation
```bash
# Install pygame if not already installed
pip install pygame
```

## 🚀 How to Play

### Starting the Game
```bash
# Navigate to the game directory
cd "C:\Users\Lenovo\Documents\all_projects\Python Project\snake game"

# Run the game
python index.py
```

### Game Controls

#### **Main Menu**
- **↑/↓ Arrow Keys**: Navigate speed options
- **Enter/Space**: Select speed and start game
- **ESC**: Exit game

#### **During Gameplay**
- **↑ Arrow**: Move snake up
- **↓ Arrow**: Move snake down  
- **← Arrow**: Move snake left
- **→ Arrow**: Move snake right
- **ESC**: Return to main menu

#### **Game Over Screen**
- **Space/Enter**: Play again with same speed
- **ESC**: Return to main menu

## 🎯 Gameplay Tips

1. **Start Slow**: Begin with slow mode to learn the mechanics
2. **Plan Ahead**: Think about your snake's path before moving
3. **Use Corners**: Utilize screen corners strategically
4. **Stay Calm**: Don't panic when the snake gets longer
5. **Practice**: Each speed mode offers unique challenges

## 🏗️ Project Structure

```
snake game/
├── index.py          # Main game file
├── README.md         # This documentation
└── (future files)    # Potential assets or configs
```

## 🎮 Game Architecture

- **Object-Oriented Design**: Clean, modular code structure
- **State Management**: Proper game state handling (menu/playing/game_over)
- **Event-Driven**: Responsive input handling
- **60 FPS Rendering**: Smooth animation and gameplay

## 🔧 Customization Options

The game is designed to be easily customizable:
- **Window Size**: Modify `WINDOW_WIDTH` and `WINDOW_HEIGHT`
- **Grid Size**: Adjust `GRID_SIZE` for different snake/food sizes
- **Colors**: Change color schemes in the color constants
- **Speed Settings**: Modify `SPEED_SETTINGS` dictionary

## 🐛 Troubleshooting

### Common Issues
- **Import Error**: Ensure pygame is installed (`pip install pygame`)
- **Window Not Appearing**: Check display drivers and pygame installation
- **Slow Performance**: Close other applications for better performance

## 🎊 Future Enhancements

Potential features for future versions:
- High score persistence
- Sound effects and background music
- Multiple themes/skins
- Power-ups and special items
- Multiplayer mode
- Different game modes (timed, survival, etc.)

---

**Enjoy the classic Snake experience! 🐍**

*Built with Python & Pygame | Classic Arcade Gaming*
