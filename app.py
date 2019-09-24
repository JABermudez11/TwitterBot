from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)       # waits 3 secs to load the game
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')

        #clears before entering anything
        email.clear()
        password.clear()

        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)     # presses enter key to login
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_element_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:                  # gets all the links
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_name('HeartAnimation').click() # liking the tweet
                    time.sleep(10)      # waiting so spam is not detected
                except Exception as ex:
                    time.sleep(60)

jbot = TwitterBot('', '')
jbot.login()
jbot.like_tweet('webdevelopment') #the hashtag
