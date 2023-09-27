# Third-Party Modules
from requests_html import HTMLSession
# Local Modules
from fakerip import exceptions


class Ripstance:
    def __init__(self, country_code='de'):
        self.url = f'https://fakeit.receivefreesms.co.uk/c/{country_code}/'

        # Personal Details
        self.country = None
        self.name = None
        self.address = None
        self.city = None
        self.postcode = None
        self.gender = None
        self.dob = None
        self.passport = None
        self.passport_expired = None
        self.phone = None
        self.email = None
        self.mothers_maiden_name = None
        self.ethnicity = None
        self.age = None
        self.zodiac_sign = None
        self.height = None
        self.weight = None
        self.hair_color = None
        self.eye_color = None

        # Financial Details
        self.bank_name = None
        self.bank_code = None
        self.account_number = None
        self.iban = None
        self.bic = None
        self.cc_type = None
        self.cc_number = None
        self.cc_expiry = None
        self.cc_cvv2 = None

        # Internet
        self.user_name = None
        self.password = None
        self.ipv4 = None
        self.ipv6 = None
        self.user_agent = None

        # Education
        self.qualification = None
        self.institution = None

        # Employment Details
        self.company_name = None
        self.company_address = None
        self.company_phone = None
        self.company_email = None
        self.job_title = None
        self.salary = None

    def get_info(self):
        session = HTMLSession()
        response = session.get(self.url)

        if response.status_code != 200:
            raise exceptions.RequestDeclined(f'Response status code: {response.status_code}')
