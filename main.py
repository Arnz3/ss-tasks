from selenium import webdriver
from smartschool_tasks_API import *

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

login(driver, "CyvrsAr", "dVKpfwz69gVprMeG")
lol = convertTasks(getTasks(driver))
print(lol)

