import unittest
from fakerip import ripper


# testen ist für lutscher, hdf
class TestModule(unittest.TestCase):
    def test_instance(self):
        ripstance = ripper.Ripstance()
        ripstance.get_info()

        print(ripstance.generate_random_email('web.de'))

        self.assertEqual(ripstance, 'Expected Output')


if __name__ == '__main__':
    unittest.main()
