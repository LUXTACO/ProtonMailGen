import time
import random
import requests
import pyautogui
import pyautogui
import configparser
from pynput.keyboard import Key, Controller
from pystyle import Colorate, Colors, Center

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import undetected_chromedriver as uc

# Variables

fail = False
miss = 0
hits = 0
amount = 0
proxychoice = 0
keyboard = Controller()
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"

# Functions

def normal_namegen():
    names = ["Emma", "Liam", "Sophia", "Noah", "Ava", "Oliver", "Mia", "Elijah", "Charlotte", "Lucas", "Amelia", "Ethan", "Harper", "Aiden", "Evelyn", "Jackson", "Abigail", "Logan", "Emily", "Mason", "Elizabeth", "Caden", "Isabella", "Grayson", "Madison", "Levi", "Sofia", "Owen", "Scarlett", "Caleb"]
    lastnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes"]
    
    result = random.choice(names) + random.choice(lastnames) + str(random.randint(1000, 9999))
    
    return result

def gamer_namegen():
    preffix = ['Swag', 'Dank', 'Lit', 'Savage', 'Crazy']
    names = ['Lil', 'Big', 'Young', 'Old', 'Dope', 'Savage', 'Crazy', 'Swag', 'Dank', 'Lit', 'Savage', 'Crazy', 'Bruh', 'Brah', 'Breh', 'Broski', 'Bro', 'Brother']
    suffix = ['Best', 'Ratchet', 'Baller', 'Big', 'Money', 'Gang', 'Gangster', 'Gangsta', 'Gangstah']
    
    result = random.choice(preffix) + random.choice(names) + random.choice(suffix) + str(random.randint(1111, 9999))
    
    return result
    
def pass_gen():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""
    
    for c in range(16):
        password += random.choice(chars)
        
    return password

def get_proxy():
    global proxychoice
    with open("proxies.txt", "r") as f:
        proxies = f.readlines()
        f.close()
    
    while True:
        proxy = proxies[proxychoice].strip()
        try:
            requests.get('https://www.google.com/', proxies={'http': proxy, 'https': proxy}, timeout=5)
            return proxy
        except:
            print(f"\r{Colors.pink}>> {Colors.white}Proxy {proxy} is not working. Trying another proxy...                                {Colors.white}", end="")
            proxychoice += 1
            if proxychoice >= len(proxies):
                proxychoice = 0

# Main

visual = input(f"{Colors.pink}>> {Colors.white}Do you want to have visual feedback? (y/n): {Colors.white}")
solver = input(f"{Colors.pink}>> {Colors.white}Do you want to use the captcha solver? (y/n): {Colors.white}")
if visual.lower() == "y":
    print(f"{Colors.pink}>> {Colors.white}Visual feedback enabled!{Colors.white}")
    options = Options()
    options.add_argument(f'--user-agent={ua}')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument("log-level=3")
    options.add_argument('--no-sandbox')
    if solver.lower() == "y":
        options.add_extension("./solver/solver.crx")
    else: 
        pass
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
else:
    print(f"{Colors.pink}>> {Colors.white}Visual feedback disabled!{Colors.white}")
    options = Options()
    options.add_argument(f'--user-agent={ua}')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument("log-level=3")
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    if solver.lower() == "y":
        options.add_extension("./solver/solver.crx")
    else: 
        pass
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 250)


amount = input(f"{Colors.pink}\n>> {Colors.white}How many accounts do you want to generate?: {Colors.white}")
prox_use = input(f"{Colors.pink}>> {Colors.white}Do you want to use proxies? (y/n): {Colors.white}")
amount = int(amount)
accs = amount

print(f"{Colors.pink}\n>> {Colors.white}Account Types: \n{Colors.pink}[{Colors.white}N{Colors.pink}] - {Colors.white}Normal Acc{Colors.pink} \n[{Colors.white}G{Colors.pink}] - {Colors.white}Gamer Acc{Colors.pink}")
gen_type = input(f"{Colors.pink}\n>> {Colors.white}Enter account type: {Colors.white}")

if gen_type.lower() == "n":
    gen_type = "normal"
    
if gen_type.lower() == "g":
    gen_type = "gamer"

