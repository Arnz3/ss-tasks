from selenium import webdriver
from smartschool_tasks_API import *
from google_agenda_API import *

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_json(filename, new_data):
    with open(filename) as f:
        json.dump(new_data, f)

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

login(driver, "CyvrsAr", "dVKpfwz69gVprMeG")
lol = convertTasks(getTasks(driver))
print(lol)
login_google(driver, "matthiashenno2004", "Sissen1957")
print(len(lol))

for i in range(len(lol)):
    if 'Taak' in lol[i]:
        print('Taak')
        dag, taak, vak, discr = lol[i]
        print(lol[i])
        if taak +": " + vak in driver.page_source:
            print("skipped")
            print("-----------------------------")
        else:
            add_task(driver, taak +': '+ vak, dag,discr)
            print("done")
            print("-----------------------------")
                
    elif 'Toets' in lol[i]:
        print('SB/Toets:')
        dag, sb, vak, discr = lol[i]
        print(lol[i])
        if sb +": " + vak in driver.page_source:
            print("skipped")
            print("-----------------------------")
        else:
            add_SB(driver, sb +': '+ vak, dag,discr)
            print("done")
            print("-----------------------------")
            




