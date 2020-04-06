import sys
import os
import utilities.config as sconfig
browsers = sys.argv
if browsers.__len__() !=  0:
    for browser in browsers[1:]:
        f = open("utilities/testsettings.json", "w")
        f.write(
            '{"url": "https://www.google.com/maps","browser": "'+browser+'","driver_timeout": "5"}')
        f.close()
        os.system('behave')

os.system('allure serve reports/')

