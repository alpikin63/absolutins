import allure

from core.data.builders.form_data_builder import FormData
from core.data.page_data import PageData
from core.data.step_name_data import StepNameData
from core.pages.base_app_page import BaseAppPage
from core.pages.custom_elements.checkbox import Checkbox
from settings import settings
from selene.api import s, be, browser, have, command, query


class CoronavirusInsurancePolicyPage(BaseAppPage):
    def __init__(self, do_open=True):
        super().__init__()
        self.url = '{base_url}{relative_url}'.format(
            base_url=settings.stand.base_url,
            relative_url=PageData.CORONAVIRUS_INSURANCE_POLICY_PAGE.relative_url
        )
        self._current_step_text = s('.calc-steps-desktop li.current span')
        # расчет
        self._sum_100_000_switcher = s('//label[text()="100 000 ₽"]/..')
        self._sum_500_000_switcher = s('//label[text()="500 000 ₽"]/..')
        self._medicine_checkbox = Checkbox('//*[@class ="step1"]//input[@name="medicine"]/..')
        self._virus_contact_checkbox = Checkbox('//*[@class ="step1"]//input[@name="virus-contact"]/..')
        self._price_input = s('.step1 #price')
        self._price_input = s('.step1 #dateStart')
        self._price_input = s('.step1 #dateEnd')
        self._continue_button = s('button[name="calculate"]')

        # ввод данных
        self._fio_input = s('.step2 #name')
        self._birthday_input = s('.step2 #dateBirth')
        self._doc_number_input = s('.step2 #id')
        self._doc_issue_date_input = s('.step2 #idDate')
        self._registration_address_input = s('.step2 #address')
        self._phone_input = s('.step2 #phone')
        self._email_input = s('.step2 #email')
        self._add_person_checkbox = Checkbox('//*[@class ="step2"]//input[@name="addPerson"]/..')
        self._name_insured_input = s('.step2 #nameInsured')
        self._date_birth_insured_input = s('.step2 #dateBirthInsured')
        self._id_insured_input = s('.step2 #idInsured')
        self._id_date_insured_input = s('.step2 #idDateInsured')
        self._go_to_payment_button = s('//button[text()="Перейти к оплате"]')

        if do_open:
            self.navigate(self.url)

    @allure.step('Выбрать чекбокс "Профессиональная сфера связана с медицинской деятельностью".')
    def fill_medicine_checkbox(self):
        self._medicine_checkbox.set(True)

    @allure.step('Выбрать страховую сумму полиса.')
    def select_sum_insured(self, sum_value: int = 100_000):
        if sum_value == 100_000:
            with allure.step('выбрать сумму: 100000'):
                self._sum_100_000_switcher.click()
        else:
            with allure.step('выбрать сумму: 500000'):
                self._sum_500_000_switcher.click()

    @allure.step('Выбрать чекбокс "Подтверждаю, что -  Отсутствуют лица,'
                 ' проживающие совместно с Застрахованным, у которых диагностирована '
                 'коронавирусная инфекция COVID-2019 ( код заболевания по МКБ-10 – В 34.2.)".')
    def fill_virus_contact_checkbox(self):
        self._virus_contact_checkbox.set(True)

    @allure.step('Нажать кнопку "Продолжить".')
    def click_on_continue_btn(self):
        self._continue_button.click()

    @allure.step('Проверить недоступность кнопки "Продолжить".')
    def assure_continue_btn_disabled(self):
        self._continue_button.should(be.disabled)

    @allure.step('Проверить название текущего шага.')
    def assure_current_step_name(self, value: StepNameData):
        self._current_step_text.should(have.text(value))

    @allure.step('Заполнить поле "ФИО страхователя"')
    def fill_fio(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                self._fio_input.set_value(value)

    @allure.step('Заполнить поле "Дата рождения страхователя"')
    def fill_birthday(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                js_id = self._birthday_input.get(query.attribute('id'))
                browser.driver.execute_script(f'$("#{js_id}").datepicker("setDate", "{value}")')

    @allure.step('Заполнить поле "Серия/номер паспорта страхователя"')
    def fill_doc_number(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                self._doc_number_input.perform(command.js.set_value(value))

    @allure.step('Заполнить поле "Дата выдачи"')
    def fill_doc_issue_date(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                js_id = self._doc_issue_date_input.get(query.attribute('id'))
                browser.driver.execute_script(f'$("#{js_id}").datepicker("setDate", "{value}")')

    @allure.step('Заполнить поле "Адрес регистрации"')
    def fill_registration_address(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                self._registration_address_input.set_value(value)

    @allure.step('Заполнить поле "Телефон"')
    def fill_phone(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                self._phone_input.set_value(value)

    @allure.step('Заполнить поле "Email"')
    def fill_email(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                self._email_input.set_value(value)

    @allure.step('Заполнить поле "ФИО застрахованного"')
    def fill_name_insured(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                self._name_insured_input.set_value(value)

    @allure.step('Заполнить поле "Дата рождения застрахованного"')
    def fill_date_birth_insured(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                js_id = self._date_birth_insured_input.get(query.attribute('id'))
                browser.driver.execute_script(f'$("#{js_id}").datepicker("setDate", "{value}")')

    @allure.step('Заполнить поле "Серия/номер паспорта застрахованного"')
    def fill_id_insured(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                self._id_insured_input.perform(command.js.set_value(value))

    @allure.step('Заполнить поле "Дата выдачи" у застрахованного')
    def fill_id_date_insured_input(self, value: str):
        if value:
            with allure.step(f'Ввести значение: {value}'):
                js_id = self._id_date_insured_input.get(query.attribute('id'))
                browser.driver.execute_script(f'$("#{js_id}").datepicker("setDate", "{value}")')

    @allure.step('Заполнить форму "Ввод данных"')
    def fill_form_data(self, value: FormData):
        self.fill_fio(value.fio)
        self.fill_birthday(value.birthday)
        self.fill_doc_number(value.doc_data)
        self.fill_doc_issue_date(value.doc_issue_date)
        self.fill_registration_address(value.registration_address)
        self.fill_phone(value.phone)
        self.fill_email(value.email)
        if not value.add_person:
            self._add_person_checkbox.set(value.add_person)
            self.fill_name_insured(value.name_insured)
            self.fill_date_birth_insured(value.date_birth_insured)
            self.fill_id_insured(value.id_insured)
            self.fill_id_date_insured_input(value.id_dateInsured)

    @allure.step('Нажать кнопку "Перейти к оплате"')
    def click_on_go_to_payments_tab(self):
        self._go_to_payment_button.click()
        self._loader()