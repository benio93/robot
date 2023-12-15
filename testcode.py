import pygame
import serial

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
# Initialize Serial Communication
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Set timeout to 0 for non-blocking behavior
ser.reset_input_buffer()
# Main loop control variable
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    w_state = "W" if keys_pressed[pygame.K_w] else "X"
    s_state = "S" if keys_pressed[pygame.K_s] else "X"
    a_state = "A" if keys_pressed[pygame.K_a] else "X"
    d_state = "D" if keys_pressed[pygame.K_d] else "X"

    # Generate valid combinations
    valid_combinations = [
        combination
        for combination in [w_state, s_state, a_state, d_state]
        if combination != ""
    ]

    # Combine and sort states
    combined_state = ''.join(sorted(valid_combinations))
    print(combined_state)
    
    ser.write(combined_state.encode('utf-8'))

    # Read and print the response
    line = ser.readline().decode('utf-8').rstrip()
    print(line)