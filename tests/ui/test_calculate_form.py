import allure
from core.common.utils.pytest_marks import regress, web_browser
from core.data.step_name_data import StepNameData


@allure.parent_suite('Регрессионное тестирование')
@allure.suite('Форма покупки полиса')
@allure.sub_suite('Расчет')
@web_browser
@regress
class TestCalculateForm:

    @allure.title('Переход на вкладку ввода данных. Страховая сумма полиса: 500000')
    def test_open_data_form(self, open_policy_purchase_form):
        policy_form_page = open_policy_purchase_form()
        policy_form_page.fill_virus_contact_checkbox()
        policy_form_page.click_on_continue_btn()
        policy_form_page.assure_current_step_name(StepNameData.STEP_INPUT_DATA)

    @allure.title('Чекбокс "Профессиональная сфера связана с медицинской деятельностью" выбран. '
                  'Страховая сумма полиса: 500000')
    def test_open_continue_button_disabled(self, open_policy_purchase_form):
        policy_form_page = open_policy_purchase_form()
        policy_form_page.fill_medicine_checkbox()
        policy_form_page.assure_continue_btn_disabled()

    @allure.title('Переход на вкладку ввода данных. Страховая сумма полиса: 100000')
    def test_open_data_form_change_insure_sum(self, open_policy_purchase_form):
        policy_form_page = open_policy_purchase_form()
        policy_form_page.select_sum_insured(100_000)
        policy_form_page.fill_virus_contact_checkbox()
        policy_form_page.click_on_continue_btn()
        policy_form_page.assure_current_step_name(StepNameData.STEP_INPUT_DATA)

    @allure.title('Чекбокс "Профессиональная сфера связана с медицинской деятельностью" выбран.'
                  ' Страховая сумма полиса: 100000')
    def test_open_continue_button_disabled_change_insure_sum(self, open_policy_purchase_form):
        policy_form_page = open_policy_purchase_form()
        policy_form_page.select_sum_insured(100_000)
        policy_form_page.fill_medicine_checkbox()
        policy_form_page.assure_continue_btn_disabled()

    @allure.title('Выбраны оба чекбокса. Страховая сумма полиса: 100000')
    def test_open_continue_button_disabled_change_insure_sum_all_checkbox(self, open_policy_purchase_form):
        policy_form_page = open_policy_purchase_form()
        policy_form_page.select_sum_insured(100_000)
        policy_form_page.fill_medicine_checkbox()
        policy_form_page.fill_virus_contact_checkbox()
        policy_form_page.assure_continue_btn_disabled()

    @allure.title('Выбраны оба чекбокса. Страховая сумма полиса: 500000')
    def test_open_continue_button_disabled_all_checkbox(self, open_policy_purchase_form):
        policy_form_page = open_policy_purchase_form()
        policy_form_page.fill_medicine_checkbox()
        policy_form_page.fill_virus_contact_checkbox()
        policy_form_page.assure_continue_btn_disabled()
