import unittest
import math

from laserkittys_speech_bubble_generator.Shapes.squareBubbleBase import SquareBubbleBase as sb

class SquareMethods(unittest.TestCase):

    def test_radiusX(self):
        with self.assertRaises(ValueError):
            sb.radiusX(0)
        with self.assertRaises(ValueError):
            sb.radiusX(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusX(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusX(0),           8)
        self.assertAlmostEqual(sb.radiusX(math.pi),    -8)
        self.assertAlmostEqual(sb.radiusX(math.pi/2),   0)
        self.assertAlmostEqual(sb.radiusX(3*math.pi/2), 0)
        self.assertAlmostEqual(sb.radiusX(0.7),  6.09802775277)
        self.assertAlmostEqual(sb.radiusX(2.1), -3.70591674169)
        self.assertAlmostEqual(sb.radiusX(4.3), -2.88788476701)
        self.assertAlmostEqual(sb.radiusX(5.9),              8)
        sb.clear()

    def test_radiusY(self):
        with self.assertRaises(ValueError):
            sb.radiusY(0)
        with self.assertRaises(ValueError):
            sb.radiusY(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusY(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusY(0),            0)
        self.assertAlmostEqual(sb.radiusY(math.pi),      0)
        self.assertAlmostEqual(sb.radiusY(math.pi/2),    3)
        self.assertAlmostEqual(sb.radiusY(3*math.pi/2), -3)
        self.assertAlmostEqual(sb.radiusY(0.7),              3)
        self.assertAlmostEqual(sb.radiusY(2.1),              3)
        self.assertAlmostEqual(sb.radiusY(4.3),             -3)
        self.assertAlmostEqual(sb.radiusY(5.9), -2.68337677334)
        sb.clear()

    def test_radius_x_deriv_norm(self):
        sb.setWidth(0)
        sb.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusXDerivNorm(          0),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(    math.pi),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(  math.pi/2), -1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(3*math.pi/2),  1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(0.7), -1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(2.1), -1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(4.3),  1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(5.9),  0)
        sb.clear()

    def test_radius_y_deriv_norm(self):
        sb.setWidth(0)
        sb.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusYDerivNorm(          0),  1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(    math.pi), -1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(  math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(3*math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(0.7), 0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(2.1), 0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(4.3), 0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(5.9), 1)
        sb.clear()

if __name__ == '__main__':
    unittest.main()