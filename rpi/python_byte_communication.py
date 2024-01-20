import pygame
import serial
import struct

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))

# Initialize Serial Communication
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Adjust the port as necessary
ser.reset_input_buffer()

# Main loop control variable
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    # Encode key states in a byte
    command_byte = 0
    command_byte |= keys_pressed[pygame.K_w] << 0  # Set bit 0 if 'W' is pressed
    command_byte |= keys_pressed[pygame.K_a] << 1  # Set bit 1 if 'A' is pressed
    command_byte |= keys_pressed[pygame.K_s] << 2  # Set bit 2 if 'S' is pressed
    command_byte |= keys_pressed[pygame.K_d] << 3  # Set bit 3 if 'D' is pressed
    # You can add more keys here following the same pattern

    # Print the binary representation
    binary_representation = bin(command_byte)
    print(f"Binary representation: {binary_representation}")


    # Send the command byte
    ser.write(bytes([command_byte]))

    # Read and print the response (optional)
    #line = ser.readline()#.decode('utf-8').rstrip()
   # print(line)
    line = ser.readline()  # Read the line as bytes
    print(f"Received raw bytes: {line}")
        # Optionally, convert to hex representation for readability
    hex_representation = line.hex()
    print(f"Hexadecimal representation: {hex_representation}")
   
# Close serial connection
ser.close()
