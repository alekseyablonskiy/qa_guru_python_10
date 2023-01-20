from datetime import date
import allure
from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages.practice_form import PracticeForm


@allure.title("Successful fill form")
def test_registration_user():
    practice_form = PracticeForm()
    user = User(
        first_name='Aleksey',
        last_name='Yablonskiy',
        email='alekseyablonskiy@gmail.com',
        phone='1234567890',
        address='Minsk',
        birthday=date(1996, 10, 27),
        gender='Male',
        subject='Computer Science',
        hobbies='Music',
        image='picture.jpg',
        state='NCR',
        city='Delhi')

    with allure.step('Open registration form'):
        practice_form.open_page()
    with allure.step('Fill registration form'):
        practice_form.fill(user).submit()
    with allure.step('Check registration form result'):
        practice_form.assert_results_registration(user)