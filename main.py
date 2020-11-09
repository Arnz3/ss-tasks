from selenium import webdriver
from smartschool_tasks_API import *
from google_agenda_API import *
import json

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def write_json(filename, new_data):
    with open(filename, "w") as f:
        json.dump(new_data, f, sort_keys=True, indent=4)

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

data = read_json("test.json")

login(driver, "CyvrsAr", "dVKpfwz69gVprMeG")
ss_data = convertTasks(getTasks(driver))
login_google(driver, "cuyversarno", "kerkStraat35")


# if ss_data is not None:
#     for i in range(len(ss_data)):
#         print(ss_data[i])
#         if 'Taak' in ss_data[i] and ss_data[i] not in data:
#             dag, taak, vak, discr = ss_data[i]
#             print(ss_data[i])
#             print(data)
#             for p in range(len(data)):
#                 print(data[p])
#                 if taak == data[p][1] and vak == data[p][2] and dag == data[p][0]:
#                     print("skipped")
#                     break

#                 elif taak == data[p][1] and vak == data[p][2] and discr == data[p][3]:
#                     print("skipped")
#                     break

#                 elif p == len(data):
#                     add_SB(driver, taak +': '+ vak, dag,discr)
#                     print("add")
#                     print("-----------------------------")
#                     break

#         elif 'Toets' in ss_data[i] and ss_data[i] not in data:
#             print('SB/Toets:')
#             dag, sb, vak, discr = ss_data[i]
#             print(sb)
#             for p in range(len(data)):
#                 print(data[p])
#                 if sb == data[p][1] and vak == data[p][2] and dag == data[p][0]:
#                     print("skipped")
#                     break

#                 elif sb == data[p][1] and vak == data[p][2] and discr == data[p][3]:
#                     print("skipped")
#                     break

#                 elif p == len(data):
#                     add_SB(driver, sb +': '+ vak, dag,discr)
#                     print("add")
#                     print("-----------------------------")
#                     break

#         else: 
#             print("already")


write_json("test.json", ss_data)

if ss_data is not None:
    for j in range(len(data)):
        if data[j] not in ss_data:
            delete_event(driver, data[j][1] +": "+ data[j][2], data[j][3])

    for i in range(len(ss_data)):
        if ss_data[i] not in data:
            if "Taak" in ss_data[i]:
                add_task(driver, ss_data[i][1] +": "+ ss_data[i][2], ss_data[i][0], ss_data[i][3])
            elif "Toets" in ss_data[i]:
                add_SB(driver, ss_data[i][1] +": "+ ss_data[i][2], ss_data[i][0], ss_data[i][3])
            else:
                print("error")  
    

write_json("test.json", ss_data)
driver.quit()
print("DONE")

