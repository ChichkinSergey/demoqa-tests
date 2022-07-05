import time

from selene import have, command
from selene.support.shared import browser

def test_webtables():
    # Variables used in this test:
    first_name = "Indira"
    last_name = "Gandhi"
    user_email = "indira@test.tst"
    age = 65
    salary = 10000
    department = "Government of India"

    # Open URL to test:
    browser.open("/webtables")

    # 1a. Adding a new row
    browser.element("#addNewRecordButton").click()
    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)
    browser.element("#userEmail").type(user_email)
    browser.element("#age").type(age)
    browser.element("#age").type(age)
    browser.element("#salary").type(salary)
    browser.element("#department").type(department)
    browser.element("#submit").click()

    # 1b. Checking that the information from step 1a is correct



    time.sleep(5)