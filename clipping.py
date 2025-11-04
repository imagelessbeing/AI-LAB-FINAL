import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 700

# 🎨 New modern color palette
BACKGROUND_GRADIENT_TOP = (30, 30, 60)
BACKGROUND_GRADIENT_BOTTOM = (15, 15, 30)
TEXT_PRIMARY = (240, 240, 255)
TEXT_SECONDARY = (180, 180, 220)
ACCENT_GREEN = (0, 255, 180)
ACCENT_RED = (255, 80, 80)
ACCENT_YELLOW = (255, 220, 100)
ACCENT_BLUE = (100, 180, 255)
CLIP_WINDOW_COLOR = (100, 255, 200)
PANEL_BG = (40, 40, 80)
PANEL_BORDER = (70, 70, 120)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✨ Clipping Visualizer ✨")

# 🪩 Use a modern font (optional: replace with custom TTF)
font = pygame.font.SysFont("arial", 26, bold=True)
small_font = pygame.font.SysFont("arial", 20)
tiny_font = pygame.font.SysFont("arial", 18)

# Global variables
clip_window = []
mode = "SETUP"  # SETUP, POINT, LINE, POLYGON
points = []
lines = []
polygons = []
current_polygon = []
clipped_results = []

def draw_text(text, pos, color=TEXT_PRIMARY, font_obj=font):
    text_surface = font_obj.render(text, True, color)
    screen.blit(text_surface, pos)

def draw_background():
    """Draw gradient background"""
    for y in range(HEIGHT):
        r = BACKGROUND_GRADIENT_TOP[0] + (BACKGROUND_GRADIENT_BOTTOM[0] - BACKGROUND_GRADIENT_TOP[0]) * y // HEIGHT
        g = BACKGROUND_GRADIENT_TOP[1] + (BACKGROUND_GRADIENT_BOTTOM[1] - BACKGROUND_GRADIENT_TOP[1]) * y // HEIGHT
        b = BACKGROUND_GRADIENT_TOP[2] + (BACKGROUND_GRADIENT_BOTTOM[2] - BACKGROUND_GRADIENT_TOP[2]) * y // HEIGHT
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

def point_clip(point, x_min, y_min, x_max, y_max):
    x, y = point
    return x_min <= x <= x_max and y_min <= y <= y_max

def liang_barsky_clip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]
    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return None
        elif p[i] != 0:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
            else:
                u2 = min(u2, t)
    if u1 > u2:
        return None
    return (x1 + u1 * dx, y1 + u1 * dy, x1 + u2 * dx, y1 + u2 * dy)

def sutherland_hodgeman_clip(polygon, x_min, y_min, x_max, y_max):
    def inside(p, edge):
        if edge == 0: return p[0] >= x_min
        elif edge == 1: return p[0] <= x_max
        elif edge == 2: return p[1] >= y_min
        return p[1] <= y_max

    def compute_intersection(p1, p2, edge):
        x1, y1 = p1
        x2, y2 = p2
        if edge == 0:
            x, y = x_min, y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
        elif edge == 1:
            x, y = x_max, y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
        elif edge == 2:
            y, x = y_min, x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
        else:
            y, x = y_max, x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
        return (x, y)

    output = list(polygon)
    for edge in range(4):
        input_list = output
        output = []
        if not input_list:
            break
        for i in range(len(input_list)):
            current = input_list[i]
            prev = input_list[i - 1]
            if inside(current, edge):
                if not inside(prev, edge):
                    output.append(compute_intersection(prev, current, edge))
                output.append(current)
            elif inside(prev, edge):
                output.append(compute_intersection(prev, current, edge))
    return output

def draw_clip_window():
    if len(clip_window) == 2:
        x_min = min(clip_window[0][0], clip_window[1][0])
        y_min = min(clip_window[0][1], clip_window[1][1])
        x_max = max(clip_window[0][0], clip_window[1][0])
        y_max = max(clip_window[0][1], clip_window[1][1])
        pygame.draw.rect(screen, CLIP_WINDOW_COLOR, (x_min, y_min, x_max - x_min, y_max - y_min), 3)

