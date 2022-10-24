from aenum import Enum


class PageData(Enum, init='page_title, relative_url'):
    CORONAVIRUS_INSURANCE_POLICY_PAGE = ('Купить полис страхования от коронавируса',
                                         '/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/')
    PAYMENTS_PAGE = ('', 'securepayments.tinkoff.ru/')
