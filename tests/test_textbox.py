import time

from selene import have, command
from selene.support.shared import browser

def test_submit_form():
    name = "John Doe"
    email = "test@test.com"
    current_address = " Some Street, 1"
    permanent_address = "Permanent address Some Street, 25"

    browser.open('/text-box')

    browser.should(have.title("ToolsQA"))
    browser.element('.main-header').should(have.exact_text('Text Box'))
    browser.element('#userName').type(name)
    browser.element('#userEmail').type(email)
    browser.element('#currentAddress').type(current_address)
    browser.element('#permanentAddress').type(permanent_address)
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    browser.all("#output p").should(have.texts(name, email, current_address, permanent_address))
    #same by elements:
    browser.element('#name').should(have.text(name))
    browser.element('#email').should(have.text(email))
    browser.element("#output").element("#currentAddress").should(have.text(current_address))
    browser.element("#output").element("#permanentAddress").should(have.text(permanent_address))




   # time.sleep(1)

