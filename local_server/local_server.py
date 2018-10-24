import requests as req
from subprocess import Popen
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#get selenium driver
def get_driver():
	Popen('taskkill /im chromedriver.exe /f')
	Popen('taskkill /im chrome.exe /f')
	time.sleep(3)
	options = webdriver.ChromeOptions() 
	options.add_argument("user-data-dir=C:\Users\gsiders\AppData\Local\Google\Chrome\User Data") 
	options.add_argument("--start-maximized") 
	driver = webdriver.Chrome("c:\dev\chromedriver.exe",chrome_options=options)
	return driver
def first_run(driver): 
	r = req.get("https://hotelcast.gsiders.app/command/")
	url = r.text
	local_url = open("command.txt", "w")
	local_url.write(url)
	local_url.close()

def second_run(driver):
	r = req.get("https://hotelcast.gsiders.app/command/")
	url = r.text
	command_file = open("command.txt", "r")
	local_command = command_file.read()
	command_file.close()
	url = url.strip("\n")
	if(url == local_command): 
		print "matches local url...will continue listeing"
		time.sleep(3)
		return second_run(driver)
	if(url == "pause"): 
		el = driver.find_element_by_class_name("nf-player-container")
		el.send_keys(Keys.RETURN)
		new_url = open("command.txt", "w")
		new_url.write(url)
		new_url.close()
		return second_run(driver)
	if(url == "play"): 
		el = driver.find_element_by_class_name("nf-player-container")
		el.send_keys(Keys.RETURN)
		new_url = open("command.txt", "w")
		new_url.write(url)
		new_url.close()
		return second_run(driver)
	if(url != local_command):
		print url
		print "doesn't match local url...opening url"
		driver.get(url)
		driver.fullscreen_window()
		new_url = open("command.txt", "w")
		new_url.write(url)
		new_url.close()
		second_run(driver)
driver = get_driver()
first_run(driver)
second_run(driver)