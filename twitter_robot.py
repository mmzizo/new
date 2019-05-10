from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import getpass
print("please enter login info:----\n")
username = input("enter you username::\t")
passwd = getpass.getpass('Enter password ::\t')

# start chrome driver headless
options = Options()
options.headless = True
driver = webdriver.Chrome(path-to-chrome-webdriver,chrome_options = options)
driver.implicitly_wait(20)
# login to twitter account
driver.get("https://twitter.com/login")
driver.implicitly_wait(20)
driver.find_element_by_class_name("js-username-field ").send_keys(username)
#getpass.getpass('Enter password \t')
pass_field = driver.find_element_by_class_name("js-password-field")
pass_field.send_keys(passwd)
pass_field.send_keys(Keys.RETURN)

#get info using bs4
def flrlst(usertoget):
    driver.get('https://twitter.com/'+usertoget+'/followers')
    driver.implicitly_wait(20)
######infinity scroll
    loopCounter = 0
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        if loopCounter > 499:
            break;  # if the account follows a ton of people, its probably a bot, cut it off
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        loopCounter = loopCounter + 1
    pagesrc = driver.page_source
    soup = bs(pagesrc, "lxml")
    username = []
    for users in soup.find_all("b", class_="u-linkComplex-target"):
        username.append(users.text)
    return username

def flglst(usertoget):
    driver.get('https://twitter.com/'+usertoget+'/following')
    driver.implicitly_wait(20)
######infinity scroll
    loopCounter = 0
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        if loopCounter > 499:
            break;  # if the account follows a ton of people, its probably a bot, cut it off
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        loopCounter = loopCounter + 1
    pagesrc = driver.page_source
    soup = bs(pagesrc, "lxml")
    username = []
    for users in soup.find_all("b", class_="u-linkComplex-target"):
        username.append(users.text)
    return username

# follow user name
def followuser(userN):
    driver.get('https://twitter.com/'+userN)
    driver.implicitly_wait(10)
    print("now following"+userN)
    fbutton = driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[6]/div/div/span[2]/button[1]')
    fbutton.click()

# unfollow username
def unfollowuser(userN):
    driver.get('https://twitter.com/'+userN)
    driver.implicitly_wait(10)
    print ("now UNfollowing "+userN)
    fbutton = driver.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[6]/div/div/span[2]/button[2]')
    fbutton.click()

#get my user followers
myusers = []
nonflrlst = []
myusers = flrlst(username)
nonflrlst = flglst(username)
for person in nonflrlst:
    if person in myusers:
        nonflrlst.remove(person)
nonflrlst.pop(0)
nom = 0
for tp in nonflrlst:
        try:
            unfollowuser(tp)
        except NoSuchElementException:
            driver.implicitly_wait(10)

print(nom)

ddd = input('press key to continue')
driver.close()
