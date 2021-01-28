import re
import os
import sys
import time
from datetime import datetime
from selenium import webdriver

base_url = "https://moodle.cpce-polyu.edu.hk/"
account = ""
password = ""
browser = "chrome" # edge or chrome

if account == "" or password == "":
    sys.exit("Credentials not inputted")

dirname = os.path.dirname(__file__)
if browser == "chrome":
    from selenium.webdriver.chrome.options import Options
    webdriver_path = os.path.join(dirname, 'chromedriver.exe')
    if os.path.isfile(webdriver_path) != True:
        sys.exit("chromedriver.exe not found")
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("-incognito")
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(webdriver_path, options = options)
elif browser == "edge":
    from msedge.selenium_tools import Edge, EdgeOptions
    webdriver_path = os.path.join(dirname, 'msedgedriver.exe')
    if os.path.isfile(webdriver_path) != True:
        sys.exit("msedgedriver.exe not found")
    options = EdgeOptions()
    options.use_chromium = True
    options.page_load_strategy = 'eager'
    options.add_argument("-inprivate")
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    driver = Edge(webdriver_path, options = options)
else:
    sys.exit("Invaild browser")

today = datetime.today()
year, month, day = int(today.strftime("%Y")), int(today.strftime("%m")), int(today.strftime("%d"))

def login():
    driver.get(base_url)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$UsernameTextBox").send_keys(account)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$PasswordTextBox").send_keys(password)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$SubmitButton").click()
    error = driver.find_elements_by_id('ctl00_ContentPlaceHolder1_ErrorTextLabel')
    if len(error):
        print("Login failed (" + re.sub("\n(.*)", "", error[0].text) + ")")
        driver.quit()
        sys.exit()
    print("\nLogged in as " + account)
    get_attendance()

def get_attendance():
    today_timestamp = str(int(datetime(year, month, day).timestamp()))
    driver.get(base_url + "calendar/view.php?view=day&time=" + today_timestamp)
    activity_link = driver.find_elements_by_link_text("Go to activity")
    activity_time = driver.find_elements_by_xpath("//span[@class='date pull-xs-right m-r-1']")
    get_attendance.link = []
    get_attendance.time = []
    attendance_pattern = re.compile(base_url + "mod/attendance/")
    for i in range(len(activity_link)):
        if attendance_pattern.match(activity_link[i].get_attribute('href')) != None:
            get_attendance.link.append(activity_link[i].get_attribute('href'))
            get_attendance.time.append(activity_time[i].text)
    print("Lessons with attendance link available: " + str(len(get_attendance.link)))
    take_attendance()

def check_time(i):
    attendance_time = get_attendance.time[i].replace(":", " ").split()
    if attendance_time[3] == "PM" and attendance_time[1] != "12":
        start_hour = int(attendance_time[1]) + 12
    elif attendance_time[3] == "AM" and attendance_time[1] == "12":
        start_hour = 0
    else:
        start_hour = int(attendance_time[1])
    start_min = int(attendance_time[2])
    start_timestamp = datetime(year, month, day, start_hour, start_min).timestamp()
    if attendance_time[7] == "PM" and attendance_time[5] != "12":
        end_hour = int(attendance_time[5]) + 12
    elif attendance_time[7] == "AM" and attendance_time[5] == "12":
        start_hour = 0
    else:
        end_hour = int(attendance_time[5])
    end_min = int(attendance_time[6])
    end_timestamp = datetime(year, month, day, end_hour, end_min).timestamp()
    current_timestamp = time.time()
    if current_timestamp >= start_timestamp and current_timestamp < end_timestamp:
        return True
    else:
        return False

def take_attendance():
    not_visited = []
    for i in range(len(get_attendance.link)):
        if check_time(i) == True:
            driver.get(get_attendance.link[i])
            current_title = driver.find_element_by_class_name("page-header-headings").text
            print("\nTaking attendance of " + current_title)
            if len(driver.find_elements_by_link_text("Submit attendance")):
                driver.find_element_by_link_text("Submit attendance").click()
                driver.find_element_by_name("status").click()
                driver.find_element_by_name("submitbutton").click()
                print("Done at " + datetime.now().strftime("%H:%M:%S"))
            else:
                print("Failed. Maybe you have already taken the attendance or there are some errors.")
        else:
            not_visited.append(get_attendance.link[i])
    if len(not_visited):
        print("\nNot visited as it is not in designated period of time now:")
    for link in not_visited:
        print(link)
    driver.quit()
    sys.exit()

login()