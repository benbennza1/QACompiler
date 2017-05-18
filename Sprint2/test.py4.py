from splinter import Browser

SLASH = "/"

def step(browser):
    return step1(browser)

def step1(browser):
    url = "https://www.google.com"

    if not (url.endswith(SLASH)):
        url += SLASH
    browser.visit(url)

    #Checking Step 1
    if browser.url != url:
        return "1"

def checkSteps():
    browser=Browser('chrome')
    err = step(browser);

    #program is done
    browser.quit()

    #return the errors if exist
    if not (err == None) and not (err.isspace()) and not (len(err) == 0):
        return "Program failed on step: " + err + "\n"
        
    return ("Program finished executed without errors.")

if __name__ == '__main__':
    print(checkSteps())
