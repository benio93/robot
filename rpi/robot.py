import serial
import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))

# Initialize Serial Communication
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)  # Set timeout to 0 for non-blocking behavior
ser.reset_input_buffer()
# Main loop control variable
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            keys_pressed = pygame.key.get_pressed()
            key_state = "W" if keys_pressed[pygame.K_w] else "S" if keys_pressed[pygame.K_s] else \
                "A" if keys_pressed[pygame.K_a] else "D" if keys_pressed[pygame.K_d] else "X"
            
            print(key_state)
            ser.write(key_state.encode('utf-8'))

            # Read available data (non-blocking)
            line = ser.read(ser.in_waiting).decode('utf-8').rstrip()
            if line:
                print(line)

        elif event.type == pygame.QUIT:
            # Handle the QUIT event (e.g., window close button)
            running = False    
# Clean up resources
pygame.quit()
ser.close()
