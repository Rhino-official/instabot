from selenium import webdriver
import BotEngine

chromedriver_path = 'YOUR CHROMEDRIVER PATH' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

BotEngine.init(webdriver)
BotEngine.update(webdriver)

webdriver.close()
