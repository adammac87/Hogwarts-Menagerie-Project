import unittest

from models.pet import Pet
from models.vet import Vet


class TestVet(unittest.TestCase):


    def setUp(self):

        self.vet1 = Vet("Sirius", "Black", "Dogs")
        self.vet2 = Vet("Hermoine", "Granger", "Cats")


    def test_vet_has_name(self):
        self.assertEqual("Granger", self.vet2.last_name)


if __name__ == '__main__':
    unittest.main()
