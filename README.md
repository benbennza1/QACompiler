# QACompiler

#### Authors
Ben (Zhang An) Ni, Dmitry Vasin

#### Input Language
Newly designed human readable language

#### Target Language
Python

#### Project Description
The input language will be a set of human readable instructions intended to be used by QA personnel in software testing. This will be a newly designed language, not an existing one. It will consist of a series of steps, and each step will have an optional result to which the current state of the program will be compared. The idea behind this language is to make a human readable language for creating test cases which can be executed automatically, but can also be examined by a person with no prior experience. Typical usage would have a software engineer write a test case and have all of them executed. Then an untrained QA employee would be able to look at the failing test cases, reproduce them and see why they failed. In order to limit the scope of the task, only web pages will be available for testing using this language.

#### Input Code Example
```
main :
step 1 : go to https://www.google.ca/ | webpage at https://www.google.ca/ should load
step 2 : enter "test" into textfield with title "Search" | textfield with title "Search" should have value "test"
step 3 : if there is button with value "Google Search" go to step 5 otherwise go to step 4 |
step 4 : exit |
step 5 : click button with value "Google Search" | current webpage should contain "Test - Wikipedia"
step 6 : refresh current webpage | webpage at https://www.google.ca/ should load
step 7 : do step 6 10 times |
step 8 : do refreshwebpage 5 times |

refreshwebpage :
step 1 : refresh current webpage | webpage at https://www.google.ca/ should load
```

#### Output Code Example
```Python
def refreshwebpage_step (browser, loop = False):
	return refreshwebpage_step1(browser, loop)

def refreshwebpage_step1(browser, loop = False):
	browser.reload()

	if browser.url!= 'https://www.youtube.com/results?search_query=test':
		return "1"

	if loop:
		return
	return

```

