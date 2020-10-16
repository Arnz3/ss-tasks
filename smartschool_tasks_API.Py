from selenium import webdriver


def login(driver, user, pasw):
	driver.get("https://talent-is.smartschool.be/")
	user_form = driver.find_element_by_xpath('//*[@id="login_form__username"]')
	user_form.send_keys(user)
	pasw_form = driver.find_element_by_xpath('//*[@id="login_form__password"]')
	pasw_form.send_keys(pasw)
	login_button = driver.find_element_by_xpath('//*[@id="smscMain"]/div/div/div[2]/div/div[3]/form/button')
	login_button.click()
	driver.implicitly_wait(5)


def getTasks(driver):
	# goto agenda
	goto = driver.find_element_by_xpath('//*[@id="smscTopContainer"]/nav/div[2]/button')
	goto.click()
	school_agenda = driver.find_element_by_xpath('//*[@id="shortcutsMenu"]/div/a[14]')
	school_agenda.click()
	# press dagweergave
	day_view = driver.find_element_by_xpath('//*[@id="dayView"]')
	day_view.click()
	# get tasks
	busy_days = driver.find_elements_by_class_name("tasksAndMaterials__day")
	busy_days_text = []
	for day in busy_days:
		busy_days_text.append(day.text)

	return(busy_days_text)
	# return list with tupples


def convertTasks(task_list):
	vakken = {"TWM": "Mechanica", "FRA": "Frans", "WIS": "Wiskunde", "ENG": "Engels", "NED": "Nederlands", "TFYS": "Fysica", "GESCH": "Geschiedenis", "TCHEM": "Chemie", "EN": "engeneering", "LO": "Turnen", "TBIOL": "Biologie", "GOD": "Godsdienst", "TWE": "Eletriek", "AARD": "Aardrijkskunde"} 
	result = []
	task_type = None
	
	for i in range(len(task_list)):
		task_splits = task_list[i].split("\n")
		dag = task_splits[0]
		task_splits.pop(0)
		for i in range(round(len(task_splits)/2)):
			task = task_splits[0]
			disc = task_splits[1]
			#print(disc[0:disc.index(":")])

			if disc[0:disc.index(":")] == "Huistaak" or disc[0:disc.index(":")] == "Grote opdracht" or disc[0:disc.index(":")] =="Taak" :
				task_type = "Taak"

			else:
				task_type = "Toets"

			result.append((dag, task_type, vakken[str(task[4:].split(",")[0])], disc))
			task_splits.pop(0)
			task_splits.pop(0)
	return result
