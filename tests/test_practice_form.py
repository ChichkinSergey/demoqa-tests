import time

from selene import have, command
from selene.support.shared import browser
from demoqa_tests.utils import path_to


class student:
    first_name = "Mahatma"
    last_name = "Gandhi"
    user_email = "mahatma@test.tst"
    gender = 1 # 1 = Male, 2 = Female, 3 = Other
    mobile_number = "1234567890"
    picture_name = 'pic.jpeg'
    current_address = "Oak Street 8"
    state = "Uttar Pradesh"
    city = "Lucknow"
    subject_math = "Maths"
    subject_computer_science = "Computer Science"
    birth_year = "1950"
    birth_month = 2 # Jan = 0, Feb = 1, Mar = 2, etc
    birth_day = "8"

    @staticmethod
    def gender_number_to_string():
        if student.gender == 1:
            return "Male"
        elif student.gender == 2:
            return "Female"
        else:
            return "Other"

    @staticmethod
    def month_to_string():
        if student.birth_month == 0:
            return "January"
        elif student.birth_month == 1:
            return "February"
        elif student.birth_month == 2:
            return "March"
        elif student.birth_month == 3:
            return "April"
        elif student.birth_month == 4:
            return "May"
        elif student.birth_month == 5:
            return "June"
        elif student.birth_month == 6:
            return "July"
        elif student.birth_month == 7:
            return "August"
        elif student.birth_month == 8:
            return "September"
        elif student.birth_month == 9:
            return "October"
        elif student.birth_month == 10:
            return "November"
        elif student.birth_month == 11:
            return "December"

def test_student_registration_form():
    def check_for_google_ads():
        if browser.element('#adplus-anchor').is_enabled():
            browser.execute_script("document.querySelector('#adplus-anchor').remove()")  # removes Google Ads footer

    # Act:
    browser.open("/automation-practice-form")
    check_for_google_ads()

    browser.element("#firstName").type(student.first_name)
    browser.element("#lastName").type(student.last_name)
    browser.element("#userEmail").type(student.user_email)

    browser.element(f"[for='gender-radio-{student.gender}']").click()

    browser.element("#userNumber").type(student.mobile_number)

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").element(f"[value='{student.birth_year}']").click()
    browser.element(".react-datepicker__month-select").element(f"[value='{student.birth_month}']").click()
    browser.element(f".react-datepicker__day--00{student.birth_day}").click()

    browser.element("#subjectsInput").type(student.subject_math).press_enter()
    browser.element("#subjectsInput").type(student.subject_computer_science).press_enter()

    def checkbox_click(selector):
        browser.element(selector).click()


    checkbox_click("label[for='hobbies-checkbox-1']")
    checkbox_click("label[for='hobbies-checkbox-2']")
    checkbox_click("label[for='hobbies-checkbox-3']")


    browser.element('#uploadPicture').send_keys(path_to(student.picture_name))

    browser.element("#currentAddress").type(student.current_address)

    browser.element("#state").element("input").perform(command.js.scroll_into_view)

    def selector_input(selector, text):
        browser.element(selector).element("input").type(text).press_tab()

    selector_input("#state", student.state)
    selector_input("#city", student.city)

    browser.element("#submit").perform(command.js.click)

    # Assert:
    def cells_of_row(index):
        return browser.elements('.modal-dialog').all('table tr')[index].all('td')

    gender = student.gender_number_to_string()
    birth_month = student.month_to_string()

    cells_of_row(1).should(have.texts('Student Name', f'{student.first_name} {student.last_name}'))
    cells_of_row(2).should(have.texts('Student Email', student.user_email))
    cells_of_row(3).should(have.texts('Gender', gender))
    cells_of_row(4).should(have.texts('Mobile', student.mobile_number))
    cells_of_row(5).should(have.texts('Date of Birth', f'0{student.birth_day} {birth_month},{student.birth_year}'))
    cells_of_row(6).should(have.texts('Subjects', f'{student.subject_math}, {student.subject_computer_science}'))
    cells_of_row(7).should(have.texts('Hobbies', 'Sports, Reading, Music'))
    cells_of_row(8).should(have.texts('Picture', student.picture_name))
    cells_of_row(9).should(have.texts('Address', student.current_address))
    cells_of_row(10).should(have.texts('State and City', f'{student.state} {student.city}'))