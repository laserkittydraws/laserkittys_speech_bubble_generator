import unittest
import math

from laserkittys_speech_bubble_generator.Shapes.squircleBubbleBase import SquircleBubbleBase as sb

class SquircleMethods(unittest.TestCase):

    def test_radius(self):
        with self.assertRaises(ValueError):
            sb.radius(0)
        with self.assertRaises(ValueError):
            sb.radius(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radius(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radius(0),8)
        self.assertAlmostEqual(sb.radius(math.pi),8)
        self.assertAlmostEqual(sb.radius(math.pi/2),3)
        self.assertAlmostEqual(sb.radius(3*math.pi/2),3)
        self.assertAlmostEqual(sb.radius(0.7), 4.49549306514)
        self.assertAlmostEqual(sb.radius(2.1), 3.45783661669)
        self.assertAlmostEqual(sb.radius(4.3), 3.26713555143)
        self.assertAlmostEqual(sb.radius(5.9), 6.48314778284)

        sb.setWidth(2*273)
        sb.setHeight(2*187)
        self.assertAlmostEqual(sb.radius(0),273)
        self.assertAlmostEqual(sb.radius(math.pi),273)
        self.assertAlmostEqual(sb.radius(math.pi/2),187)
        self.assertAlmostEqual(sb.radius(3*math.pi/2),187)
        self.assertAlmostEqual(sb.radius(0.7), 247.617691377)
        self.assertAlmostEqual(sb.radius(2.1), 210.955550159)
        self.assertAlmostEqual(sb.radius(4.3), 201.67178883)
        self.assertAlmostEqual(sb.radius(5.9), 273.638606804)

    def test_radius_deriv(self):
        sb.setWidth(0)
        sb.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusDeriv(0)
        with self.assertRaises(ValueError):
            sb.radiusDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusDeriv(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusDeriv(0),0)
        self.assertAlmostEqual(sb.radiusDeriv(math.pi),0)
        self.assertAlmostEqual(sb.radiusDeriv(math.pi/2),0)
        self.assertAlmostEqual(sb.radiusDeriv(3*math.pi/2),0)
        self.assertAlmostEqual(sb.radiusDeriv(0.7), -4.47961020301)
        self.assertAlmostEqual(sb.radiusDeriv(2.1),  1.91052533268)
        self.assertAlmostEqual(sb.radiusDeriv(4.3),  -1.3732509483)
        self.assertAlmostEqual(sb.radiusDeriv(5.9),  7.67749282856)

        sb.setWidth(2*273)
        sb.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusDeriv(0),0)
        self.assertAlmostEqual(sb.radiusDeriv(math.pi),0)
        self.assertAlmostEqual(sb.radiusDeriv(math.pi/2),0)
        self.assertAlmostEqual(sb.radiusDeriv(3*math.pi/2),0)
        self.assertAlmostEqual(sb.radiusDeriv(0.7), -113.467789151)
        self.assertAlmostEqual(sb.radiusDeriv(2.1),  88.6840155514)
        self.assertAlmostEqual(sb.radiusDeriv(4.3),  -70.042214882)
        self.assertAlmostEqual(sb.radiusDeriv(5.9),  35.4822890108)

    def test_radius_x_deriv(self):
        sb.setWidth(0)
        sb.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusXDeriv(0)
        with self.assertRaises(ValueError):
            sb.radiusXDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusXDeriv(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusXDeriv(          0),  0)
        self.assertAlmostEqual(sb.radiusXDeriv(    math.pi),  0)
        self.assertAlmostEqual(sb.radiusXDeriv(  math.pi/2), -3)
        self.assertAlmostEqual(sb.radiusXDeriv(3*math.pi/2),  3)
        self.assertAlmostEqual(sb.radiusXDeriv(0.7), -6.32227101127)
        self.assertAlmostEqual(sb.radiusXDeriv(2.1), -3.94935822781)
        self.assertAlmostEqual(sb.radiusXDeriv(4.3),   3.5436361461)
        self.assertAlmostEqual(sb.radiusXDeriv(5.9),  9.54460667133)

        sb.setWidth(2*273)
        sb.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusXDeriv(          0),    0)
        self.assertAlmostEqual(sb.radiusXDeriv(    math.pi),    0)
        self.assertAlmostEqual(sb.radiusXDeriv(  math.pi/2), -187)
        self.assertAlmostEqual(sb.radiusXDeriv(3*math.pi/2),  187)
        self.assertAlmostEqual(sb.radiusXDeriv(0.7), -246.304648499)
        self.assertAlmostEqual(sb.radiusXDeriv(2.1), -226.870586635)
        self.assertAlmostEqual(sb.radiusXDeriv(4.3),  212.837685065)
        self.assertAlmostEqual(sb.radiusXDeriv(5.9),  135.216147412)

    def test_radius_y_deriv(self):
        sb.setWidth(0)
        sb.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusYDeriv(0)
        with self.assertRaises(ValueError):
            sb.radiusYDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusYDeriv(5*math.pi/3)

        sb.setWidth(2*8)
        sb.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusYDeriv(          0),  8)
        self.assertAlmostEqual(sb.radiusYDeriv(    math.pi), -8)
        self.assertAlmostEqual(sb.radiusYDeriv(  math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDeriv(3*math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDeriv(0.7),   0.552498624152)
        self.assertAlmostEqual(sb.radiusYDeriv(2.1), -0.0964919838899)
        self.assertAlmostEqual(sb.radiusYDeriv(4.3), -0.0513394826451)
        self.assertAlmostEqual(sb.radiusYDeriv(5.9),    3.14254431891)

        sb.setWidth(2*273)
        sb.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusYDeriv(          0),  273)
        self.assertAlmostEqual(sb.radiusYDeriv(    math.pi), -273)
        self.assertAlmostEqual(sb.radiusYDeriv(  math.pi/2),    0)
        self.assertAlmostEqual(sb.radiusYDeriv(3*math.pi/2),    0)
        self.assertAlmostEqual(sb.radiusYDeriv(0.7),   116.29049998)
        self.assertAlmostEqual(sb.radiusYDeriv(2.1), -29.9472148455)
        self.assertAlmostEqual(sb.radiusYDeriv(4.3), -16.6595945857)
        self.assertAlmostEqual(sb.radiusYDeriv(5.9),  240.527905754)

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
        self.assertAlmostEqual(sb.radiusXDerivNorm(0.7), -0.996203290565)
        self.assertAlmostEqual(sb.radiusXDerivNorm(2.1),  -0.99970166443)
        self.assertAlmostEqual(sb.radiusXDerivNorm(4.3),  0.999895068381)
        self.assertAlmostEqual(sb.radiusXDerivNorm(5.9),  0.949840945816)

        sb.setWidth(2*273)
        sb.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusXDerivNorm(          0),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(    math.pi),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(  math.pi/2), -1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(3*math.pi/2),  1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(0.7), -0.904277036943)
        self.assertAlmostEqual(sb.radiusXDerivNorm(2.1), -0.991400051534)
        self.assertAlmostEqual(sb.radiusXDerivNorm(4.3),  0.996950618421)
        self.assertAlmostEqual(sb.radiusXDerivNorm(5.9),  0.490038779493)

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
        self.assertAlmostEqual(sb.radiusYDerivNorm(0.7),  0.0870574745107)
        self.assertAlmostEqual(sb.radiusYDerivNorm(2.1), -0.0244250309379)
        self.assertAlmostEqual(sb.radiusYDerivNorm(4.3), -0.0144862772005)
        self.assertAlmostEqual(sb.radiusYDerivNorm(5.9),   0.312733397083)

        sb.setWidth(2*273)
        sb.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusYDerivNorm(          0),  1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(    math.pi), -1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(  math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(3*math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(0.7),   0.426946179813)
        self.assertAlmostEqual(sb.radiusYDerivNorm(2.1),  -0.130866106451)
        self.assertAlmostEqual(sb.radiusYDerivNorm(4.3), -0.0780350205358)
        self.assertAlmostEqual(sb.radiusYDerivNorm(5.9),   0.871700633585)

if __name__ == '__main__':
    unittest.main()