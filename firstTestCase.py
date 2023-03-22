import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--incognito")
#from selenium.webdriver.support import expected_conditions as EC


path = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\\shyam\\Downloads\\chromedriver_win32(1)\\chromedriver.exe")

path.get("https://this-person-does-not-exist.com/en")
path.maximize_window()
def close_tabs():
    # Get the handle of the current window
    current_handle = path.current_window_handle

    # Get a list of all open window handles
    handles = path.window_handles

    # Loop through the window handles
    for handle in handles:
        # Switch to the window
        path.switch_to.window(handle)

        # If the window is not the current one, close it
        if handle != current_handle:
            path.close()

    # Switch back to the current window
    path.switch_to.window(current_handle)


def image_download():
    path.find_element(By.ID,'oldButtonDownload').click()
    path.switch_to.window(path.window_handles[1])
    time.sleep(2)
    path.find_element(By.CLASS_NAME,'download-page-avatar').click()
    time.sleep(35)
#    path.close()
    path.switch_to.window(path.window_handles[1])
    path.get("https://this-person-does-not-exist.com/en")
    time.sleep(5)
    close_tabs()

n = 2
for i in range(n):
    image_download()

print("Done")