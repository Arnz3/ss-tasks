from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Ad0ba58f3907446ec%2C10%3A1602440566%2C16%3A5e8fa0befc74fda1%2C0854e629b691884eaa22bc7bc4d1d9b3f4296853ac762b201e8e3403bbfa01f7%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22aef0a6b6f41e46f493cc26b144abd02e%22%7D&response_type=code&flowName=GeneralOAuthFlow")

def login_google(email, pasw):
	email_form = driver.find_element_by_xpath('//*[@id="identifierId"]')
	email_form.send_keys(email)
	next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
	next_button.click()
	time.sleep(2)
	pasw_form = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
	pasw_form.send_keys(pasw)
	login_button = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
	login_button.click()
	driver.implicitly_wait(5)
	time.sleep(2)

def add_task(task, date, discr):
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/button/span[2]/div[2]')
        add_button.click()
        time.sleep(1)
        task_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/span/span')
        task_button.click()
        task_form = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
        task_form.send_keys('Taak: ' + task)
        time.sleep(1)
        date_form = driver.find_element_by_xpath('//*[@id="xStDaIn"]')
        date_form.send_keys(Keys.CONTROL + 'a')
        date_form.send_keys(Keys.BACKSPACE)
        date_form.send_keys(date)
        date_form.send_keys(Keys.ENTER)
        time.sleep(1)
        day_button = driver.find_element_by_xpath('//*[@id="tabTask"]/div/div[1]/div[2]/div[2]/label/div/div[2]')
        day_button.click()
        discr_form = driver.find_element_by_xpath('//*[@id="tabTask"]/div/div[2]/div[2]/div/label/div[2]/textarea')
        discr_form.send_keys(discr)
        save_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[2]/span/span')
        save_button.click()
        time.sleep(1)

def add_SB(SB, date, discr):
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/button/span[2]/div[2]')
        add_button.click()
        time.sleep(1)
        change_button = driver.find_element_by_xpath('//*[@id="tabEvent"]/div/div[7]/div[1]/div/div[2]/div/div/span/span/div[1]/div')
        change_button.click()
        time.sleep(1)
        change2_button = driver.find_element_by_xpath('//*[@id="xCalSel"]/div[1]/div[1]/div[1]/span/div/div')
        change2_button.click()
        time.sleep(1)
        SB_button = driver.find_element_by_xpath('//*[@id="xCalSel"]/div[2]/div[2]/span/div')
        SB_button.click()
        time.sleep(1)
        SB_form = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
        SB_form.send_keys(SB)
        time.sleep(1)
        #date_form = driver.find_element_by_xpath('//*[@id="tabEvent"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div/span/span/div[1]/span/span')
        
        
        #date_form.send_keys(date)
        #date_form.send_keys(Keys.ENTER)
        #time.sleep(1)
        discr_button = driver.find_element_by_xpath('//*[@id="tabEvent"]/div/div[6]/div[1]/div/div[2]/div/div/span')
        discr_button.click()
        discr_form = driver.find_element_by_xpath('//*[@id="c1991"]/div/div[2]/div[2]/div/div[2]/div/span/span')
        discr_form.send_keys(discr)
        time.sleep(1)
        
        
login_google("matthiashenno2004", "Sissen1957")
driver.get("https://calendar.google.com/calendar/u/0/r/agenda")
time.sleep(3)
add_task("test","22 10 20", "Dit is een test")
add_SB("test", "22 10 20", "Dit is een test")
