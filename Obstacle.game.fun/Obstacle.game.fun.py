from site import getuserbase
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Obstacles")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Player
player_size = 50
player_pos = [WIDTH / 2, HEIGHT - 2 * player_size]

# Obstacles
obstacle_size = 50
obstacle_pos = [random.randint(0, WIDTH - obstacle_size), 0]
obstacle_list = [obstacle_pos]

# Speed and score
speed = 10
score = 0

# Function to create obstacles
def create_obstacles():
    delay = random.random()
    if len(obstacle_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - obstacle_size)
        y_pos = 0
        obstacle_list.append([x_pos, y_pos])

# Function to move obstacles
def move_obstacles():
    for idx, obstacle_pos in enumerate(obstacle_list):
        if obstacle_pos[1] >= 0 and obstacle_pos[1] < HEIGHT:
            obstacle_pos[1] += speed
        else:
            obstacle_list.pop(idx)

# Function to draw obstacles
def draw_obstacles():
    for obstacle_pos in obstacle_list:
        pygame.draw.rect(window, RED, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

# Function to detect collision
def collision_detection(player_pos, obstacle_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    o_x = obstacle_pos[0]
    o_y = obstacle_pos[1]

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obstacle_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obstacle_size)):
            return True
    return False

# Function to update the score
def update_score(score):
    score += 1
    return score

# Function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, [10, 10])

# Main function

# Function to move the player
def move_player(keys):
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

# Main function
def main():
    global speed, score
    username = getuserbase()
    print(f"Welcome {username}! Let's get started.")
    
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        move_player(keys)

        window.fill(WHITE)
        create_obstacles()
        move_obstacles()
        draw_obstacles()
        display_score(score)

        pygame.draw.rect(window, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

        for obstacle_pos in obstacle_list:
            if collision_detection(player_pos, obstacle_pos):
                print("Game Over!")
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(30)  # Set the frame rate to 30 frames per second

    # Quit Pygame (moved inside main() function)
    pygame.quit()
    sys.exit()

# Start the game
# Function to display the settings menu
def show_settings_menu():
    settings_menu = True
    while settings_menu:
        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    settings_menu = False

        # Display settings options
        settings_text = font.render("Settings Menu", True, BLACK)
        window.blit(settings_text, [WIDTH // 2 - 100, HEIGHT // 2 - 50])

        pygame.display.update()

# Main function
def main():
    global speed, score
    username = getuserbase()
    print(f"Welcome {username}! Let's get started.")
    
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print("Game paused.")
                    show_settings_menu()

        keys = pygame.key.get_pressed()
        move_player(keys)

        window.fill(WHITE)
        create_obstacles()
        move_obstacles()
        draw_obstacles()
        display_score(score)

        pygame.draw.rect(window, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

        for obstacle_pos in obstacle_list:
            if collision_detection(player_pos, obstacle_pos):
                print("Game Over!")
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(30)  # Set the frame rate to 30 frames per second

    # Quit Pygame (moved inside main() function)
    pygame.quit()
    sys.exit()

# Start the game
main()

main()
