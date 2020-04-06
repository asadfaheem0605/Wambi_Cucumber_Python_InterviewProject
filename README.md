# Python-Behave-Selenium

## Test Cases Included

For this demo I have 4 test cases implemented. These test cases are validating the following scenarios: 
Test Case #1: Validate car distance on google maps from PA to CA is more than 40 hours
Test Case #2: Validate walking distance on google maps from PA to CA is more than 900 hours
Test Case #3: Validate bicycle distance on google maps from PA to CA is more than 250 horus and includes Ferry in the directions
Test Case #4(Edge Case): Validate flight booking from google maps doesn't allow booking for more than 11 months in the future 


##Framework-Page Object Model Overview
I am using Cucumber BDD framework with Page Object Model. Language used for this framework is python. Behave is the python library used for implementing this BDD framework.
It is a common language syntax which can be used to define steps for end to end tests.

Overview of the Page Object Model 

1)Feature file includes all the test cases setup as individual scenarios. 
2)Logic behind each step is inside the step definition file. 
3)All the common functions used in the project are driverUtil file
4)config file includes the url and basic information for common variables. 
5)pageUtils includes all the elements and their xpaths that are being used for automation. 
6)environment files includes the before and after methods for all the tests
7)All the reports are generated and kept in the reports folder. 
   

## Installations for environment setup
1) First of move root project directory execute `pip install -r requirements.txt` which will install the all needed python dependencies to your computer

2) Install the chromedriver using: `brew cask install chromedriver`
 
3) Install the geckodriver(firefox) using: `brew install geckodriver`
 
4) Install allure using `brew install allure` & `pip install allure_behave`(OR `npm install -g allure-commandline --save-dev`)

#Test Execution

1) In the root project directory execute: `behave`and it will start executing tests

2) In the root project directory execute: run `behave -f plain --no-capture features/GoogleSearch_UI.feature` to print logs from print statements.

3) In the root project directory execute: run `behave -f plain --no-capture --tags=@<tagName> features/GoogleSearch_UI.feature` to print logs and run specific test by providing tag.

4) To execute tests with multiple browsers and generate report, execute below three commands in different command prompts
  --Follow steps below. 



## CROSS BROWSER TESTING -- SELENIUM GRID

 **Download the Selenium standalone jar file: [https://bit.ly/2TlkRyu](https://bit.ly/2TlkRyu)**

1) Open terminal-1 and enter: `java -jar <path to downlaoded jar file>> -role hub` EXAMPLE:  `java -jar /Users/Asad/Downloads/selenium-server-standalone-3.141.59.jar -role hub`

It gives a message saying: `Nodes should register to [http://<LOCALHOSTIP>:4444/grid/register/](http://<LOCALHOSTIP>:4444/grid/register/)` so you need to start the node(step-2)

2) Open terminal-2 and enter: `java -jar selenium-server-standalone-3.141.59.jar -role node -hub [http://<LOCALHOSTIP>:4444/wd/hub](EXAMPLE: http://192.168.1.77:4444/wd/hub)`

Once you execute this command it will register the node to above hub and now hub will say: `Clients should connect to [http://<LOCALHOSTIP>:4444/wd/hub](EXAMPLE: http://192.168.1.77:4444/wd/hub)`

3) Once the hub and node are running: To execute a test on multiple browsers use command `python exec.py chrome firefox` 
