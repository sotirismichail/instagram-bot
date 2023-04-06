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

def getRandomTime():
        randTime = randint(3, 5)
        return randTime

def loggin(bot_name,bot_pass):
    time.sleep(getRandomTime())
    browser.find_element(By.NAME,"username").send_keys(bot_name)
    browser.find_element(By.NAME,"password").send_keys(bot_pass)
	# Click on the facebook log-in button
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button"))).click();
	# Save your login info : no
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"))).click()
	# Turn off notifications
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))).click()
# def loggout():

def get_number_of_posts():
        """
        Returns number of post for an account or tag
        """
        try:
            num_of_posts = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="_ac2a"]'))).text
            num_of_posts = num_of_posts.replace(',','')
            return int(num_of_posts)
        except:
            return None


def click_first_post():
        """
        Clicks on the first post found for an account
        """
        try:
            #browser.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="v1Nh3 kIKUG _bz0w"]'))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_aagw"]'))).click()
            return True
        except:
            return False

def open_target(browser):
        """
        Opens the target account or hashtag
        """
        target="https://www.instagram.com/"+sys.argv[1]
        try:
            browser.get(target)
            # if unable to load the page
            if not self.is_page_loaded():
                logger.info("[open_target] Unable to load the page. Retrying...")
                time.sleep(1)
                return False

            # if not a valid account or tag
            elif not self.validate_target():
                return 'skip_retry'
        except:
            return False
        return True

def like():
        """
        Likes a post if not liked already
        """
        like_button:WebElement = None
        try:
            like_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="_aamw"]/button')))
            like_button_span = like_button.find_element(By.XPATH, 'div/span')
            button_status = like_button_span.find_element(By.TAG_NAME, 'svg').get_attribute('aria-label')
            # like only if not already liked
            if button_status == 'Like':
                like_button.click()

        except ElementClickInterceptedException:
            browser.execute_script('arguments[0].click();', like_button)         
        except:
            print("Error mate")

def next_post(browser): 
        """
        Moves to the next post
        """
        try:
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.RIGHT)
            return True
        except:
            return False






browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
# ======= Setting =============
# Your Facebook credentials
bot_username = "iordanispapavlou"
bot_password = "IpaP123"

# =============================
# Open the Website
browser.get('https://www.instagram.com/')
wait = WebDriverWait(browser, timeout=40)
wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Only allow essential cookies']"))).click()

# loggin in instagram
loggin(bot_username,bot_password);



# Make a like
open_target(browser)
click_first_post()
like()
time.sleep(getRandomTime())
next_post(browser)
like()

