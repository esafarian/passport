import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from email.message import EmailMessage



def questionnaire():
	PATH = "C:\Program Files (x86)\chromedriver.exe"

	options = webdriver.ChromeOptions() 
	options.add_argument("start-maximized")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option('useAutomationExtension', False)


	driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')

	driver.get("https://passportappointment.travel.state.gov/")
#click first option
	driver.find_element_by_id("rb-home-list-new").click()
#click next button
	driver.find_element_by_id("btnHomeNext").click()
#click yes to travel plans
	driver.find_element_by_id("InternationalTravel-yes").click()
#input travel date
	driver.find_element_by_id("DateTravel").send_keys("05/29/2021")
#click no visa needed
	driver.find_element_by_id("VisaNeeded-no").click()
#select how many household members need passport
	driver.find_element_by_xpath('//button[text()="2"]').click()
	
#complete captcha
	WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
#probably broken so just wait for me to do captcha
	time.sleep(45)
	findApp(driver.current_url)


# once on map page
def findApp():
	
	none = driver.find_element_by_xpath('//button[text()="OK"]')
	
#if 0 appointment dialog box pops up, refresh and check again
	while none.is_Displayed():
		none.click()
		driver.refresh()
		
#if dialog box doesnt show up, send notification that there are available appointments
		
	sendEmail("Passport appointment found!","Appointment found, book now!!!! \nhttps://passportappointment.travel.state.gov/","cupquake2@aol.com")


#email notif
def sendEmail(subject, body, to):
	msg = EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to


	user = "lezaalert@gmail.com"
	password = "izbfhjocqhhqgdae"
	msg['from'] = user

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(user,password)

	server.send_message(msg)



options= webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe",chrome_options=options
	findApp()

# check for session expiry
#expire = driver.find_element_class_name("validation-summary-errors validator-error")
#if expire.is_Displayed
	#questionnaire()
	#email("session expired","","cupquake2@aol.com")
