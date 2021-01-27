import re
import os
import sys
from datetime import datetime
from selenium import webdriver

base_url = "https://moodle.cpce-polyu.edu.hk/"
account = ""
password = ""
browser = "chrome" # edge or chrome

if account == "" or password == "":
    sys.exit("Credentials are not inputted.")

dirname = os.path.dirname(__file__)
if browser == "chrome":
    from selenium.webdriver.chrome.options import Options
    webdriver_path = os.path.join(dirname, 'chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("-incognito")
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(webdriver_path, options = options)
elif browser == "edge":
    from msedge.selenium_tools import Edge, EdgeOptions
    webdriver_path = os.path.join(dirname, 'msedgedriver.exe')
    options = EdgeOptions()
    options.use_chromium = True
    options.page_load_strategy = 'eager'
    options.add_argument("-inprivate")
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    driver = Edge(webdriver_path, options = options)
else:
    print("Invaild browser.")

def login():
    driver.get(base_url)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$UsernameTextBox").send_keys(account)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$PasswordTextBox").send_keys(password)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$SubmitButton").click()
    get_attendance()

def get_attendance():
    today = datetime.today()
    timestamp = str(int(datetime(int(today.strftime("%Y")), int(today.strftime("%m")), int(today.strftime("%d"))).timestamp()))
    driver.get(base_url + "calendar/view.php?view=day&time=" + timestamp)
    get_calendar_link = driver.find_elements_by_link_text("Go to activity")
    get_attendance.link = []
    attendance_pattern = re.compile(base_url + "mod/attendance/")
    for a in get_calendar_link:
        if attendance_pattern.match(a.get_attribute('href')) != None:
            print("Attendance link found: " + a.get_attribute('href'))
            get_attendance.link.append(a.get_attribute('href'))
    print("Total link found: " + str(len(get_attendance.link)) + "\n")
    take_attendance()

def take_attendance():
    for a in get_attendance.link:
        driver.get(a)
        current_title = driver.find_element_by_class_name("page-header-headings").text
        if len(driver.find_elements_by_link_text("Submit attendance")):
            driver.find_element_by_link_text("Submit attendance").click()
            driver.find_element_by_name("status").click()
            driver.find_element_by_name("submitbutton").click()
            print("Taked attendance: " + current_title)
        else:
            print("NOT taked attendance: " + current_title)
    driver.quit()

login()
