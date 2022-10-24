from core.data.page_data import PageData
from core.pages.base_app_page import BaseAppPage


class PaymentsPage(BaseAppPage):
    def __init__(self):
        super().__init__()
        self.assure_current_page_url_contains_text(PageData.PAYMENTS_PAGE.relative_url)
