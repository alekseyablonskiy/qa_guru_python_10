from selene import have
from selene.support.shared import browser
from demoqa_tests.model.controls.checkboxes import Checkboxes
from demoqa_tests.model.controls.datepicker import Datepicker
from demoqa_tests.model.controls.drop_down import Dropdown
from demoqa_tests.model.controls.radiobutton import Radiobutton
from demoqa_tests.utils import path_to_file, date_config


class PracticeForm:
    def open_page(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def fill_name(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        return self

    def fill_contacts(self, user):
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.phone)
        return self

    def select_gender(self, user):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_by_value(user.gender)
        return self

    def select_birthday(self, user):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.set_date(user.birthday)
        return self

    def input_subject(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()
        return self

    def select_hobbies(self, user):
        check_hobbies = Checkboxes(browser.all('[for^=hobbies-checkbox]'))
        check_hobbies.select(user.hobbies)
        return self

    def send_image(self, user):
        browser.element('#uploadPicture').set_value(path_to_file.generate_path_upload(user.image))
        return self

    def input_address(self, user):
        browser.element('#currentAddress').type(user.address)
        return self

    def select_state(self, user):
        dropdown = Dropdown('#state')
        dropdown.select(user.state)
        return self

    def select_city(self, user):
        dropdown = Dropdown('#city')
        dropdown.select(user.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def fill(self, user):
        (self.fill_name(user)
            .fill_contacts(user)
            .select_gender(user)
            .select_birthday(user)
            .input_subject(user)
            .select_hobbies(user)
            .send_image(user)
            .input_address(user)
            .select_state(user)
            .select_city(user)
            .submit())
        return self

    def assert_results_registration(self, user):
        browser.element('.table').all('td').even.should(have.texts(
            user.first_name + ' ' + user.last_name,
            user.email,
            user.gender,
            user.phone,
            user.birthday.strftime(date_config.datetime_view_format),
            user.subject,
            user.hobbies,
            user.image,
            user.address,
            user.state + ' ' + user.city))
        return self

