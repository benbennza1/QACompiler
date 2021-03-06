from splinter import Browser
from time import sleep

SLASH = "/"

def step (browser, loop = False):
	return step1(browser, loop)

def step1(browser, loop = False):
	url = "https://www.youtube.com/"
	if not (url.endswith(SLASH)):
		url += SLASH
	browser.visit(url)

	if browser.url!= 'https://www.youtube.com/':
		return "1"

	url = "https://www.baidu.com/"
	if not (url.endswith(SLASH)):
		url += SLASH
	browser.visit(url)

	if loop:
		return
	return step3(browser, loop)

def step3(browser, loop = False):
	url = "https://www.google.com/"
	if not (url.endswith(SLASH)):
		url += SLASH
	browser.visit(url)

	return

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