def draw_ui():
    pygame.draw.rect(screen, PANEL_BG, (0, HEIGHT - 150, WIDTH, 150))
    pygame.draw.line(screen, PANEL_BORDER, (0, HEIGHT - 150), (WIDTH, HEIGHT - 150), 3)
    
    y_offset = HEIGHT - 140
    draw_text("✨ Clipping Control Panel ✨", (10, y_offset), ACCENT_BLUE, font)
    y_offset += 35

    if mode == "SETUP":
        draw_text("Setup Mode: Click 2 points to define clipping window", (10, y_offset), TEXT_SECONDARY, small_font)
    else:
        draw_text(f"Current Mode: {mode}", (10, y_offset), ACCENT_YELLOW, small_font)
        y_offset += 25
        if mode == "POINT":
            draw_text(f"Points: {len(points)}", (10, y_offset), ACCENT_GREEN, tiny_font)
        elif mode == "LINE":
            draw_text(f"Lines: {len(lines)}", (10, y_offset), ACCENT_GREEN, tiny_font)
        elif mode == "POLYGON":
            draw_text(f"Polygons: {len(polygons)}", (10, y_offset), ACCENT_GREEN, tiny_font)

    y_offset = HEIGHT - 60
    draw_text("Controls: [1] Point  [2] Line  [3] Polygon  [C] Clear  [R] Reset  [ESC] Quit", (10, y_offset), TEXT_SECONDARY, tiny_font)

def perform_clipping():
    global clipped_results
    clipped_results = []
    if len(clip_window) != 2:
        return
    x_min = min(clip_window[0][0], clip_window[1][0])
    y_min = min(clip_window[0][1], clip_window[1][1])
    x_max = max(clip_window[0][0], clip_window[1][0])
    y_max = max(clip_window[0][1], clip_window[1][1])
    if mode == "POINT":
        clipped_results = [p if point_clip(p, x_min, y_min, x_max, y_max) else None for p in points]
    elif mode == "LINE":
        clipped_results = [liang_barsky_clip(*l, x_min, y_min, x_max, y_max) for l in lines]
    elif mode == "POLYGON":
        clipped_results = [r if r and len(r) >= 3 else None for r in
                           [sutherland_hodgeman_clip(poly, x_min, y_min, x_max, y_max) for poly in polygons]]

def draw_scene():
    draw_background()
    draw_clip_window()

    if mode == "POINT":
        for i, p in enumerate(points):
            color = ACCENT_GREEN if clipped_results[i] else ACCENT_RED
            pygame.draw.circle(screen, color, (int(p[0]), int(p[1])), 6)
    elif mode == "LINE":
        for i, l in enumerate(lines):
            pygame.draw.line(screen, ACCENT_RED, (l[0], l[1]), (l[2], l[3]), 2)
            if clipped_results[i]:
                c = clipped_results[i]
                pygame.draw.line(screen, ACCENT_GREEN, (int(c[0]), int(c[1])), (int(c[2]), int(c[3])), 3)
    elif mode == "POLYGON":
        for p in current_polygon:
            pygame.draw.circle(screen, ACCENT_YELLOW, (int(p[0]), int(p[1])), 5)
        if len(current_polygon) > 1:
            pygame.draw.lines(screen, ACCENT_YELLOW, False, current_polygon, 2)
        for i, poly in enumerate(polygons):
            pygame.draw.polygon(screen, ACCENT_RED, poly, 2)
            if clipped_results[i]:
                pygame.draw.polygon(screen, ACCENT_GREEN, clipped_results[i], 0)
                pygame.draw.polygon(screen, ACCENT_BLUE, clipped_results[i], 2)

    draw_ui()
    pygame.display.flip()

# Main loop
running = True
temp_line_point = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] < HEIGHT - 150:
                if mode == "SETUP":
                    clip_window.append(pos)
                    if len(clip_window) == 2:
                        mode = "POINT"
                elif mode == "POINT":
                    points.append(pos)
                    perform_clipping()
                elif mode == "LINE":
                    if temp_line_point is None:
                        temp_line_point = pos
                    else:
                        lines.append((temp_line_point[0], temp_line_point[1], pos[0], pos[1]))
                        temp_line_point = None
                        perform_clipping()
                elif mode == "POLYGON":
                    current_polygon.append(pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_1 and len(clip_window) == 2:
                mode = "POINT"
                perform_clipping()
            elif event.key == pygame.K_2 and len(clip_window) == 2:
                mode = "LINE"
                perform_clipping()
            elif event.key == pygame.K_3 and len(clip_window) == 2:
                mode = "POLYGON"
                perform_clipping()
            elif event.key == pygame.K_c:
                points, lines, polygons, current_polygon, clipped_results = [], [], [], [], []
            elif event.key == pygame.K_r:
                clip_window, points, lines, polygons, current_polygon, clipped_results = [], [], [], [], [], []
                mode = "SETUP"
            elif event.key == pygame.K_SPACE and mode == "POLYGON" and len(current_polygon) >= 3:
                polygons.append(list(current_polygon))
                current_polygon = []
                perform_clipping()

    draw_scene()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()