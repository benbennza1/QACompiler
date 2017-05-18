from splinter import Browser

SLASH = "/"

def step(browser):
    return step1(browser)

def step1(browser):
    url = "https://www.google.ca"

    if not (url.endswith(SLASH)):
        url += SLASH
    browser.visit(url)

    #Checking Step 1
    if browser.url != url:
        print (browser.url)
        return "step 1 error message\n" + step2(browser)

    #Calling next step
    return step2(browser)

def step2(browser):
    browser.fill('q', 'happy fruit')

    # not sure how you can check the value here
    return ""

def checkSteps():
    browser=Browser('chrome')
    err = step(browser);

    #program is done
    #browser.quit()

    #return the errors if exist
    if not (err == None) and not (err.isspace()) and not (len(err) == 0):
        return err
        
    return ("Program finished executed.")

if __name__ == '__main__':
    print(checkSteps())
