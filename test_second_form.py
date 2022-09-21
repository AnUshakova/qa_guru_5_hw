import os
from selene.support.shared import browser
from selene import have, be

def test_anketa():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Ann')
    browser.element('#lastName').type('Rose')
    browser.element('#userEmail').type('aaa@aa.aa')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('April')
    browser.element('.react-datepicker__year-select').type('2001')
    browser.element("[aria-label='Choose Sunday, April 1st, 2001']").click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('Test_date/bug_logo.gif'))
    browser.element('#currentAddress').type('some adress text')
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaipur').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(be.visible).should(
        have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text('Student Name Ann Rose'))
    browser.element('.table-responsive').should(have.text('Student Email aaa@aa.aa'))
    browser.element('.table-responsive').should(have.text('Gender Female'))
    browser.element('.table-responsive').should(have.text('Mobile 1234567890'))
    browser.element('.table-responsive').should(have.text('Date of Birth 01 April,2001'))
    browser.element('.table-responsive').should(have.text('Subjects English'))
    browser.element('.table-responsive').should(have.text('Hobbies Sports'))
    browser.element('.table-responsive').should(have.text('Picture bug_logo.gif'))
    browser.element('.table-responsive').should(have.text('Address some adress text'))
    browser.element('.table-responsive').should(have.text('State and City Rajasthan Jaipur'))

