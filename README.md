# Epic7AutoRefreshShop
Epic7 Auto refresh shop for covenant and mystic bookmarks.

Epic7AutoShopCompletedv2.1.py script
Made from and used on Spyder (Python 3.11), should work for other Python IDEs.
*Anaconda Navigator is my Python Workstation, https://www.anaconda.com/download*

Code made in 1920/1080 resolution setting display and Bluestacks Settings 1920/1080 resolution maximized window.
Code should work for any type of resolution or emulator as long the image is recognizable.

Pip install the following:
 pip install pyautogui 
 pip install opencv-python-headless 
 pip install numpy 
 pip install keyboard

Create a new folder and download/save Epic7AutoShopCompletedv2.1.py script to the Folder.
Make sure Python IDEs reads from the same new folder and contents inside, otherwise it may fail to locate or recogonize images.

Provide your own screenshot of the following images for more accuracy.*Snipping Tool or Snip & Sketch*
Use downloaded images as guidelines to your own screenshot as it may not recognize my screenshots to your own.
Overwrite images with your own to simplify process, as the name is already set.
List below shows how each image will be recognized in the script.

# Load images
mystic_bookmark_image = cv2.imread('mystic_bookmark.png')
covenant_bookmark_image = cv2.imread('covenant_bookmark.png')
mystic_buy_button_image = cv2.imread('mystic_buy_button.png')
covenant_buy_button_image = cv2.imread('covenant_buy_button.png')
mystic_confirm_button_image = cv2.imread('mystic_confirm_button.png')
covenant_confirm_button_image = cv2.imread('covenant_confirm_button.png')
refresh_button_image = cv2.imread('refresh_button.png')
refresh_confirm_button_image = cv2.imread('refresh_confirm_button.png')

*IMPORTANT: All screenshot images should be in the same resolution and window size*

How the script should work:
Attempt to purchase Mystic Bookmark
Attempt to purchase Covenant Bookmark
Scroll down and attempt to purchase again
If still not found, refresh the shop
If found it will purchase, refresh the shop.
Random clicks to simulate human interactions, to avoid potential detection.
