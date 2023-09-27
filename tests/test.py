import unittest
from fakerip import ripper


class TestModule(unittest.TestCase):
    def test_instance(self):
        ripstance = ripper.Ripstance().get_info()

        self.assertEqual(ripstance, 'Expected Output')


if __name__ == '__main__':
    unittest.main()
