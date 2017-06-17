from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def initdrivers():
	driver = webdriver.Chrome()
	return driver

def main():
	d = initdrivers()
	d.get("https://web.whatsapp.com")
	print("Open target chat..")
	time.sleep(20)
	Available = False
	while (not Available):
		try:
			textarea = d.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')	
			Available = True
		except:
			print("Chat not found :( Waiting..")
			time.sleep(5)
			pass
		
	print("Text area found!")

	txt = input("What you want to send?\n>> ")
	n = int(input("How many times?\n>> "))


	for i in range(n):
		textarea.send_keys(txt)
		time.sleep(1)
		textarea.send_keys(Keys.RETURN)	
		print(i)
		
	print("Done")
	a = input()
if __name__ == "__main__":
	main()
