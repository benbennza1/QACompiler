from splinter import Browser
from time import sleep


SLASH = "/"

def step(browser, loop = False):
	return step1(browser, loop)

def refreshwebpage_step(browser, loop = False):
	return refreshwebpage_step1(browser, loop)

def refreshwebpage_step1(browser, loop=False):
	#Step 1

	browser.reload()
	#Checking Step1
	if browser.url != "https://www.youtube.com/results?search_query=test":
		return "1"
	if loop:
		return
	return 


def step1(browser, loop=False):
	#Step 1

	url = "https://www.youtube.com/"
	if not (url.endswith(SLASH)):
		url += SLASH
	browser.visit(url)

	#Checking Step1
	if browser.url != "https://www.youtube.com/":
		return "1"
	if loop:
		return
	return step2(browser,loop)
def step2(browser, loop=False):
	#Step 2

	browser.find_by_id("masthead-search-term").first.type("test")
	#Checking Step2
	if browser.find_by_id("masthead-search-term").first.value!="test":
		return "2"
	if loop:
		return
	return step3(browser,loop)
def step3(browser, loop=False):
	#Step 3

	if len(browser.find_by_id("search-btn"))>0:
		return step5(browser,loop)
	else:
		return step4(browser,loop)

	#Checking Step3

	if loop:
		return
	return step4(browser,loop)
def step4(browser, loop=False):
	#Step 4

	return
	#Checking Step4
	if loop:
		return
def step5(browser, loop=False):
	#Step 5

	oldURL=browser.url
	browser.find_by_id("search-btn").first.click()
	sleep(1)
	d = 0
	newURL = browser.url
	while oldURL == newURL or browser.evaluate_script("document.readyState")!="complete":
		sleep(0.1)
		d+=1
		if d>10000:
			return "5"

	#Checking Step5
	if browser.html.find("Talko") == -1:
		return "5"
	if loop:
		return
	return step6(browser,loop)
def step6(browser, loop=False):
	#Step 6

	browser.reload()
	#Checking Step6
	if browser.url != "https://www.youtube.com/results?search_query=test":
		return "6"
	if loop:
		return
	return step7(browser,loop)
def step7(browser, loop=False):
	#Step 7

	c=0
	for c in range (0,10):
		err=step6(browser, loop=True)
		if not (err == None) and not (err.isspace()) and not (len(err) == 0):
			return "7"

	#Checking Step7

	if loop:
		return
	return step8(browser,loop)
def step8(browser, loop=False):
	#Step 8

	c=0
	for c in range (0,5):
		err=refreshwebpage_step(browser, loop=True)
		if not (err == None) and not (err.isspace()) and not (len(err) == 0):
			return "8"

	#Checking Step8

	if loop:
		return
	return 


def checkSteps():
	browser=Browser('chrome')
	err = step(browser)

	#program is done
	browser.quit()

	#return the failed step
	if not (err == None) and not (err.isspace()) and not (len(err) == 0):
		return "Program failed on step: " + err + "\n"

	return "The testcase passed"


if __name__ == '__main__':
	print(checkSteps())
