import unittest
from bt2 import add_to_order, view_order, current_order, InvalidQuantityError

class TestHighlandsPOS(unittest.TestCase):
    def setUp(self):
        current_order.clear()

    def test_calculate_total(self):
        add_to_order("P1", 2)
        add_to_order("F1", 1)
        result = view_order()
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        with self.assertRaises(InvalidQuantityError):
            add_to_order("T1", -1)

if __name__ == "__main__":
    unittest.main()
