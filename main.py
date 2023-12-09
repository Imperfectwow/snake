import pygame
import random

# Initialize pygame
pygame.init()


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


dis_width = 750
dis_height = 750


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')


snake_block = 15
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont('arial', 50)

image_path = 'images/'
# Load the images
snake_img = pygame.image.load(image_path + 'snake.png')
apple_img = pygame.image.load(image_path + 'apple.png')




snake_img = pygame.transform.scale(snake_img, (snake_block, snake_block))
apple_size = snake_block * 2
apple_img = pygame.transform.scale(apple_img, (apple_size, apple_size))


def draw_apple(foodx, foody):
    dis.blit(apple_img, (foodx, foody))

def score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    lines = msg.split(' ')  # Split the message by spaces to handle multiple lines if needed.
    line_height = font_style.size('Tg')[1]  # Get the height of the text.
    start_y = dis_height // 2 - (line_height * len(lines) // 2)  # Start at the vertical center.

    for index, line in enumerate(lines):
        mesg = font_style.render(line, True, color)
        mesg_rect = mesg.get_rect(center=(dis_width // 2, start_y + index * line_height))
        dis.blit(mesg, mesg_rect)

    pygame.display.update()  # Make sure to update the display to show the message.


def gameLoop():  # creating a function
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # When the snake moves
    x1_change = 0
    y1_change = 0

    paused = False
    # Define the snake's length
    snake_List = []
    Length_of_snake = 1

    # Location of the food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        draw_apple(foodx, foody)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 >= foodx and x1 < foodx + apple_size and y1 >= foody and y1 < foody + apple_size:
            foodx = round(random.randrange(0, dis_width - apple_size) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - apple_size) / 10.0) * 10.0
            Length_of_snake += 1
            snake_List.append(snake_Head)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
