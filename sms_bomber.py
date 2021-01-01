from selenium import webdriver
import time
import pyautogui
path="D:/Downloads/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
driver.get("http://google.com")
driver.maximize_window()
driver.get("https://www.flipkart.com/account/login?ret=/")
pyautogui.typewrite("8700391505")
forgot=driver.find_element_by_link_text("Forgot?")
forgot.click()
time.sleep(10)
resend=driver.find_element_by_link_text("Resend?")
resend.click()
for i in range(0,10):
  resend.click()
  time.sleep(10)
driver.quit()  
  