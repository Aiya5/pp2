import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Advanced Paint Program")

# Drawing variables
drawing = False
last_pos = None
current_color = BLACK
brush_size = 5
current_tool = "pen"  # pen, rectangle, circle, eraser

# Color palette positions
color_buttons = [
    {"rect": pygame.Rect(10, 10, 30, 30), "color": BLACK},
    {"rect": pygame.Rect(50, 10, 30, 30), "color": RED},
    {"rect": pygame.Rect(90, 10, 30, 30), "color": GREEN},
    {"rect": pygame.Rect(130, 10, 30, 30), "color": BLUE},
    {"rect": pygame.Rect(170, 10, 30, 30), "color": YELLOW},
    {"rect": pygame.Rect(210, 10, 30, 30), "color": PURPLE},
    {"rect": pygame.Rect(250, 10, 30, 30), "color": CYAN},
    {"rect": pygame.Rect(290, 10, 30, 30), "color": WHITE}
]

# Tool buttons
tool_buttons = [
    {"rect": pygame.Rect(350, 10, 80, 30), "tool": "pen", "text": "Pen"},
    {"rect": pygame.Rect(440, 10, 80, 30), "tool": "rectangle", "text": "Rectangle"},
    {"rect": pygame.Rect(530, 10, 80, 30), "tool": "circle", "text": "Circle"},
    {"rect": pygame.Rect(620, 10, 80, 30), "tool": "eraser", "text": "Eraser"}
]

# Drawing surfaces
canvas = pygame.Surface((screen_width, screen_height))
canvas.fill(WHITE)

# Temporary surface for shapes
temp_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

# Shape drawing variables
start_pos = None
current_shape = None

def draw_interface():
    """Draw the color palette and tool buttons"""
    # Draw color palette
    for button in color_buttons:
        pygame.draw.rect(screen, button["color"], button["rect"])
        pygame.draw.rect(screen, BLACK, button["rect"], 1)
    
    # Draw tool buttons
    for button in tool_buttons:
        color = (200, 200, 200) if current_tool == button["tool"] else (100, 100, 100)
        pygame.draw.rect(screen, color, button["rect"])
        pygame.draw.rect(screen, BLACK, button["rect"], 1)
        
        font = pygame.font.Font(None, 24)
        text = font.render(button["text"], True, BLACK)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)
    
    # Draw current color indicator
    pygame.draw.rect(screen, current_color, (700, 10, 30, 30))
    pygame.draw.rect(screen, BLACK, (700, 10, 30, 30), 1)

def draw_pen(pos):
    """Draw with pen tool"""
    if last_pos:
        pygame.draw.line(canvas, current_color, last_pos, pos, brush_size)
    return pos

def draw_rectangle(start, end):
    """Draw rectangle"""
    temp_surface.fill((0, 0, 0, 0))  # Clear temporary surface
    rect = pygame.Rect(
        min(start[0], end[0]),
        min(start[1], end[1]),
        abs(end[0] - start[0]),
        abs(end[1] - start[1])
    )
    pygame.draw.rect(temp_surface, current_color, rect, brush_size)
    return rect

def draw_circle(start, end):
    """Draw circle"""
    temp_surface.fill((0, 0, 0, 0))  # Clear temporary surface
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    radius = int(((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5) // 2
    pygame.draw.circle(temp_surface, current_color, (center_x, center_y), radius, brush_size)
    return (center_x, center_y, radius)

def draw_eraser(pos):
    """Erase with eraser tool"""
    if last_pos:
        pygame.draw.line(canvas, WHITE, last_pos, pos, brush_size * 2)
    return pos

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                
                # Check color buttons
                for button in color_buttons:
                    if button["rect"].collidepoint(pos):
                        current_color = button["color"]
                        break
                
                # Check tool buttons
                for button in tool_buttons:
                    if button["rect"].collidepoint(pos):
                        current_tool = button["tool"]
                        break
                
                # Start drawing
                if pos[1] > 50:  # Below the toolbar
                    drawing = True
                    last_pos = pos
                    start_pos = pos
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                
                # Finalize shape drawing
                if current_tool in ["rectangle", "circle"] and current_shape:
                    # Copy from temp surface to canvas
                    canvas.blit(temp_surface, (0, 0))
                    temp_surface.fill((0, 0, 0, 0))  # Clear temp surface
                
                last_pos = None
                start_pos = None
                current_shape = None
        
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                pos = pygame.mouse.get_pos()
                
                if current_tool == "pen":
                    last_pos = draw_pen(pos)
                
                elif current_tool == "eraser":
                    last_pos = draw_eraser(pos)
                
                elif current_tool == "rectangle" and start_pos:
                    current_shape = draw_rectangle(start_pos, pos)
                
                elif current_tool == "circle" and start_pos:
                    current_shape = draw_circle(start_pos, pos)
    
    # Draw everything
    screen.blit(canvas, (0, 0))  # Draw canvas
    screen.blit(temp_surface, (0, 0))  # Draw temporary shapes
    draw_interface()  # Draw UI
    
    pygame.display.flip()

pygame.quit()