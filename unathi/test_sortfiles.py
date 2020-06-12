import unittest
from sortfiles import Footwear


class SortingTest(unittest.TestCase):

    def setUp(self):
        self.list = [['Vans', 'Blue', 10.00],
                     ['Nike', 'Red', 20.00],
                     ['Nike', 'Green', 10.00],
                     ['New Balance', 'White', 50.00],
                     ['Adidas', 'Blue', 30.00]]
        self.class_t = Footwear()
        self.amnt = self.class_t.sort_amount(self.list)
        self.col = self.class_t.sort_color(self.list)
        self.prod = self.class_t.sort_products(self.list)

    def test_list_equal_amnt(self):
        self.assertNotEqual(self.list, self.amnt)

    def test_list_equal_color(self):
        self.assertNotEqual(self.list, self.col)

    def test_list_equal_prdct(self):
        self.assertNotEqual(self.list, self.prod)

    def test_prod_sorted(self):
        sorted_by_prod = [['Vans', 'Blue', 10.0],
                          ['Nike', 'Green', 10.0],
                          ['Nike', 'Red', 20.0],
                          ['Adidas', 'Blue', 30.0],
                          ['New Balance', 'White', 50.0]]
        prod_functn_output = self.class_t.sort_products(self.list)
        self.assertTrue(prod_functn_output, sorted_by_prod)
        self.assertEqual(prod_functn_output, sorted_by_prod)

    def test_color_sorted(self):
        sorted_by_color = [['Vans', 'Blue', 10.0],
                           ['Nike', 'Green', 10.0],
                           ['Nike', 'Red', 20.0],
                           ['Adidas', 'Blue', 30.0],
                           ['New Balance', 'White', 50.0]]
        color_functn_output = self.class_t.sort_color(self.list)
        self.assertTrue(color_functn_output, sorted_by_color)
        self.assertEqual(color_functn_output, sorted_by_color)

    def test_amount_sorted(self):
        sorted_by_amount = [['New Balance', 'White', 50.0],
                            ['Adidas', 'Blue', 30.0],
                            ['Nike', 'Red', 20.0],
                            ['Vans', 'Blue', 10.0],
                            ['Nike', 'Green', 10.0]]
        amount_functn_output = self.class_t.sort_amount(self.list)
        self.assertTrue(amount_functn_output, sorted_by_amount)
        self.assertEqual(amount_functn_output, sorted_by_amount)


if __name__ == '__main__':
    unittest.main()