import os
import time


def take_screenshot(driver, name):
    screenshot_directory = "screenshots/"
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)
    name += time.strftime("-%Y-%m-%d_%H-%M-%S", time.localtime())
    name += ".png"
    name = name.replace(" ", "_")
    driver.get_screenshot_as_file(f"{screenshot_directory}{name}")
