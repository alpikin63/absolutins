import pytest

from core.pages.coronavirus_insurance_policy_page import CoronavirusInsurancePolicyPage

__all__ = [
    'open_policy_purchase_form',
    'open_policy_purchase_form_go_to_data_tab'
]


@pytest.fixture(scope='function')
def open_policy_purchase_form():
    """Открыть страницу формы покупки полиса"""
    def _open():
        return CoronavirusInsurancePolicyPage()
    return _open


@pytest.fixture(scope='function')
def open_policy_purchase_form_go_to_data_tab(open_policy_purchase_form):
    """Открыть страницу формы покупки полиса заполнить форму расчета и перейти на вкладку ввода данных"""
    def _open(change_sum: bool = False):
        policy_form_page = open_policy_purchase_form()
        if change_sum:
            policy_form_page.select_sum_insured()
        policy_form_page.fill_virus_contact_checkbox()
        policy_form_page.click_on_continue_btn()
        return CoronavirusInsurancePolicyPage(do_open=False)
    return _open
