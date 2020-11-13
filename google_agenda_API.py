from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def login_google(driver, email, pasw):
        driver.get("https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Ad0ba58f3907446ec%2C10%3A1602440566%2C16%3A5e8fa0befc74fda1%2C0854e629b691884eaa22bc7bc4d1d9b3f4296853ac762b201e8e3403bbfa01f7%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22aef0a6b6f41e46f493cc26b144abd02e%22%7D&response_type=code&flowName=GeneralOAuthFlow")
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
        driver.get("https://calendar.google.com/calendar/u/0/r/agenda")
        time.sleep(3)

def add_task(driver, task, date, discr):
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/button/span[2]/div[2]')
        add_button.click()
        time.sleep(1)
        task_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/span/span')
        task_button.click()
        task_form = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
        task_form.send_keys(task)
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

def add_SB(driver, SB, date, discr):
        #add event
        add_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/button/span[2]/div[2]')
        add_button.click()
        time.sleep(1)
        #fill in date on task page
        task_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/span/span')
        task_button.click()                         
        date_form = driver.find_element_by_xpath('//*[@id="xStDaIn"]')
        date_form.send_keys(Keys.CONTROL + 'a')
        date_form.send_keys(Keys.BACKSPACE)
        date_form.send_keys(date)
        date_form.send_keys(Keys.ENTER)
        #set task to whole day
        whole_day = driver.find_element_by_xpath('//*[@id="tabTask"]/div/div[1]/div[2]/div[2]/label/div/div[2]')
        whole_day.click()
        #goto event (date is the same)
        event_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/span')
        event_button.click()
        time.sleep(1)
        #change the agenda you save in
        change_button = driver.find_element_by_xpath('//*[@id="tabEvent"]/div/div[7]/div[1]/div/div[2]/div/div/span/span/div[1]/div')
        change_button.click()
        time.sleep(1)
        change2_button = driver.find_element_by_xpath('//*[@id="xCalSel"]/div[1]/div[1]/div[2]')
        change2_button.click()
        time.sleep(1)
        for _ in range(2, 6): #look for agenda called SB's
                button = driver.find_element_by_xpath(f'//*[@id="xCalSel"]/div[1]/div[1]/div[2]')
                if button.get_attribute("innerHTML") == "SB's":
                        button.click() 
                        break                  

        SB_form = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/input')
        SB_form.send_keys(SB)
        time.sleep(1)
        #add a discription to event
        discr_button = driver.find_element_by_xpath('//*[@id="tabEvent"]/div/div[6]/div[1]/div/div[2]/div/div/span')
        discr_button.click()
        time.sleep(1)
        discr_form = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/span/div/div[1]/div[3]/div[1]/div[2]/div[2]/span[1]/div/div[6]/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]')
        discr_form.send_keys(discr)
        time.sleep(1)
        #save the event
        save_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div/div/div[2]/span/div/div[1]/div[3]/div[2]/div[2]/span')
        save_button.click()
        time.sleep(1)


def delete_event(driver, event_name, disc):
        events = driver.find_elements_by_xpath(f"//*[contains(text(), '{event_name}')]")
        for i in range (len(events)):
                events[i].click()
                e_disc = driver.find_element_by_id("xDetDlgDesc")
                if e_disc.text == f"Beschrijving:\n{disc}":
                        delete = driver.find_element_by_xpath("//div[@data-tooltip='Afspraak verwijderen']//*[name()='svg']")
                        delete.click()
                        break
                
