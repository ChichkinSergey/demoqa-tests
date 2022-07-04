import time

from selene import have, command
from selene.support.shared import browser

def test_practice_form():
    #Variables used in this test:
    first_name = "Mahatma"
    last_name = "Gandhi"
    user_email = "mahatma@test.tst"
    phone_number = "1234567890"
    current_address = "Oak Street 8"

    browser.open("/automation-practice-form")

    browser.element("#firstName").type(first_name)
    browser.element("#lastName").type(last_name)
    browser.element("#userEmail").type(user_email)
    browser.element("label[for='gender-radio-1']").click()
    browser.element("#userNumber").type(phone_number)

    #Selecting 8 March 1950 in the calendar
    (
    browser.element("#dateOfBirthInput").click() #click on the calendar
    .element("//select[@class='react-datepicker__year-select']").click() #click on the year
    .element("//option[@value='1950']").click() #click on 1950
    .element("//select[@class='react-datepicker__month-select']").click() #click on month
    .element("//option[@value='2']").click() #click on March
    .element("//div[@aria-label='Choose Wednesday, March 8th, 1950']").click() #click on 8
    )

   # browser.element("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]").click().press().type("Math").click()#.type("Computer Science")

    browser.element("label[for='hobbies-checkbox-1']").click()
    browser.element("label[for='hobbies-checkbox-2']").click()
    browser.element("label[for='hobbies-checkbox-3']").click()
    browser.element("#currentAddress").type(current_address)
    browser.element("#submit").perform(command.js.scroll_into_view).click()
    time.sleep(5)


