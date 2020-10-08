from selenium import webdriver

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://talent-is.smartschool.be/")

def login(user, pasw):
	user_form = driver.find_element_by_xpath('//*[@id="login_form__username"]')
	user_form.send_keys(user)
	pasw_form = driver.find_element_by_xpath('//*[@id="login_form__password"]')
	pasw_form.send_keys(pasw)
	login_button = driver.find_element_by_xpath('//*[@id="smscMain"]/div/div/div[2]/div/div[3]/form/button')
	login_button.click()
	driver.implicitly_wait(5)

def getTasks():
	# goto agenda
	goto = driver.find_element_by_xpath('//*[@id="smscTopContainer"]/nav/div[2]/button')
	goto.click()
	school_agenda = driver.find_element_by_xpath('//*[@id="shortcutsMenu"]/div/a[14]')
	school_agenda.click()
	# press dagweergave
	day_view = driver.find_element_by_xpath('//*[@id="dayView"]')
	day_view.click()
	# get tasks
	# return list with tupples


login("CyvrsAr", "dVKpfwz69gVprMeG")
getTasks()