import time 
from selenium import webdriver	# needed to access the browser and play with it 
from selenium.webdriver.common.keys import Keys # allows selenium to use the keyboard 

class LincolnIngram():
	def __init__(self, username, password):
		self.browser=webdriver.Chrome("./chromedriver")
		self.username = username
		self.password = password

	def login(self):
		self.browser.get("https://twitter.com/explore")
		time.sleep(5) 	# just like a real boy 
		self.browser.find_element_by_name("session[username_or_email]").send_keys(self.username)
		time.sleep(5)
		self.browser.find_element_by_name("session[password]").send_keys(self.password).send_keys(Keys.ENTER)

	def tweet(self, text):
		time.sleep(5)
		tweet_box = self.browser.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                  /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                  /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                  /div/div/div''')
		tweet_box.send_keys(text)
		tweet_box.send_keys(Keys.COMMAND, Keys.ENTER)
		


