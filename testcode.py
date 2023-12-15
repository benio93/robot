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

    w_state = ""
    keys_pressed = pygame.key.get_pressed()

    # Check if the W key is pressed
    if keys_pressed[pygame.K_w]:
        w_state = "W"
    else:
        w_state = "X"
    ser.write(w_state.encode('utf-8'))
   # print(w_state)
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
