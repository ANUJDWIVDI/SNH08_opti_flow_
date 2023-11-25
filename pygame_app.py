# main.py

import pygame
import sys

pygame.init()

# Initialize Pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("OptiCarFlow Pygame Input")

# Colors
white = (255, 255, 255)
brown = (139, 69, 19)
red = (255, 0, 0)
black = (0, 0, 0)

# Clock to control the frame rate
clock = pygame.time.Clock()

def get_input(width, height):
    # Input page
    font = pygame.font.Font(None, 36)
    input_text_time = ''
    input_text_percentages = ['', '', '']
    input_text_labors = ['', '', '']

    input_rect_time = pygame.Rect(250, 150, 300, 50)
    input_rect_percentages = [pygame.Rect(250, 250, 300, 50) for _ in range(3)]
    input_rect_labors = [pygame.Rect(250, 350, 300, 50) for _ in range(3)]

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False

    text_time = font.render('Enter Total Time (in minutes):', True, (0, 0, 0))
    text_percentages = [font.render(f'Enter Percentage for Section {i + 1}:', True, (0, 0, 0)) for i in range(3)]
    text_labors = [font.render(f'Enter Labor for Section {i + 1}:', True, (0, 0, 0)) for i in range(3)]

    text_rect_time = text_time.get_rect(center=(width // 2, 100))
    text_rect_percentages = [text.get_rect(center=(width // 2, 200 + i * 100)) for i, text in enumerate(text_percentages)]
    text_rect_labors = [text.get_rect(center=(width // 2, 300 + i * 100)) for i, text in enumerate(text_labors)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_time.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive
                    for i in range(3):
                        if input_rect_percentages[i].collidepoint(event.pos):
                            active = True
                            color = color_active
                            input_text_percentages[i] = ''
                        if input_rect_labors[i].collidepoint(event.pos):
                            active = True
                            color = color_active
                            input_text_labors[i] = ''
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            total_time = int(input_text_time)
                            return total_time, [float(percentage) / 100 for percentage in input_text_percentages], [
                                int(labor) for labor in input_text_labors]
                        except ValueError:
                            print("Invalid input. Please enter valid numbers.")
                    elif event.key == pygame.K_BACKSPACE:
                        input_text_time = input_text_time[:-1]
                        for i in range(3):
                            if input_rect_percentages[i].collidepoint(event.pos):
                                input_text_percentages[i] = input_text_percentages[i][:-1]
                            if input_rect_labors[i].collidepoint(event.pos):
                                input_text_labors[i] = input_text_labors[i][:-1]
                    else:
                        if input_rect_time.collidepoint(event.pos):
                            input_text_time += event.unicode
                        for i in range(3):
                            if input_rect_percentages[i].collidepoint(event.pos):
                                input_text_percentages[i] += event.unicode
                            if input_rect_labors[i].collidepoint(event.pos):
                                input_text_labors[i] += event.unicode

        screen.fill(white)
        pygame.draw.rect(screen, color, input_rect_time, 2)
        input_surface_time = font.render(input_text_time, True, (0, 0, 0))
        width_time = max(200, input_surface_time.get_width() + 10)
        input_rect_time.w = width_time
        screen.blit(text_time, text_rect_time)
        screen.blit(input_surface_time, (input_rect_time.x + 5, input_rect_time.y + 5))

        for i in range(3):
            pygame.draw.rect(screen, color, input_rect_percentages[i], 2)
            input_surface_percentage = font.render(input_text_percentages[i], True, (0, 0, 0))
            width_percentage = max(200, input_surface_percentage.get_width() + 10)
            input_rect_percentages[i].w = width_percentage
            screen.blit(text_percentages[i], text_rect_percentages[i])
            screen.blit(input_surface_percentage, (input_rect_percentages[i].x + 5, input_rect_percentages[i].y + 5))

            pygame.draw.rect(screen, color, input_rect_labors[i], 2)
            input_surface_labor = font.render(input_text_labors[i], True, (0, 0, 0))
            width_labor = max(200, input_surface_labor.get_width() + 10)
            input_rect_labors[i].w = width_labor
            screen.blit(text_labors[i], text_rect_labors[i])
            screen.blit(input_surface_labor, (input_rect_labors[i].x + 5, input_rect_labors[i].y + 5))

        pygame.display.flip()
        clock.tick(30)


def display_result(total_time, section_times, section_labors):
    # Result page
    section_width = width // 3
    section_height = height
    ladder_width = 50
    ladder_height = 100
    box_width = width * 0.06
    box_height = height
    box_x = width * 0.94

    labor_dot_x = box_x + box_width + 10
    time_dot_x = box_x + box_width + 30
    dot_y = height - 50

    time_taken = [0, 0, 0]
    labor_required = [0, 0, 0]

    for i in range(3):
        time_taken[i] = total_time * section_times[i]
        labor_required[i] = total_time * section_labors[i]

    running = True
    while running:
        for event, _ in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)

        # Draw brown box
        pygame.draw.rect(screen, brown, (box_x, 0, box_width, box_height))

        # Draw section dividers
        for i in range(1, 3):
            pygame.draw.line(screen, (0, 0, 0), (i * section_width, 0), (i * section_width, height), 2)

        # Draw ladder
        pygame.draw.rect(screen, brown, (ladder_width, height - ladder_height, ladder_width, ladder_height))

        # Display time and labor information
        font = pygame.font.Font(None, 36)
        for i in range(3):
            text = font.render(f"Section {i + 1}: Time {time_taken[i]}, Labor {labor_required[i]}", True, (0, 0, 0))
            screen.blit(text, (i * section_width + 10, 10))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    total_time, section_percentages, section_labors = get_input(width, height)
    display_result(total_time, section_percentages, section_labors)
