from behave import *
from utilities.driverUtil import driver
import utilities.config as sconfig
from pageUtils.elements import *
from selenium.webdriver.common.keys import Keys
import re

use_step_matcher("re")

@given("I go to Google Maps")
def step_impl(context):
    driver.navigateToMaps(sconfig.googleMapUrl)

@when("I input source and destination in maps")
def step_impl(context):
    driver.elementClick(directionBtn)
    driver.waitOnElement(sourceField)
    driver.clearElement(sourceField)
    driver.enterValues(sourceField, sconfig.source)
    driver.clearElement(destinationField)
    driver.enterValues(destinationField, sconfig.destination)
    driver.enterValues(destinationField, Keys.ENTER)

@when("I check flights information by clicking google flights")
def step_impl(context):
    driver.waitOnElement(walkBicycleFirstResultHours)
    driver.elementClick(flightBtn)
    driver.waitOnElement(flightResultLink)
    driver.elementClick(flightResultLink)
    driver.waitFor(3)
    driver.switchWindow()
    driver.waitOnElement(fromDate)

@then("I verify car distance in the maps from PA to CA is greater than 40 hours")
def step_impl(context):
    driver.waitOnElement(carFirstResultHours)
    hours = driver.getTextForElement(carFirstResultHours)
    print("Number of hours: " + hours)
    hoursValue = int(hours[:-1])
    print("Number of hours by Car: "+str(hoursValue))
    assert hoursValue > sconfig.carHoursMin

@then("I verify walking distance in the maps from PA to CA is more than 900 hours")
def step_impl(context):
    driver.waitOnElement(carFirstResultHours)
    driver.elementClick(walkBtn)
    driver.waitOnElement(walkBicycleFirstResultHours)
    miles = driver.getTextForElement(walkFirstResultMiles)
    print("Number of Miles: " + miles)
    milesValue = int(re.sub('[^0-9]', '', miles))
    print("Number of miles by Walk: " + str(milesValue))
    assert milesValue > sconfig.walkMilesMin

@then("I verify bicycle distance on google maps from PA to CA is more than 250 horus and includes Ferry in the directions")
def step_impl(context):
    driver.waitOnElement(walkBicycleFirstResultHours)
    driver.elementClick(cycleBtn)
    driver.waitOnElement(walkBicycleFirstResultHours)
    hours = driver.getTextForElement(walkBicycleFirstResultHours)
    print("Number of hours: " + hours)
    hoursValue = int(hours[:-1])
    print("Number of hours by Bicycle: " + str(hoursValue))
    assert hoursValue > sconfig.bicycleHoursMin
    ferryMsg = driver.getTextForElement(ferryMessage)
    print("Ferry Message is: " + ferryMsg)
    assert ferryMsg == sconfig.ferryIncludedMsg

@then("I verify flight booking from google maps doesn't allow booking for more than 11 months in the future")
def step_impl(context):
    driver.elementClick(fromDate)
    driver.waitOnElement(firstAvailDate)

    availToClickCount = len(driver.getElements(availDate))
    numOfMonthsAvaialble = int(availToClickCount / 30)
    print("Number of months to book ahead from elements: "+str(numOfMonthsAvaialble))
    availCheckCount = 1

    try:
        for i in range(1, numOfMonthsAvaialble+1):
            print("Next month selection clicked")
            driver.elementClick(nextMonthSelectionBtn)
            availCheckCount=availCheckCount+1
    except:
        driver.elementClick(nextMonthSelectionBtnDisabled)
        print("Number of months to book ahead from next month click: " + str(availCheckCount))
        assert availCheckCount == numOfMonthsAvaialble