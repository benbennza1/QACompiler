from splinter import Browser
from time import sleep

SLASH = "/"

def step(browser):
    return step1(browser)

def step1(browser, loop = False):
    url = "https://www.youtube.com/"

    if url.count(SLASH) < 3 and not (url.endswith(SLASH)):
        url += SLASH
    browser.visit(url)

    #Checking Step 1
    url = "https://www.youtube.com/"
    if not (url.endswith(SLASH)):
        url += SLASH
    if browser.url != url:
        return "1"

    if loop:
        return
    return step2(browser,loop)

def step2(browser, loop = False):
    #step 2 : enter "test" into textfield with name "q" | textfield with title "Search" should have value "test"
    browser.find_by_id("masthead-search-term").first.type("happy fruit")

    #Checking Step 2
    if browser.find_by_id("masthead-search-term").first.value != "happy fruit":
        return "2"

    if loop:
        return
    return 

def step3(browser, loop = False):
    if len(browser.find_by_id("search-btn")) > 0:
        if loop:
            step5(browser, loop = True)
        return step5(browser,loop)
    else:
        if loop:
            step5(browser, loop = True)
        return step4(browser,loop)

def step4(browser, loop = False):
    if loop:
        return
    return

def step5(browser, loop = False):
    oldURL = browser.url
    browser.find_by_id("search-btn").first.click()

    sleep(1)
    c = 0
    newURL = browser.url
    while oldURL == newURL or browser.evaluate_script("document.readyState")!="complete":
        sleep(0.1)
        c+=1
        if c>10000:
            return "5"
    
    if browser.html.find("Happy zSunshine Friends") != -1:
        if loop:
            return 
        return step6(browser, loop)
    else:
        return "5"

def step6(browser, loop = False):
    browser.reload()

    url = "https://www.youtube.com/results?search_query=happy+fruit"
    if url.count(SLASH) < 3 and not (url.endswith(SLASH)):
        url += SLASH
    if browser.url != url:
        return "1"  
    if loop:
        return 
    return step7(browser, loop)

def step7(browser, loop = False):
    c = 0
    for c in range (0, 10):
        err = step6(browser, loop = True)
        if not (err == None) and not (err.isspace()) and not (len(err) == 0):
            return "7"

    return step8(browser, loop)

def refreshwebpage(browser, loop = False):
    return refreshwebpage_step1(browser, loop)

def refreshwebpage_step1(browser, loop = False):
    browser.reload()

    url = "https://www.youtube.com/results?search_query=happy+fruit"
    if url.count(SLASH) < 3 and not (url.endswith(SLASH)):
        url += SLASH
    if browser.url != url:
        return "refreshwebpage:1"  
    if loop:
        return 
    return
        
def step8(browser, loop = False):
    c = 0
    for c in range (0, 5):
        err = refreshwebpage(browser, loop = True)
        if not (err == None) and not (err.isspace()) and not (len(err) == 0):
            return "8"
    return step9(browser, loop)

def step9(browser, loop = False):
    numCalc = float(browser.find_by_id("num1").first.value) - float(browser.find_by_id("num2").first.value)
    browser.find_by_id("userInput").type(str(numCalc))

    if loop:
        return
    return step10(broser, loop)

def step10(browser, loop = False):
    strConcat = browser.find_by_id("1").first.value + browser.find_by_id("4").first.value
    browser.find_by_id("userInput").type(strConcat)
    
    if loop:
        return
    return     
    
def checkSteps():
    browser=Browser('chrome')
    err = step(browser);

    #program is done
    #browser.quit()

    #return the errors if exist
    if not (err == None) and not (err.isspace()) and not (len(err) == 0):
        return "Program failed on step: " + err + "\n"
        
    return ("Program finished executed without errors.")

if __name__ == '__main__':
    print(checkSteps())
