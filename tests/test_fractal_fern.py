import unittest
from fractal_fern import FractalFern

class TestFractalFernOO(unittest.TestCase):
    def test_generate_fractal_fern_points_length(self):
        """Test that the correct number of points are generated."""
        points = 10000
        fern = FractalFern(points=points)
        fern.generate_points()
        self.assertEqual(len(fern.x_points), points)
        self.assertEqual(len(fern.y_points), points)

    def test_generate_fractal_fern_points_type(self):
        """Test the types of the generated points."""
        fern = FractalFern(points=6000)
        fern.generate_points()
        self.assertIsInstance(fern.x_points, list)
        self.assertIsInstance(fern.y_points, list)
        self.assertTrue(all(isinstance(x, float) for x in fern.x_points))
        self.assertTrue(all(isinstance(y, float) for y in fern.y_points))

    def test_generate_fractal_fern_points_zero(self):
        """Test generating zero points."""
        fern = FractalFern(points=0)
        fern.generate_points()
        self.assertEqual(len(fern.x_points), 5000)
        self.assertEqual(len(fern.y_points), 5000)

    def test_generate_fractal_fern_points_negative(self):
        """Test that a negative points value raises a ValueError."""
        with self.assertRaises(ValueError):
            FractalFern(points=-100)

    def test_generate_fractal_fern_points_less_than_5000(self):
        """Test that requesting less than 5000 points generates 3000 points by default."""
        fern = FractalFern(points=999)
        fern.generate_points()
        self.assertEqual(len(fern.x_points), 5000)
        self.assertEqual(len(fern.y_points), 5000)

if __name__ == '__main__':
    unittest.main()
