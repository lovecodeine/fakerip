# Third-Party Modules
from requests_html import HTMLSession
# Local Modules
from fakerip import exceptions


class Ripstance:
    def __init__(self, country_code='de'):
        self.url = f'https://fakeit.receivefreesms.co.uk/c/{country_code}/'

        # Personal Details
        self.country = None
        self.full_name = None
        self.address = None
        self.city = None
        self.postcode = None
        self.gender = None
        self.dob = None
        self.passport = None
        self.passport_expired = None
        self.phone = None
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
        self.job_title = None
        self.salary = None

        # Vehicle Details
        self.vehicle = None
        self.license_plate = None
        self.vin = None
        self.vehicle_color = None

        # Custom
        self.forename = None
        self.surname = None
        self.dob_day = None
        self.dob_month = None
        self.dob_year = None
        self.email = None

    def get_info(self):
        session = HTMLSession()
        response = session.get(self.url)

        if response.status_code != 200:
            raise exceptions.RequestDeclined(f'Response status code: {response.status_code}')

        tr_elements = response.html.find('tr')

        for tr in tr_elements:
            data = tr.find('th')
            value = tr.find('span')
            data_left = data[0].text.lower()
            data_right = data[1].text.lower() if len(data) > 1 else None
            value_left = value[0].text
            value_right = value[1].text if len(value) > 1 else None

            # Left column
            if data_left == 'country':
                self.country = value_left
            elif data_left == 'address':
                self.address = value_left
            elif data_left == 'city':
                self.city = value_left.capitalize()
            elif data_left == 'gender':
                self.gender = value_left
            elif data_left == 'passport':
                self.passport = value_left
            elif data_left == 'phone':
                self.phone = value_left
            elif data_left == 'mother\'s maiden name':
                self.mothers_maiden_name = value_left
            elif data_left == 'age (years)':
                self.age = value_left
            elif data_left == 'height':
                self.height = value_left
            elif data_left == 'hair color':
                self.hair_color = value_left
            elif data_left == 'bank name':
                self.bank_name = value_left
            elif data_left == 'bic':
                self.bic = value_left
            elif data_left == 'iban':
                self.iban = value_left
            elif data_left == 'credit card type':
                self.cc_type = value_left
            elif data_left == 'credit card expiry':
                self.cc_expiry = value_left
            elif data_left == 'user name':
                self.user_name = value_left
            elif data_left == 'ipv4 address':
                self.ipv4 = value_left
            elif data_left == 'user agent':
                self.user_agent = value_left
            elif data_left == 'qualification':
                self.qualification = value_left
            elif data_left == 'company name':
                self.company_name = value_left
            elif data_left == 'company address':
                self.company_address = value_left
            elif data_left == 'company phone':
                self.company_phone = value_left
            elif data_left == 'vehicle':
                self.vehicle = value_left
            elif data_left == 'vin':
                self.vin = value_left

            # Right column
            if data_right == 'name':
                self.full_name = value_right
                splitted_name = value_right.split(' ')
                self.forename = splitted_name[0]
                self.surname = splitted_name[1]
            elif data_right == 'postcode':
                self.postcode = value_right
            elif data_right == 'date of birth':
                self.dob = value_right
                splitted_dob = value_right.split(' ')
                self.dob_day = splitted_dob[0]
                self.dob_month = splitted_dob[1]
                self.dob_year = splitted_dob[2]
            elif data_right == 'passport expired':
                self.passport_expired = value_right
            elif data_right == 'ethnicity':
                self.ethnicity = value_right
            elif data_right == 'zodiac sign':
                self.zodiac_sign = value_right
            elif data_right == 'weight':
                self.weight = value_right
            elif data_right == 'eye color':
                self.eye_color = value_right
            elif data_right == 'bank code':
                self.bank_code = value_right
            elif data_right == 'account number':
                self.account_number = value_right
            elif data_right == 'credit card number':
                self.cc_number = value_right
            elif data_right == 'credit card cvv2':
                self.cc_cvv2 = value_right
            elif data_right == 'password':
                self.password = value_right
            elif data_right == 'ipv6 address':
                self.ipv6 = value_right
            elif data_right == 'institution':
                self.institution = value_right
            elif data_right == 'salary':
                self.salary = value_right
            elif data_right == 'job title':
                self.job_title = value_right
            elif data_right == 'license plate':
                self.license_plate = value_right
            elif data_right == 'color':
                self.vehicle_color = value_right

    def __str__(self):
        attributes = [f'{attr}: {getattr(self, attr)}' for attr in vars(self)]
        return '\n'.join(attributes)
