# import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import getpass
from time import sleep

# print("enter pass")
# myPassword = input()

# 0 - Default, 1 - Allow, 2 - Block
chrome_options = Options()
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1})
desired_cap = chrome_options.to_capabilities()
desired_cap.update({
  'browser_version': '75.0',
  'os': 'Windows',
  'os_version': '10'
})

loginPhone = input("INPUT | Facebook Username: ")
myPassword=getpass.getpass(prompt='INPUT | Facebook Password: ')
eventPage = input("INPUT | Link to event: ")

# PATH = 'C:\Users\Vincent Pham\Downloads\chromedriver_win32'
driver = webdriver.Chrome("chromedriver.exe", desired_capabilities=desired_cap)
driver.get("https://www.facebook.com/")
driver.maximize_window()

# loginPhone = "4088332530"

username = driver.find_element(By.XPATH,"//input[@type='text']")
username.send_keys(loginPhone)

password = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
password.send_keys(myPassword)

loginButton = driver.find_element(By.XPATH,"//button[@type='submit']")
loginButton.click()
# sleep(10)
# driver.find_element_by_xpath("//body/main[1]/p[3]/input[1]").click()
sleep(10)

driver.get(eventPage)
sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

openlist = driver.find_element(By.XPATH, '//div[@class="x1d52u69 x1pi30zi x1swvt13"]')
openlist.click()

sleep(2)
friendXPath = '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]'
friends = driver.find_elements(By.XPATH, friendXPath)
del friends[0:2]

print("Attendanees: ")
for f in friends:
    print(f.text)
sleep(2)
driver.quit()
done = input("\nEnter any key when done")


# myProfile = driver.find_element(By.XPATH,"//input[@aria-label='Search Facebook']")
# myProfile.click()
# myProfile.send_keys("San Jose Dragon Boat")

# groupClick = driver.find_element(By.XPATH,"//a[@href='https://www.facebook.com/groups/512390446516025/']")
# sleep(2)
# groupClick.click()


# sleep(3)
# driver.navigate("https://www.facebook.com/groups/512390446516025")