while True:
    
    if prox_use.lower() == "y":
        driver.quit()
        proxy = get_proxy()
        options.add_argument(f'--proxy-server={proxy}')
        driver = un.Chrome(options=options)
    else: 
        proxy = "None"
        
    proxychoice += 1
    fail = False
    password = pass_gen()
    
    if gen_type == "normal":
        try:
            username = normal_namegen()
        except:
            fail = True
        
    elif gen_type == "gamer":
        try:
            username = gamer_namegen()
        except:
            fail = True
    
    if fail == False:
        print(f"{Colors.pink}>> {Colors.white}Username: {username} | Password: {password} | Proxy: {proxy} |{Colors.white}")
        
        try: 
            driver.get("https://account.proton.me/signup?plan=free&billing=12&ref=prctbl&minimumCycle=12&currency=USD&product=mail&language=en")
            print(f"{Colors.pink}>> {Colors.white}Loading page...{Colors.white}")
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
            time.sleep(5)
            print(f"{Colors.pink}>> {Colors.white}Page loaded!{Colors.white}")
        except:
            print(f"{Colors.pink}>> {Colors.white}Failed to load page!{Colors.white}")
            miss += 1
            fail = True
        
        if fail == False:
            try:
                print(f"{Colors.pink}>> {Colors.white}Adding username...{Colors.white}")
                time.sleep(random.uniform(0.8, 1.3))
                pyautogui.moveTo(420, 459, duration=random.uniform(0.3, 0.5))
                pyautogui.click()
                keyboard.type(username)
                print(f"{Colors.pink}>> {Colors.white}Adding password...{Colors.white}")
                time.sleep(random.uniform(0.8, 1.3))
                driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
                print(f"{Colors.pink}>> {Colors.white}Adding password again...{Colors.white}")
                driver.find_element(By.XPATH, '//*[@id="repeat-password"]').send_keys(password)
                time.sleep(random.uniform(0.8, 1.3))
                print(f"{Colors.pink}>> {Colors.white}Sending...{Colors.white}")
                driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[1]/div/main/div[2]/form/button').click()
                time.sleep(random.uniform(0.8, 1.3))
            except:
                print(f"{Colors.pink}>> {Colors.white}Failed to add details!{Colors.white}")
                miss += 1
                fail = True
            
            if fail == False:
                try:
                    print(f"{Colors.pink}>> {Colors.white}Please complete verification, you have {Colors.pink}250{Colors.white} seconds!{Colors.white}")
                    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="displayName"]')))
                    print(f"{Colors.pink}>> {Colors.white}Verification complete!{Colors.white}")
                except:
                    print(f"{Colors.pink}>> {Colors.white}Failed to verify!{Colors.white}")
                    miss += 1
                    fail = True
                if fail == False:
                    try:
                        print(f"{Colors.pink}>> {Colors.white}Adding displayname...{Colors.white}")
                        driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/main/div[2]/form/button').click()
                    except:
                        print(f"{Colors.pink}>> {Colors.white}Failed to set displayname!{Colors.white}")
                        miss += 1
                        fail = True
                    if fail == False:
                        try: 
                            print(f"{Colors.pink}>> {Colors.white}Skipping phone verification...{Colors.white}")
                            driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/main/div[2]/form/button[2]').click()
                            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/dialog/div')))
                            driver.find_element(By.XPATH, '/html/body/div[4]/dialog/div/div[4]/button[1]').click()
                            print(f"{Colors.pink}>> {Colors.white}Account created!{Colors.white}")
                            print(f"{Colors.pink}>> Saving credentials...{Colors.white}")
                        except:
                            print(f"{Colors.pink}>> {Colors.white}Failed to skip phone verification!{Colors.white}")
                            miss += 1
                            fail = True

    elif fail == True:
        driver.quit()
        pass
    
    if fail == False:
        s = "----- Proton Account -----"
        u = "Email: " + username + "@proton.me"
        p = "Password: " + password
        d = "--------------------------"
        with open("accounts.txt", "a") as f:
            f.write(s)
            f.write("\n")
            f.write(u)
            f.write("\n")
            f.write(p)
            f.write("\n")
            f.write(d)
            f.write("\n")
            f.flush()
            f.close()
            
        amount -= 1
        hits += 1
        
    if amount <= 0:
        print(f"{Colors.pink}>> {Colors.white}Done!{Colors.white}")
        print(f"{Colors.pink}>> {Colors.white}Created {Colors.pink}{hits}{Colors.white} out of {Colors.pink}{accs}{Colors.white} accounts!{Colors.white} (misses: {Colors.pink}{miss}{Colors.white})")
        print(f"{Colors.pink}>> {Colors.white}Thanks for using ProtonGen V2!{Colors.white}")
        break