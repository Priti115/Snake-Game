import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Speed settings (milliseconds between moves)
SPEED_SETTINGS = {
    'slow': 200,
    'medium': 120,
    'fast': 80
}

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        self.small_font = pygame.font.Font(None, 24)
        
        self.speed_options = ['slow', 'medium', 'fast']
        self.selected_speed_index = 1  # Start with medium selected
        self.speed = self.speed_options[self.selected_speed_index]
        self.game_state = 'menu'  # 'menu', 'playing', 'game_over'
        self.reset_game()
        
    def reset_game(self):
        # Snake starts in the middle, moving right
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food = self.generate_food()
        self.score = 0
        self.last_move_time = 0
        
    def generate_food(self):
        while True:
            food_x = random.randint(0, GRID_WIDTH - 1)
            food_y = random.randint(0, GRID_HEIGHT - 1)
            if (food_x, food_y) not in self.snake:
                return (food_x, food_y)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if self.game_state == 'menu':
                    if event.key == pygame.K_UP:
                        self.selected_speed_index = (self.selected_speed_index - 1) % len(self.speed_options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_speed_index = (self.selected_speed_index + 1) % len(self.speed_options)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.speed = self.speed_options[self.selected_speed_index]
                        self.game_state = 'playing'
                        self.last_move_time = pygame.time.get_ticks()
                    elif event.key == pygame.K_ESCAPE:
                        return False
                        
                elif self.game_state == 'playing':
                    # Arrow key controls
                    if event.key == pygame.K_UP and self.direction != (0, 1):
                        self.next_direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        self.next_direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                        self.next_direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.next_direction = (1, 0)
                    elif event.key == pygame.K_ESCAPE:
                        self.game_state = 'menu'
                        
                elif self.game_state == 'game_over':
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.reset_game()
                        self.game_state = 'playing'
                        self.last_move_time = pygame.time.get_ticks()
                    elif event.key == pygame.K_ESCAPE:
                        self.game_state = 'menu'
                        self.reset_game()
        return True
    
    def update_game(self):
        if self.game_state != 'playing':
            return
            
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time < SPEED_SETTINGS[self.speed]:
            return
            
        self.last_move_time = current_time
        self.direction = self.next_direction
        
        # Move snake
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.game_state = 'game_over'
            return
            
        # Check self collision
        if new_head in self.snake:
            self.game_state = 'game_over'
            return
            
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            self.snake.pop()
    
    def draw_menu(self):
        self.screen.fill(BLACK)
        
        # Title
        title_text = self.big_font.render("SNAKE GAME", True, GREEN)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title_text, title_rect)
        
        # Speed selection title
        speed_text = self.font.render("Choose Speed:", True, WHITE)
        speed_rect = speed_text.get_rect(center=(WINDOW_WIDTH // 2, 250))
        self.screen.blit(speed_text, speed_rect)
        
        # Speed options with selection highlight
        for i, speed_option in enumerate(self.speed_options):
            y_pos = 320 + i * 60
            
            # Highlight selected option
            if i == self.selected_speed_index:
                # Draw selection box
                selection_rect = pygame.Rect(WINDOW_WIDTH // 2 - 100, y_pos - 20, 200, 50)
                pygame.draw.rect(self.screen, DARK_GREEN, selection_rect)
                pygame.draw.rect(self.screen, GREEN, selection_rect, 3)
                
                # Arrow indicators
                arrow_left = self.font.render("►", True, YELLOW)
                arrow_right = self.font.render("◄", True, YELLOW)
                self.screen.blit(arrow_left, (WINDOW_WIDTH // 2 - 140, y_pos - 10))
                self.screen.blit(arrow_right, (WINDOW_WIDTH // 2 + 110, y_pos - 10))
                
                text_color = WHITE
            else:
                text_color = GRAY
            
            option_text = self.font.render(speed_option.upper(), True, text_color)
            option_rect = option_text.get_rect(center=(WINDOW_WIDTH // 2, y_pos))
            self.screen.blit(option_text, option_rect)
        
        # Instructions
        instructions = [
            "↑↓ Navigate    ENTER/SPACE Select",
            "ESC to quit"
        ]
        
        for i, instruction in enumerate(instructions):
            inst_text = self.small_font.render(instruction, True, GRAY)
            inst_rect = inst_text.get_rect(center=(WINDOW_WIDTH // 2, 500 + i * 25))
            self.screen.blit(inst_text, inst_rect)
    
    def draw_game(self):
        self.screen.fill(BLACK)
        
        # Draw snake
        for i, segment in enumerate(self.snake):
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            if i == 0:  # Head
                pygame.draw.rect(self.screen, DARK_GREEN, rect)
                pygame.draw.rect(self.screen, GREEN, rect, 2)
                # Draw eyes
                eye_size = 3
                eye1_x = x * GRID_SIZE + 5
                eye2_x = x * GRID_SIZE + GRID_SIZE - 8
                eye_y = y * GRID_SIZE + 5
                pygame.draw.circle(self.screen, WHITE, (eye1_x, eye_y), eye_size)
                pygame.draw.circle(self.screen, WHITE, (eye2_x, eye_y), eye_size)
                pygame.draw.circle(self.screen, BLACK, (eye1_x, eye_y), 1)
                pygame.draw.circle(self.screen, BLACK, (eye2_x, eye_y), 1)
            else:  # Body
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, DARK_GREEN, rect, 1)
        
        # Draw food with animation effect
        food_x, food_y = self.food
        food_rect = pygame.Rect(food_x * GRID_SIZE, food_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)
        pygame.draw.rect(self.screen, YELLOW, food_rect, 2)
        # Add a shine effect
        shine_rect = pygame.Rect(food_x * GRID_SIZE + 2, food_y * GRID_SIZE + 2, 6, 6)
        pygame.draw.rect(self.screen, WHITE, shine_rect)
        
        # Draw score and speed
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        speed_text = self.small_font.render(f"Speed: {self.speed.title()}", True, WHITE)
        self.screen.blit(speed_text, (10, 50))
        
        length_text = self.small_font.render(f"Length: {len(self.snake)}", True, WHITE)
        self.screen.blit(length_text, (10, 70))
        
        # Draw subtle grid
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (15, 15, 15), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (15, 15, 15), (0, y), (WINDOW_WIDTH, y))
            
        # Instructions
        inst_text = self.small_font.render("Arrow Keys: Move | ESC: Menu", True, GRAY)
        self.screen.blit(inst_text, (WINDOW_WIDTH - 220, 10))
    
    def draw_game_over(self):
        self.screen.fill(BLACK)
        
        # Game Over text
        game_over_text = self.big_font.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, 200))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Final score
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, 280))
        self.screen.blit(score_text, score_rect)
        
        # Length achieved
        length_text = self.font.render(f"Snake Length: {len(self.snake)}", True, WHITE)
        length_rect = length_text.get_rect(center=(WINDOW_WIDTH // 2, 320))
        self.screen.blit(length_text, length_rect)
        
        # Options
        options = [
            "SPACE/ENTER - Play Again",
            "ESC - Main Menu"
        ]
        
        for i, option in enumerate(options):
            option_text = self.font.render(option, True, YELLOW)
            option_rect = option_text.get_rect(center=(WINDOW_WIDTH // 2, 400 + i * 40))
            self.screen.blit(option_text, option_rect)
    
    def run(self):
        running = True
        
        while running:
            running = self.handle_events()
            self.update_game()
            
            if self.game_state == 'menu':
                self.draw_menu()
            elif self.game_state == 'playing':
                self.draw_game()
            elif self.game_state == 'game_over':
                self.draw_game_over()
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

def main():
    try:
        game = SnakeGame()
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
