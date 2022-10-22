from dataclasses import dataclass
from datetime import datetime

from core.common.base_builder import BaseBuilder
from core.utils.data_helper import data_helper


@dataclass
class FormData:
    fio: str | None
    birthday: str | None
    doc_data: str | None
    doc_issue_date: str | None
    registration_address: str | None
    phone: str | None
    email: str | None
    add_person: bool
    name_insured: str | None
    date_birth_insured: str | None
    id_insured: str | None
    id_dateInsured: str | None


class FormDataBuilder(BaseBuilder):
    """Генерация данных страхователя."""

    def __init__(self):
        super().__init__()
        self._fio: str | None = None
        self._birthday: str | None = None
        self._doc_data: str | None = None
        self._doc_issue_date: str | None = None
        self._registration_address: str | None = None
        self._phone: str | None = None
        self._email: str | None = None
        self._add_person: bool = True
        self._name_insured: str | None = None
        self._date_birth_insured: str | None = None
        self._id_insured: str | None = None
        self._id_date_insured: str | None = None

    def with_fio(self, value: str):
        self._fio = value
        return self

    def with_random_fio(self):
        self._fio = self._faker.name()

    def with_birthday(self, value: str):
        self._birthday = value
        return self

    def with_random_birthday(self):
        self._birthday = data_helper.get_random_date(datetime.strptime('1/1/1970', '%m/%d/%Y'),
                                                     datetime.strptime('1/1/2002', '%m/%d/%Y'))

    def with_doc_data(self, value: str):
        self._doc_data = value
        return self

    def with_random_doc_data(self):
        doc_data = f'{self.random_number(end=9999)}-{self.random_number(start=100000, end=999999)}'
        self._doc_data = doc_data

    def with_doc_issue_date(self, value: str):
        self._doc_issue_date = value
        return self

    def with_random_doc_issue_date(self):
        self._doc_issue_date = data_helper.get_random_date(datetime.strptime('1/1/2010', '%m/%d/%Y'),
                                                           datetime.strptime('1/1/2018', '%m/%d/%Y'))

    def with_doc_registration_address(self, value: str):
        self._registration_address = value
        return self

    def with_random_registration_address(self):
        self._registration_address = self._faker.address()

    def with_phone(self, value: str):
        self._phone = value
        return self

    def with_random_phone(self):
        self._phone = self.phone(mask='+7(xxx)-xxx-xx-xx')

    def with_doc_email(self, value: str):
        self._email = value
        return self

    def with_random_email(self):
        self._email = self._faker.company_email()

    def without_add_person(self):
        self._add_person = False

    def with_doc_name_insured(self, value: str):
        self._name_insured = value
        return self

    def with_random_name_insured(self):
        self._name_insured = self._faker.name()

    def with_date_birth_insured(self, value: str):
        self._date_birth_insured = value
        return self

    def with_random_date_birth_insured(self):
        self._date_birth_insured = data_helper.get_random_date(datetime.strptime('1/1/1970', '%m/%d/%Y'),
                                                               datetime.strptime('1/1/2002', '%m/%d/%Y'))

    def with_id_insured(self, value: str):
        self._id_insured = value
        return self

    def with_random_id_insured(self):
        doc_data = f'{self.random_number(end=9999)}-{self.random_number(start=100000, end=999999)}'
        self._id_insured = doc_data

    def with_id_date_insured(self, value: str):
        self._id_date_insured = value
        return self

    def with_random_id_date_insured(self):
        self._id_date_insured = data_helper.get_random_date(datetime.strptime('1/1/2010', '%m/%d/%Y'),
                                                            datetime.strptime('1/1/2018', '%m/%d/%Y'))

    def random_with_add_person(self):
        """Случайные значения для всех полей формы. Страхователь является застрахованным."""
        self.with_random_fio()
        self.with_random_birthday()
        self.with_random_doc_data()
        self.with_random_doc_issue_date()
        self.with_random_registration_address()
        self.with_random_phone()
        self.with_random_email()
        return self

    def random_without_add_person(self):
        """Случайные значения для всех полей формы. Страхователь не является застрахованным."""
        self.with_random_fio()
        self.with_random_birthday()
        self.with_random_doc_data()
        self.with_random_doc_issue_date()
        self.with_random_registration_address()
        self.with_random_phone()
        self.with_random_email()
        self.without_add_person()
        self.with_random_name_insured()
        self.with_random_date_birth_insured()
        self.with_random_id_insured()
        self.with_random_id_date_insured()
        return self

    def build(self):
        return FormData(
            fio=self._fio,
            birthday=self._birthday,
            doc_data=self._doc_data,
            doc_issue_date=self._doc_issue_date,
            registration_address=self._registration_address,
            phone=self._phone,
            email=self._email,
            add_person=self._add_person,
            name_insured=self._name_insured,
            date_birth_insured=self._date_birth_insured,
            id_insured=self._id_insured,
            id_dateInsured=self._id_date_insured
        )
