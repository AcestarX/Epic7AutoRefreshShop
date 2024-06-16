# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:50:45 2024

@author: Acestar
"""

import pyautogui
import cv2
import numpy as np
import time
import logging
import random
import keyboard

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load images
mystic_bookmark_image = cv2.imread('mystic_bookmark.png')
covenant_bookmark_image = cv2.imread('covenant_bookmark.png')
mystic_buy_button_image = cv2.imread('mystic_buy_button.png')
covenant_buy_button_image = cv2.imread('covenant_buy_button.png')
mystic_confirm_button_image = cv2.imread('mystic_confirm_button.png')
covenant_confirm_button_image = cv2.imread('covenant_confirm_button.png')
refresh_button_image = cv2.imread('refresh_button.png')
refresh_confirm_button_image = cv2.imread('refresh_confirm_button.png')

# Global variable to control the loop
running = True

# Function to find and click button
def find_and_click(image, confidence=0.7, click_position='center'):
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    logging.info(f"Matching confidence for {image}: {max_val}")
    if max_val >= confidence:
        x, y = max_loc
        h, w, _ = image.shape
        if click_position == 'bottom_right':
            pyautogui.click(x + w - 5, y + h - 5)  # Adjust these offsets as needed
        else:
            pyautogui.click(x + w / 2, y + h / 2)
        return True
    return False

# Function to perform random clicks more centered on the screen but adjusted to the right
def random_clicks():
    screen_width, screen_height = pyautogui.size()
    x_center = (screen_width * 3) // 4  # Shift clicks to the right
    y_center = screen_height // 2

    for _ in range(random.randint(1, 3)):  # Reduced number of random clicks
        x = random.randint(x_center - 50, x_center + 50)
        y = random.randint(y_center - 50, y_center + 50)
        pyautogui.click(x, y)
        time.sleep(random.uniform(0.1, 0.3))  # Further reduced delay between clicks

# Function to refresh the shop
def refresh_shop():
    logging.info("Refreshing the shop...")
    if find_and_click(refresh_button_image):
        time.sleep(0.3)  # Reduced wait time for the refresh confirm dialog
        if find_and_click(refresh_confirm_button_image):
            random_clicks()  # Perform random clicks during the refresh process
            time.sleep(1)  # Reduced wait time for the shop to refresh
        else:
            logging.error("Refresh confirm button not found!")
    else:
        logging.error("Refresh button not found!")

# Function to scroll the shop using scroll wheel
def scroll_shop():
    logging.info("Scrolling the shop...")
    pyautogui.scroll(-3)  # Scroll down (negative value)
    time.sleep(0.3)  # Reduced wait time for the scroll to complete

# Function to attempt purchase of an item
def attempt_purchase(item_image, buy_button_image, confirm_button_image, purchase_count, limit):
    if find_and_click(item_image):
        time.sleep(0.5)  # Adjusted wait time for the buy button to appear
        if find_and_click(buy_button_image, click_position='bottom_right'):
            logging.info(f"Clicked {buy_button_image}, waiting for confirmation button...")
            time.sleep(0.5)  # Adjusted wait time for the confirm dialog to appear
            if find_and_click(confirm_button_image):
                logging.info(f"Purchase {purchase_count + 1} complete")
                # Scroll and attempt to purchase again after a successful purchase
                scroll_shop()
                purchase_count = attempt_purchase(item_image, buy_button_image, confirm_button_image, purchase_count + 1, limit)
                return purchase_count
            else:
                logging.error(f"Confirm button {confirm_button_image} not found!")
        else:
            logging.error(f"Buy button {buy_button_image} not found!")
    return purchase_count

# Main loop
def auto_buy_bookmarks(purchase_limit):
    global running
    purchase_count = 0

    while purchase_count < purchase_limit and running:
        # Check for 'q' key press to stop the script
        if keyboard.is_pressed('q'):
            logging.info("Stopping the script...")
            running = False
            break

        # Attempt to purchase Mystic Bookmark
        purchase_count = attempt_purchase(mystic_bookmark_image, mystic_buy_button_image, mystic_confirm_button_image, purchase_count, purchase_limit)
        if purchase_count >= purchase_limit:
            break

        # Attempt to purchase Covenant Bookmark
        purchase_count = attempt_purchase(covenant_bookmark_image, covenant_buy_button_image, covenant_confirm_button_image, purchase_count, purchase_limit)
        if purchase_count >= purchase_limit:
            break

        # Scroll and attempt to purchase again
        logging.info("Bookmarks not found, scrolling and searching again...")
        scroll_shop()
        time.sleep(2)  # Added delay after scrolling to allow time for searching and purchasing
        purchase_count = attempt_purchase(mystic_bookmark_image, mystic_buy_button_image, mystic_confirm_button_image, purchase_count, purchase_limit)
        if purchase_count >= purchase_limit:
            break

        purchase_count = attempt_purchase(covenant_bookmark_image, covenant_buy_button_image, covenant_confirm_button_image, purchase_count, purchase_limit)
        if purchase_count >= purchase_limit:
            break

        # If still not found, refresh the shop
        logging.info("Bookmarks not found after scrolling, refreshing the shop...")
        random_clicks()  # Perform random clicks during the search process
        refresh_shop()

if __name__ == "__main__":
    purchase_limit = 10  # Set the number of purchases you want to make
    try:
        auto_buy_bookmarks(purchase_limit)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
