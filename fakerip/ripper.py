# Standard Library
import random
from typing import List, Union
# Third-Party Library
from requests_html import HTMLSession
# Local Modules
from fakerip import exceptions


class Ripstance:
    # Define the attributes this class will use.
    __slots__: List[str] = [
        'url', 'country', 'full_name', 'address', 'city', 'postcode', 'gender',
        'dob', 'passport', 'passport_expired', 'phone', 'mothers_maiden_name',
        'ethnicity', 'age', 'zodiac_sign', 'height', 'weight', 'hair_color',
        'eye_color', 'bank_name', 'bank_code', 'account_number', 'iban', 'bic',
        'cc_type', 'cc_number', 'cc_expiry', 'cc_cvv2', 'user_name', 'password',
        'ipv4', 'ipv6', 'user_agent', 'qualification', 'institution', 'company_name',
        'company_address', 'company_phone', 'job_title', 'salary', 'vehicle',
        'license_plate', 'vin', 'vehicle_color', 'forename', 'surname', 'dob_day',
        'dob_month', 'dob_year'
    ]

    def __init__(self, country_code: str = 'de') -> None:
        # Construct the URL based on the country code.
        self.url = f'https://fakeit.receivefreesms.co.uk/c/{country_code}/'

    def get_info(self) -> None:
        """Fetch the content from the URL and parse the relevant data."""
        response = self._fetch_content()
        tr_elements = response.html.find('tr')
        self._parse_data_from_elements(tr_elements)

    def _fetch_content(self):
        """Make a GET request to the given URL and return the response."""
        session = HTMLSession()
        # session.headers.update({'User-Agent': 'Mozilla/5.0'})

        response = session.get(self.url)
        if response.status_code != 200:
            raise exceptions.RequestDeclined(f'Response status code: {response.status_code}')
        return response

    def _parse_data_from_elements(self, elements) -> None:
        """Parse and extract the data from the provided elements."""
        for tr in elements:
            data = tr.find('th')
            value = tr.find('span')
            self._extract_data(data[0].text.lower(), value[0].text)
            if len(data) > 1 and len(value) > 1:
                self._extract_data(data[1].text.lower(), value[1].text)

    def _extract_data(self, key: str, value: str) -> None:
        """
        Mapping from the scraped keys to the internal attribute names.
        If a value is callable (a function/method), it will be called with 'value' as an argument.
        Otherwise, the attribute with the corresponding name is set to 'value'.
        """
        mapping = {
            'country': 'country',
            'address': 'address',
            'city': 'city',
            'gender': 'gender',
            'passport': 'passport',
            'phone': 'phone',
            'mother\'s maiden name': 'mothers_maiden_name',
            'age (years)': 'age',
            'height': 'height',
            'hair color': 'hair_color',
            'bank name': 'bank_name',
            'bic': 'bic',
            'iban': 'iban',
            'credit card type': 'cc_type',
            'credit card expiry': 'cc_expiry',
            'user name': 'user_name',
            'ipv4 address': 'ipv4',
            'user agent': 'user_agent',
            'qualification': 'qualification',
            'company name': 'company_name',
            'company address': 'company_address',
            'company phone': 'company_phone',
            'vehicle': 'vehicle',
            'vin': 'vin',
            'postcode': 'postcode',
            'passport expired': 'passport_expired',
            'ethnicity': 'ethnicity',
            'zodiac sign': 'zodiac_sign',
            'weight': 'weight',
            'eye color': 'eye_color',
            'bank code': 'bank_code',
            'account number': 'account_number',
            'credit card number': 'cc_number',
            'credit card cvv2': 'cc_cvv2',
            'password': 'password',
            'ipv6 address': 'ipv6',
            'institution': 'institution',
            'salary': 'salary',
            'job title': 'job_title',
            'license plate': 'license_plate',
            'color': 'vehicle_color',
            'name': self._split_full_name,
            'date of birth': self._split_dob,
        }

        if key in mapping:
            target = mapping[key]
            if callable(target):  # if the target is a method, call it
                target(value)
            else:
                setattr(self, target, value)

    def _split_full_name(self, full_name: str) -> None:
        """Split the full name into forename and surname."""
        self.full_name = full_name
        splitted_name = full_name.split(' ')
        self.forename = splitted_name[0]
        self.surname = splitted_name[1] if len(splitted_name) > 1 else None  # safe check in case there's no surname

    def _split_dob(self, dob: str) -> None:
        """Split the date of birth into day, month, and year."""
        self.dob = dob
        splitted_dob = dob.split(' ')
        self.dob_day = splitted_dob[0]
        self.dob_month = splitted_dob[1]
        self.dob_year = splitted_dob[2] if len(splitted_dob) > 2 else None  # safe check in case the format changes

    def generate_random_email(self, domain: Union[str, None] = None) -> str:
        """
        Generate a random email based on the forename, surname, and a random selection from dob_year.
        The email is also sanitized to replace certain characters.
        """
        if not (self.forename and self.surname and self.dob_year):
            self.get_info()

        # Random choice for the dob_year index
        index = random.choice([-2, -3])
        base_email = f"{self.forename.lower()}_{self.surname.lower()}{self.dob_year[index:]}"
        sanitized_email = self._sanitize_email(base_email)

        return f"{sanitized_email}@{domain}" if domain else sanitized_email

    @staticmethod
    def _sanitize_email(email: str) -> str:
        """Replace certain characters in the email to make it valid."""
        replacements = {'ä': 'ae', 'ö': 'oe', 'ü': 'ue'}
        for key, value in replacements.items():
            email = email.replace(key, value)
        return email

    def __str__(self) -> str:
        """Define the string representation of the object, listing all attributes and their values"""
        return '\n'.join([f'{attr}: {getattr(self, attr)}' for attr in self.__slots__])