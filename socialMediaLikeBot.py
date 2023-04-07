import time
import sys
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement


def getRandomTime() -> int:
    randTime = randint(3, 5)
    return randTime


def login(bot_name: str, bot_pass: str) -> None:
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(
        bot_name
    )
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(
        bot_pass
    )
    # Click on the facebook log-in button
    button = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button",
            )
        )
    )
    browser.execute_script("arguments[0].click();", button)
    # Save your login info : no
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div",
            )
        )
    ).click()
    # Turn off notifications
    wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]",
            )
        )
    ).click()


# def logout():


def get_number_of_posts() -> int:
    """
    Returns number of post for an account or tag
    """
    try:
        num_of_posts = wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="_ac2a"]'))
        ).text
        num_of_posts = num_of_posts.replace(",", "")
        return int(num_of_posts)
    except:
        return None


def click_first_post() -> bool:
    """
    Clicks on the first post found for an account
    """
    try:
        # browser.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="v1Nh3 kIKUG _bz0w"]'))).click()
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_aagw"]'))
        ).click()
        return True
    except:
        return False


def open_target(browser: object, targetName: str) -> bool:
    """
    Opens the target account or hashtag
    """
    target = "https://www.instagram.com/" + targetName
    try:
        browser.get(target)
        # if unable to load the page
        if not self.is_page_loaded():
            logger.info("[open_target] Unable to load the page. Retrying...")
            time.sleep(1)
            return False

        # if not a valid account or tag
        elif not self.validate_target():
            return "skip_retry"
    except:
        return False
    return True


def like() -> None:
    """
    Likes a post if not liked already
    """
    like_button: WebElement = None
    try:
        like_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="_aamw"]/button'))
        )
        like_button_span = like_button.find_element(By.XPATH, "div/span")
        button_status = like_button_span.find_element(By.TAG_NAME, "svg").get_attribute(
            "aria-label"
        )
        # like only if not already liked
        if button_status == "Like":
            like_button.click()

    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", like_button)
    except:
        print("ERROR: Failed to perform like")


def next_post(browser: object) -> bool:
    """
    Moves to the next post
    """
    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).send_keys(
            Keys.RIGHT
        )
        return True
    except:
        return False


## Starting the Bot


browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
# ======= Setting =============
# Your Facebook credentials
bot_username = sys.argv[1]  # "iordanispapavlou"
bot_password = sys.argv[2]  # "IpaP123"
targetName = sys.argv[3]
numberOfPosts = int(sys.argv[4])

# =============================
# Open the Website
browser.get("https://www.instagram.com/")
wait = WebDriverWait(browser, timeout=50)
wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[text()='Only allow essential cookies']")
    )
).click()

# Log into instagram
login(bot_username, bot_password)

# Perform a like
open_target(browser, targetName)
maxPosts = get_number_of_posts()

if maxPosts < numberOfPosts:
    numberOfPosts = maxPosts

if numberOfPosts != 0:
    click_first_post()
    like()

    for x in range(numberOfPosts - 1):
        next_post(browser)
        like()
