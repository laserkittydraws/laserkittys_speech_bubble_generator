import unittest
import math

from laserkittys_speech_bubble_generator.Shapes.roundBubbleBase import RoundBubbleBase as rb

class RoundMethods(unittest.TestCase):

    def test_radius(self):
        rb.clear()
        with self.assertRaises(ValueError):
            rb.radius(0)
        with self.assertRaises(ValueError):
            rb.radius(2*math.pi/3)
        with self.assertRaises(ValueError):
            rb.radius(5*math.pi/3)

        rb.setWidth(2*8)
        rb.setHeight(2*3)
        self.assertAlmostEqual(rb.radius(0),           8)
        self.assertAlmostEqual(rb.radius(math.pi),     8)
        self.assertAlmostEqual(rb.radius(math.pi/2),   3)
        self.assertAlmostEqual(rb.radius(3*math.pi/2), 3)
        self.assertAlmostEqual(rb.radius(0.7), 4.25422906548)
        self.assertAlmostEqual(rb.radius(2.1), 3.39471779402)
        self.assertAlmostEqual(rb.radius(4.3), 3.23132181507)
        self.assertAlmostEqual(rb.radius(5.9), 5.87499777022)

    def test_radius_deriv(self):
        rb.clear()
        rb.setWidth(0)
        rb.setHeight(0)
        with self.assertRaises(ValueError):
            rb.radiusDeriv(0)
        with self.assertRaises(ValueError):
            rb.radiusDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            rb.radiusDeriv(5*math.pi/3)

        rb.setWidth(2*8)
        rb.setHeight(2*3)
        self.assertAlmostEqual(rb.radiusDeriv(0),           0)
        self.assertAlmostEqual(rb.radiusDeriv(math.pi),     0)
        self.assertAlmostEqual(rb.radiusDeriv(math.pi/2),   0)
        self.assertAlmostEqual(rb.radiusDeriv(3*math.pi/2), 0)
        self.assertAlmostEqual(rb.radiusDeriv(0.7), -3.62249084468)
        self.assertAlmostEqual(rb.radiusDeriv(2.1),  1.62789500403)
        self.assertAlmostEqual(rb.radiusDeriv(4.3),  -1.1829919795)
        self.assertAlmostEqual(rb.radiusDeriv(5.9),  6.71421900277)

    def test_radius_x_deriv(self):
        rb.clear()
        rb.setWidth(0)
        rb.setHeight(0)
        with self.assertRaises(ValueError):
            rb.radiusXDeriv(0)
        with self.assertRaises(ValueError):
            rb.radiusXDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            rb.radiusXDeriv(5*math.pi/3)

        rb.setWidth(2*8)
        rb.setHeight(2*3)
        self.assertAlmostEqual(rb.radiusXDeriv(          0),  0)
        self.assertAlmostEqual(rb.radiusXDeriv(    math.pi),  0)
        self.assertAlmostEqual(rb.radiusXDeriv(  math.pi/2), -3)
        self.assertAlmostEqual(rb.radiusXDeriv(3*math.pi/2),  3)
        self.assertAlmostEqual(rb.radiusXDeriv(0.7), -5.51128343061)
        self.assertAlmostEqual(rb.radiusXDeriv(2.1), -3.75218864841)
        self.assertAlmostEqual(rb.radiusXDeriv(4.3),   3.4345691836)
        self.assertAlmostEqual(rb.radiusXDeriv(5.9),  8.42381787657)

    def test_radius_y_deriv(self):
        rb.clear()
        rb.setWidth(0)
        rb.setHeight(0)
        with self.assertRaises(ValueError):
            rb.radiusYDeriv(0)
        with self.assertRaises(ValueError):
            rb.radiusYDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            rb.radiusYDeriv(5*math.pi/3)

        rb.setWidth(2*8)
        rb.setHeight(2*3)
        self.assertAlmostEqual(rb.radiusYDeriv(          0),  8)
        self.assertAlmostEqual(rb.radiusYDeriv(    math.pi), -8)
        self.assertAlmostEqual(rb.radiusYDeriv(  math.pi/2),  0)
        self.assertAlmostEqual(rb.radiusYDeriv(3*math.pi/2),  0)
        self.assertAlmostEqual(rb.radiusYDeriv(0.7),  0.920141189652)
        self.assertAlmostEqual(rb.radiusYDeriv(2.1), -0.308595839125)
        self.assertAlmostEqual(rb.radiusYDeriv(4.3), -0.211294153135)
        self.assertAlmostEqual(rb.radiusYDeriv(5.9),   2.93864390486)

    def test_radius_x_deriv_norm(self):
        rb.clear()
        rb.setWidth(0)
        rb.setHeight(0)
        with self.assertRaises(ValueError):
            rb.radiusXDerivNorm(0)
        with self.assertRaises(ValueError):
            rb.radiusXDerivNorm(2*math.pi/3)
        with self.assertRaises(ValueError):
            rb.radiusXDerivNorm(5*math.pi/3)

        rb.setWidth(2*8)
        rb.setHeight(2*3)
        self.assertAlmostEqual(rb.radiusXDerivNorm(          0),  0)
        self.assertAlmostEqual(rb.radiusXDerivNorm(    math.pi),  0)
        self.assertAlmostEqual(rb.radiusXDerivNorm(  math.pi/2), -1)
        self.assertAlmostEqual(rb.radiusXDerivNorm(3*math.pi/2),  1)
        self.assertAlmostEqual(rb.radiusXDerivNorm(0.7), -0.986347625189)
        self.assertAlmostEqual(rb.radiusXDerivNorm(2.1), -0.996635005221)
        self.assertAlmostEqual(rb.radiusXDerivNorm(4.3),  0.998113009099)
        self.assertAlmostEqual(rb.radiusXDerivNorm(5.9),  0.94419659849)

    def test_radius_y_deriv_norm(self):
        rb.clear()
        rb.setWidth(0)
        rb.setHeight(0)
        with self.assertRaises(ValueError):
            rb.radiusXDerivNorm(0)
        with self.assertRaises(ValueError):
            rb.radiusXDerivNorm(2*math.pi/3)
        with self.assertRaises(ValueError):
            rb.radiusXDerivNorm(5*math.pi/3)

        rb.setWidth(2*8)
        rb.setHeight(2*3)
        self.assertAlmostEqual(rb.radiusYDerivNorm(          0),  1)
        self.assertAlmostEqual(rb.radiusYDerivNorm(    math.pi), -1)
        self.assertAlmostEqual(rb.radiusYDerivNorm(  math.pi/2),  0)
        self.assertAlmostEqual(rb.radiusYDerivNorm(3*math.pi/2),  0)
        self.assertAlmostEqual(rb.radiusYDerivNorm(0.7),   0.164676538356)
        self.assertAlmostEqual(rb.radiusYDerivNorm(2.1), -0.0819674714031)
        self.assertAlmostEqual(rb.radiusYDerivNorm(4.3),  -0.061403754508)
        self.assertAlmostEqual(rb.radiusYDerivNorm(5.9),   0.329382427278)

if __name__ == '__main__':
    unittest.main()