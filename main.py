import os
import time
import random
import string
import csv
import sys
import selenium
import requests
from selenium import webdriver
from colorama import Fore, Back, Style
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from pystyle import Colorate, Colors, Center
from selenium.webdriver.chrome.options import Options 

def title():
	os.system("cls")
	banner = (Colorate.Vertical(Colors.red_to_purple, """

						██████╗ ██████╗  ██████╗ ████████╗ ██████╗ ███╗   ██╗███╗   ███╗ █████╗ ██╗██╗      ██████╗ ███████╗███╗   ██╗
						██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔═══██╗████╗  ██║████╗ ████║██╔══██╗██║██║     ██╔════╝ ██╔════╝████╗  ██║
						██████╔╝██████╔╝██║   ██║   ██║   ██║   ██║██╔██╗ ██║██╔████╔██║███████║██║██║     ██║  ███╗█████╗  ██╔██╗ ██║
						██╔═══╝ ██╔══██╗██║   ██║   ██║   ██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══██║██║██║     ██║   ██║██╔══╝  ██║╚██╗██║
						██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚████║██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╔╝███████╗██║ ╚████║
						╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
																																																
========================================================================================================================
	"""))
	print(banner)
	print (Center.XCenter(f"""{Fore.LIGHTMAGENTA_EX}
	>> {Fore.LIGHTRED_EX}Made By Taquito & NotRageJustGood {Fore.LIGHTMAGENTA_EX}
	>> {Fore.LIGHTRED_EX}Version 1.0 {Fore.LIGHTMAGENTA_EX}"""))

def gname():
	name = ['anita', 'robert', 'jones', 'laver', 'gratsher', 'killoms', 'ramez', 'sarah', 'michael', 'david', 'jennifer', 'chris', 'emily', 'john', 'jessica', 'matthew', 'ashley', 'mike', 'amanda']
	suffix = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	
	csuffix = random.choice(suffix)
	rname = random.choice(name)

	rngsuffix = random.choice(suffix)
	i = 0
	while i < 4:
		rngsuffix += random.choice(suffix)
		i += 1

	final_name = rname + rngsuffix
	return final_name

def gpass():
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	i = 0
	password = random.choice(numbers) + random.choice(alphabet)
	while i < 4:
		password += random.choice(numbers) + random.choice(alphabet)
		i += 1

	return password

title()
url = 'https://account.proton.me/signup?plan=free&billing=12&minimumCycle=12&currency=USD&product=mail&language=en'
amount = input("\n\nEnter the amount of accounts to generate: ")
prox = input("\nUse proxies? (Y/N): ")
keyboard = Controller()

a = 0
while True:
	user = gname()
	passw = gpass()
	print("\nCredentials:\n" + user)
	print(passw)
	print("\n")
	r = 0
	if prox == 'y' or prox == 'Y':
		with open('./proxies.txt', 'r') as data:
			proxy_lines = [line.strip() for line in data]
		proxy_from_file = "false"
		while (proxy_from_file == "false"):
			r += 1
			print(proxy_lines[r])
			try:
				proxies_file = {'http':'http://:@{}/'.format(proxy_lines[r])}
				requests.get("http://protonmail.com/", proxies=proxies_file, timeout=1.5)
			except OSError:
				print ("Proxy Connection error!")
				proxy_from_file = "false"
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K") 
				sys.stdout.write("\033[F")
				sys.stdout.write("\033[K") 
			else:
				print ("Proxy is working...")
				r += 1
				options = webdriver.ChromeOptions()
				options.add_argument('--proxy-server=%s'.format(proxy_lines[r]))
				proxy_from_file = "true"
				driver = webdriver.Chrome(options=options)
	else:
		driver = webdriver.Chrome()
		pass

	driver.get(url)

	time.sleep(8)

	keyboard.type(user)

	time.sleep(1)

	driver.switch_to.default_content()

	time.sleep(1)

	driver.find_element(By.ID, "password").send_keys(passw)

	time.sleep(1)

	driver.find_element(By.ID, "repeat-password").send_keys(passw)

	time.sleep(1)

	driver.find_element(By.CSS_SELECTOR, "body > div.app-root > div.flex-no-min-children.flex-nowrap.flex-column.h100.sign-layout-bg.scroll-if-needed.relative > div.sign-layout-container.flex-item-fluid-auto.flex.flex-nowrap.flex-column.flex-justify-space-between > div > main > div.sign-layout-main-content > form > button").click()

	time.sleep(5)

	capcha = input("\nPress enter when you complete the capcha and setup!")

	account = user + "@proton.me" + ":" + passw
	with open("accounts.txt", "w") as f:
		f.write(account)
		f.write("\n")

	a += 1

	if amount == 1:
		break