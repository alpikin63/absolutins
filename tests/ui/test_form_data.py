import allure
from core.common.utils.pytest_marks import regress, web_browser
from core.data.builders.form_data_builder import FormDataBuilder
from core.data.step_name_data import StepNameData
from datetime import datetime, timedelta


@allure.parent_suite('Регрессионное тестирование')
@allure.suite('Форма покупки полиса')
@allure.sub_suite('Ввод данных')
@web_browser
@regress
class TestCalculateForm:

    @allure.title('Переход на вкладку Оплата. Страхователь является застрахованным. Страховая сумма 500000')
    def test_open_payment_form(self, open_policy_purchase_form_go_to_data_tab):
        test_data = FormDataBuilder().random_with_add_person().build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab()
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_PAYMENT)

    @allure.title('Переход на вкладку Оплата. Страхователь не является застрахованным. Страховая сумма 500000.'
                  'Застрахованный имеет паспорт')
    def test_open_payment_form_add_person_with_passport(self, open_policy_purchase_form_go_to_data_tab):
        test_data = FormDataBuilder().random_without_add_person().build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab()
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_PAYMENT)

    @allure.title('Переход на вкладку Оплата. Страхователь не является застрахованным. Страховая сумма 500000.'
                  'Застрахованный не имеет паспорт')
    def test_open_payment_form_add_person_without_passport(self, open_policy_purchase_form_go_to_data_tab):
        start_date = datetime.now()
        result_date = start_date - timedelta(days=1096)

        test_data = FormDataBuilder() \
            .random_without_add_person() \
            .but() \
            .with_date_birth_insured(result_date.strftime('%d.%m.%Y')) \
            .with_id_insured(None) \
            .with_id_date_insured(None) \
            .build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab()
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_PAYMENT)

    @allure.title('Переход на вкладку Оплата. Страхователь является застрахованным. Страховая сумма 100000')
    def test_open_payment_form_change_sum(self, open_policy_purchase_form_go_to_data_tab):
        test_data = FormDataBuilder().random_with_add_person().build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab(change_sum=True)
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_PAYMENT)

    @allure.title('Переход на вкладку Оплата. Страхователь не является застрахованным. Страховая сумма 100000.'
                  'Застрахованный имеет паспорт')
    def test_open_payment_form_add_person_with_passport_change_sum(self, open_policy_purchase_form_go_to_data_tab):
        test_data = FormDataBuilder().random_without_add_person().build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab(change_sum=True)
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_PAYMENT)

    @allure.title('Переход на вкладку Оплата. Страхователь не является застрахованным. Страховая сумма 100000.'
                  'Застрахованный не имеет паспорт')
    def test_open_payment_form_add_person_without_passport_change_sum(self, open_policy_purchase_form_go_to_data_tab):
        start_date = datetime.now()
        result_date = start_date - timedelta(days=1096)

        test_data = FormDataBuilder() \
            .random_without_add_person() \
            .but() \
            .with_date_birth_insured(result_date.strftime('%d.%m.%Y')) \
            .with_id_insured(None) \
            .with_id_date_insured(None) \
            .build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab(change_sum=True)
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_PAYMENT)

    @allure.title('Переход на вкладку Оплата. Страхователь является застрахованным. Страховая сумма 500000'
                  'Не заполнено ни одно поле.')
    def test_open_payment_form_empty_data(self, open_policy_purchase_form_go_to_data_tab):
        test_data = FormDataBuilder().build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab()
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_INPUT_DATA)

    @allure.title('Переход на вкладку Оплата. Страхователь является застрахованным. Страховая сумма 500000'
                  'Не заполнено 1 поле')
    def test_open_payment_form_one_empty_field(self, open_policy_purchase_form_go_to_data_tab):
        test_data = FormDataBuilder().random_with_add_person().but() \
            .with_doc_email(None) \
            .build()

        policy_form_page = open_policy_purchase_form_go_to_data_tab()
        policy_form_page.fill_form_data(test_data)
        policy_form_page.click_on_go_to_payments_tab()
        policy_form_page.assure_current_step_name(StepNameData.STEP_INPUT_DATA)

