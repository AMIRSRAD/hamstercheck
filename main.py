import time
import pyautogui
import logging
import random

# Path to your emulator executable

logging.basicConfig(filename='telegram_script.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


# Function to open the emulator


# Function to find and click on Telegram app
def find_and_open_telegram():
    try:
        # Locate the Telegram icon and click it with a confidence level
        telegram_icon_location = pyautogui.locateCenterOnScreen('source/telegram_icon.png', confidence=0.8)
        if telegram_icon_location:
            pyautogui.click(telegram_icon_location)
            time.sleep(10)  # wait for Telegram to open
        else:
            print("Telegram icon not found on screen")
    except pyautogui.ImageNotFoundException:
        print("Telegram icon not found on screen")


# Function to search for a specific chat and open it
def search_and_open_chat(chat_name_image):
    try:
        search_icon_location = pyautogui.locateCenterOnScreen('search_icon.png',
                                                              confidence=0.8)  # Image of the search icon
        if search_icon_location:
            pyautogui.click(search_icon_location)
            time.sleep(2)
            pyautogui.write(chat_name_image)
            time.sleep(2)

            chat_position_location = pyautogui.locateCenterOnScreen(chat_name_image,
                                                                    confidence=0.8)  # Image of the chat name
            if chat_position_location:
                pyautogui.click(chat_position_location)
                time.sleep(2)
            else:
                print(f"Chat image '{chat_name_image}' not found on screen")
        else:
            print("Search icon not found on screen")
    except pyautogui.ImageNotFoundException:
        print(f"Search icon or chat image '{chat_name_image}' not found on screen")


# Function to click something in the chat
def click_in_chat(element_image):
    try:
        element_position_location = pyautogui.locateCenterOnScreen(element_image,
                                                                   confidence=0.8)  # Image of the element to click
        if element_position_location:
            pyautogui.click(element_position_location)
            time.sleep(2)
        else:
            print(f"Element image '{element_image}' not found on screen")
    except pyautogui.ImageNotFoundException:
        print(f"Element image '{element_image}' not found on screen")

def reset():
    pyautogui.press("esc")


def main():
    tel_found = False;
    while(tel_found == False):
        try:
            find_and_open_telegram()
        except:
            tel_found = False
            continue
        tel_found = True

    time.sleep(50) # huge delay

    process = True;
    while(process):
        try:
            click_in_chat("source/search.png")  # Provide the image file for the element to click
        except:
            print("error")
            reset()
            time.sleep(1)
            reset()
            continue

        time.sleep(10)

        try:
            click_in_chat("source/hamster_icon.png")  # Provide the image file for the element to click
        except:
            print("error")
            reset()
            continue

        time.sleep(10)

        try:
            click_in_chat("source/play_icon.png")  # Provide the image file for the element to click
        except:
            print("error")
            reset()
            continue

        time.sleep(10)

        try:
            click_in_chat("source/start_icon.png")  # Provide the image file for the element to click
        except:
            print("no start")

        time.sleep(30)

        try:
            click_in_chat("source/claim_icon.png")  # Provide the image file for the element to click
        except:
            print("error")
            reset()
            reset()
            continue

        process = False
    time.sleep(10)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)



if __name__ == "__main__":
    while True:
        main()
        logging.info("Script completed. Waiting for 5 minutes before the next run.")
        random_number = random.randint(9000, 11000)
        time.sleep(random_number)  # Wait for 5 minutes (300 seconds)
        pyautogui.moveRel(0, 1)  # Move the mouse by 1 pixel
        pyautogui.moveRel(0, -1)  # Move it back to the original position
        time.sleep(2)
