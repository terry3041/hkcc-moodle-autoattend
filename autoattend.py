import re
import os
import sys
import time
from datetime import datetime
from selenium import webdriver
from discord_webhook import DiscordWebhook, DiscordEmbed

base_url = "https://moodle.cpce-polyu.edu.hk/"
account = ""
password = ""
webdriver_port = "4444"
discord_webhook_url = ""

if account == "" or password == "":
    sys.exit("Credentials not inputted")

today = datetime.today()
year, month, day = int(today.strftime("%Y")), int(today.strftime("%m")), int(today.strftime("%d"))
webhook = DiscordWebhook(url=discord_webhook_url)
capabilities = webdriver.DesiredCapabilities.HTMLUNITWITHJS
capabilities.update({'page_load_strategy' : 'eager'})
driver = webdriver.Remote("http://localhost:" + webdriver_port +"/wd/hub", desired_capabilities = capabilities)

def login():
    driver.get(base_url)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$UsernameTextBox").send_keys(account)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$PasswordTextBox").send_keys(password)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$SubmitButton").click()
    error = driver.find_elements_by_id('ctl00_ContentPlaceHolder1_ErrorTextLabel')
    if len(error):
        reason = re.sub("\n(.*)", "", error[0].text)
        print("Login failed (" + reason + ")")
        message = "❌ | 無法登入為 " + account + " (" + reason + ")"
        embed = DiscordEmbed(description=message, color=14495300)
        webhook.add_embed(embed)
        webhook.execute()
        driver.quit()
        sys.exit()
    driver.execute_script("window.setTimeout('document.forms[0].submit()', 0);")
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
                message = "✅ | 已為 " + current_title + " 點名"
                embed = DiscordEmbed(description=message, color=7844437)
            else:
                print("Failed. Maybe you have already taken the attendance or there are some errors.")
                message = "❌ | 未能為 " + current_title + " 點名"
                embed = DiscordEmbed(description=message, color=14495300)
            webhook.add_embed(embed)
            webhook.execute()
        else:
            not_visited.append(get_attendance.link[i])
    if len(not_visited):
        print("\nNot visited as it is not in designated period of time now:")
    for link in not_visited:
        print(link)
    driver.quit()
    sys.exit()

login()
