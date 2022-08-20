#cookie clicker game automation

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, )
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3228593221&f_AL=true&f_E=1&f_JT=I&f_TPR=r604800&geoId=102713980&keywords=python%20intern&location=India&refresh=true')



log_email = "xxxxxxx@gmail.com" #yourEmail
passw = "XXXXXX" #yourPassword
phNo= "9087xxxxxx" #your number

#auto sign in/Authentication
sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

username = driver.find_element(By.ID, "username")
username.send_keys(log_email)

password = driver.find_element(By.ID, "password")
password.send_keys(passw)

signupButton = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
signupButton.click()

#Get first Job and apply
Easy_apply = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button/span")
Easy_apply.click()

#fill phonenumber
phone = driver.find_element(By.CSS_SELECTOR, ".display-flex input")
phone.send_keys(phNo)

#press Submit
submit = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end span")
submit.click()



time.sleep(100)
driver.quit()


#Note : program can be looped to fill multiple forms