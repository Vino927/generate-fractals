import unittest
from fractal_fern import generate_fractal_fern_points

class TestFractalFern(unittest.TestCase):
    def test_generate_fractal_fern_points_length(self):
        points = 10000
        x_list, y_list = generate_fractal_fern_points(points)
        self.assertEqual(len(x_list), points)
        self.assertEqual(len(y_list), points)

    def test_generate_fractal_fern_points_type(self):
        x_list, y_list = generate_fractal_fern_points(6000)
        self.assertIsInstance(x_list, list)
        self.assertIsInstance(y_list, list)
        self.assertTrue(all(isinstance(x, float) for x in x_list))
        self.assertTrue(all(isinstance(y, float) for y in y_list))

    def test_generate_fractal_fern_points_zero(self):
        x_list, y_list = generate_fractal_fern_points(0)
        self.assertEqual(len(x_list), 0)
        self.assertEqual(len(y_list), 0)

    def test_generate_fractal_fern_points_negative(self):
        with self.assertRaises(ValueError):
            generate_fractal_fern_points(-100)

    def test_generate_fractal_fern_points_less_than_3000(self):
        # Assuming the default behavior is to generate 3000 points
        x_list, y_list = generate_fractal_fern_points(999)
        self.assertEqual(len(x_list), 3000)
        self.assertEqual(len(y_list), 3000)

if __name__ == '__main__':
    unittest.main()
