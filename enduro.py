import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enduro Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Game variables
player_width, player_height = 50, 100
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT // 2 - player_height // 2
player_speed = 5
player_velocity = 0
player_deceleration = 0.05  # Slow down effect

rival_width, rival_height = 50, 100
rivals_up = []  # Rivals going upwards in the North lane
rivals_down = []  # Rivals going downwards in the South lane
rival_base_speed_min = 3
rival_base_speed_max = 5
speed_increment = 0.1

road_width = 400
lane_width = road_width // 2  # Two lanes (left and right)
road_x = WIDTH // 2 - road_width // 2

# Define slots for the cars in the lanes
north_lane_slots = {'right': 3, 'center': 4, 'left': 6}  # Slow, medium, fast
south_lane_slots = {'right': 3, 'center': 4, 'left': 6}  # Slow, medium, fast

# Global game variables
score = 0
kilometers = 0.0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
time_elapsed = 0
message_font = pygame.font.Font(None, 48)
game_over = False

# Function to create a new rival car
def create_rival():
    # Randomly choose to spawn in the South (down) or North (up) lane
    lane_choice = random.choice([0, 1])  # 0 for South lane (down), 1 for North lane (up)
    
    # Randomly select lane within each side (3 options)
    lane_pos = random.randint(0, 2)  # Select right, center, or left slot
    
    # Speed based on lane (slow, medium, fast)
    if lane_pos == 0:
        speed = random.randint(2, 3)  # Slow
    elif lane_pos == 1:
        speed = random.randint(4, 5)  # Medium
    else:
        speed = random.randint(6, 7)  # Fast
    
    if lane_choice == 0:  # South lane (down)
        # Spawn above the screen (coming down)
        x_pos = road_x + lane_pos * lane_width
        y_pos = random.randint(-200, -rival_height)  
        rivals_down.append({'rect': pygame.Rect(x_pos, y_pos, rival_width, rival_height), 'speed': speed})
        
    else:  # North lane (up)
        # Spawn below the screen (coming up)
        x_pos = road_x + lane_pos * lane_width
        y_pos = random.randint(HEIGHT + 10, HEIGHT + 200)  
        rivals_up.append({'rect': pygame.Rect(x_pos, y_pos, rival_width, rival_height), 'speed': speed})

# Function to reset the game
def reset_game():
    global player_x, player_y, rivals_up, rivals_down, score, kilometers, time_elapsed, player_velocity, game_over
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT // 2 - player_height // 2
    rivals_up.clear()
    rivals_down.clear()
    score = 0
    kilometers = 0.0
    time_elapsed = 0
    player_velocity = 0
    game_over = False

# Game loop
running = True
while running:
    screen.fill(GRAY)

    # Draw road with 2 lanes (North and South)
    pygame.draw.rect(screen, BLACK, (road_x, 0, road_width, HEIGHT))
    pygame.draw.line(screen, YELLOW, (road_x + lane_width, 0), (road_x + lane_width, HEIGHT), 5)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_over:
        # Display game over message
        message_text = message_font.render("Eeeeeeita! Fim de Férias!", True, RED)
        screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT // 2 - 50))
        sub_message = font.render("Press Q to Quit or C to Restart", True, WHITE)
        screen.blit(sub_message, (WIDTH // 2 - sub_message.get_width() // 2, HEIGHT // 2 + 20))

        if keys[pygame.K_q]:
            running = False
        if keys[pygame.K_c]:
            reset_game()

        pygame.display.flip()
        clock.tick(60)
        continue

    # Player movement
    if keys[pygame.K_LEFT] and player_x > road_x:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < road_x + road_width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_velocity += speed_increment  # Player car accelerates
    if keys[pygame.K_DOWN]:
        player_velocity -= player_deceleration  # Gradual deceleration

    # Prevent negative velocity (no reverse movement)
    if player_velocity < 0:
        player_velocity = 0

    # Update kilometers based on player's speed
    kilometers += player_velocity / 100

    # Update time elapsed
    time_elapsed += clock.get_time() / 1000

    # Update player position
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, GREEN, player)

    # Update rivals going down (South lane)
    for rival in rivals_down[:]:
        rival['rect'].y += rival['speed'] + (player_velocity * 0.2)  # Rivals in South lane accelerate with the player
        if rival['rect'].colliderect(player):
            game_over = True  # End the game on collision
        if rival['rect'].y > HEIGHT:
            rivals_down.remove(rival)
            score += 1  # Increment score when a rival goes off-screen
        pygame.draw.rect(screen, RED, rival['rect'])

    # Update rivals going up (North lane)
    for rival in rivals_up[:]:
        rival['rect'].y -= rival['speed']  # Rivals in North lane maintain their independent speed
        if rival['rect'].colliderect(player):
            game_over = True  # End the game on collision
        if rival['rect'].y < -rival_height:
            rivals_up.remove(rival)
            score += 1  # Increment score when a rival goes off-screen
        pygame.draw.rect(screen, RED, rival['rect'])

    # Spawn new rivals if there is space
    if random.randint(1, 30) == 1:
        create_rival()

    # Display score and other stats
    score_text = font.render(f"Score: {score}", True, WHITE)
    kilometers_text = font.render(f"Kilometers: {kilometers:.1f} km", True, WHITE)
    time_text = font.render(f"Time: {int(time_elapsed)} s", True, WHITE)
    message_text = font.render("Cê vai descer, vai descer para B.C.", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(kilometers_text, (10, 40))
    screen.blit(time_text, (10, 70))
    screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()

