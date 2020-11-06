from selenium import webdriver
from smartschool_tasks_API import *
from google_agenda_API import *
import json

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_json(filename, new_data):
    with open(filename, "w") as f:
        json.dump(new_data, f)

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

data = read_json("test.json")

login(driver, "CyvrsAr", "dVKpfwz69gVprMeG")
ss_data = convertTasks(getTasks(driver))
login_google(driver, "cuyversarno", "kerkStraat35")

for i in range(len(ss_data)):
    if 'Taak' in ss_data[i] and ss_data[i] not in data:
        dag, taak, vak, discr = ss_data[i]
        print(ss_data[i])
        print(data)
        for p in range(len(data)):
            print(data[p])
            if taak == data[p][1] and vak == data[p][2]:
                if dag != data[p][0] or discr != data[p][3]:
                    print("skipped")
            else:
                add_task(driver, taak +': '+ vak, dag,discr)
                print("added")
                break

    elif 'Toets' in ss_data[i] and ss_data[i] not in data:
        print('SB/Toets:')
        dag, sb, vak, discr = ss_data[i]
        print(ss_data[i])
        print(data)
        for p in range(len(data)):
            print(data[p])
            if sb == data[p][1] and vak == data[p][2]:
                if dag != data[p][0] or discr != data[p][3]:
                    print("skipped")
            else:
                add_SB(driver, sb +': '+ vak, dag,discr)
                print("add")
                print("-----------------------------")
                break

    else: 
        print("error")

write_json("test.json", ss_data)
