from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def activate_board(name=""):
	driver = webdriver.Chrome()
	driver.get("http://ibbapp.jjrobots.com/?APPID=665D963BEC24BFB5")

	#set elem to the textbox on the screen
	elem = driver.find_element_by_name("TEXT")
	elem.clear()
	elem.send_keys("Proceed to Rice Hall " + name + "!")
	elem.send_keys(Keys.RETURN)

	send = driver.find_element_by_xpath("//input[@value='Send!']")
	send.click()

	#wait for a minute to let the users see the board
	time.sleep(60)

	#code to clear the screen
	clear = driver.find_element_by_xpath("//button[@class='btn btn-md btn-warning btn-block']")
	clear.click()
