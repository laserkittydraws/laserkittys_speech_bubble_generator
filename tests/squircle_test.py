import unittest
import math

import laserkittys_speech_bubble_generator.Shapes.squircleBubble as sb

class SquircleMethods(unittest.TestCase):

    def test_radius(self):
        sb.SquircleBubble.setWidth(0)
        sb.SquircleBubble.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radius(0)
        with self.assertRaises(ValueError):
            sb.radius(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radius(5*math.pi/3)

        sb.SquircleBubble.setWidth(2*8)
        sb.SquircleBubble.setHeight(2*3)
        self.assertAlmostEqual(sb.radius(0),8)
        self.assertAlmostEqual(sb.radius(math.pi),8)
        self.assertAlmostEqual(sb.radius(math.pi/2),3)
        self.assertAlmostEqual(sb.radius(3*math.pi/2),3)
        self.assertAlmostEqual(sb.radius(0.7),4.49549306514)
        self.assertAlmostEqual(sb.radius(2.1),3.45783661669)
        self.assertAlmostEqual(sb.radius(4.3),3.26713555143)
        self.assertAlmostEqual(sb.radius(5.9),6.48314778284)

        sb.SquircleBubble.setWidth(2*273)
        sb.SquircleBubble.setHeight(2*187)
        self.assertAlmostEqual(sb.radius(0),273)
        self.assertAlmostEqual(sb.radius(math.pi),273)
        self.assertAlmostEqual(sb.radius(math.pi/2),187)
        self.assertAlmostEqual(sb.radius(3*math.pi/2),187)
        self.assertAlmostEqual(sb.radius(0.7),247.617691377)
        self.assertAlmostEqual(sb.radius(2.1),210.955550159)
        self.assertAlmostEqual(sb.radius(4.3),201.67178883)
        self.assertAlmostEqual(sb.radius(5.9),273.638606804)

    def test_radius_deriv(self):
        sb.SquircleBubble.setWidth(0)
        sb.SquircleBubble.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusAngDeriv(0)
        with self.assertRaises(ValueError):
            sb.radiusAngDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusAngDeriv(5*math.pi/3)

        sb.SquircleBubble.setWidth(2*8)
        sb.SquircleBubble.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusAngDeriv(0),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(math.pi),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(math.pi/2),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(3*math.pi/2),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(0.7),-4.47961020301)
        self.assertAlmostEqual(sb.radiusAngDeriv(2.1),1.91052533268)
        self.assertAlmostEqual(sb.radiusAngDeriv(4.3),-1.3732509483)
        self.assertAlmostEqual(sb.radiusAngDeriv(5.9),7.67749282856)

        sb.SquircleBubble.setWidth(2*273)
        sb.SquircleBubble.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusAngDeriv(0),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(math.pi),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(math.pi/2),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(3*math.pi/2),0)
        self.assertAlmostEqual(sb.radiusAngDeriv(0.7),-113.467789151)
        self.assertAlmostEqual(sb.radiusAngDeriv(2.1),88.6840155514)
        self.assertAlmostEqual(sb.radiusAngDeriv(4.3),-70.042214882)
        self.assertAlmostEqual(sb.radiusAngDeriv(5.9),35.4822890108)

    def test_radius_x_deriv(self):
        sb.SquircleBubble.setWidth(0)
        sb.SquircleBubble.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusXDeriv(0)
        with self.assertRaises(ValueError):
            sb.radiusXDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusXDeriv(5*math.pi/3)

        sb.SquircleBubble.setWidth(2*8)
        sb.SquircleBubble.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusXDeriv(          0),  0)
        self.assertAlmostEqual(sb.radiusXDeriv(    math.pi),  0)
        self.assertAlmostEqual(sb.radiusXDeriv(  math.pi/2), -3)
        self.assertAlmostEqual(sb.radiusXDeriv(3*math.pi/2),  3)
        self.assertAlmostEqual(sb.radiusXDeriv(0.7), -6.32227101127)
        self.assertAlmostEqual(sb.radiusXDeriv(2.1), -3.94935822781)
        self.assertAlmostEqual(sb.radiusXDeriv(4.3),   3.5436361461)
        self.assertAlmostEqual(sb.radiusXDeriv(5.9),  9.54460667133)

        sb.SquircleBubble.setWidth(2*273)
        sb.SquircleBubble.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusXDeriv(          0),    0)
        self.assertAlmostEqual(sb.radiusXDeriv(    math.pi),    0)
        self.assertAlmostEqual(sb.radiusXDeriv(  math.pi/2), -187)
        self.assertAlmostEqual(sb.radiusXDeriv(3*math.pi/2),  187)
        self.assertAlmostEqual(sb.radiusXDeriv(0.7), -246.304648499)
        self.assertAlmostEqual(sb.radiusXDeriv(2.1), -226.870586635)
        self.assertAlmostEqual(sb.radiusXDeriv(4.3),  212.837685065)
        self.assertAlmostEqual(sb.radiusXDeriv(5.9),  135.216147412)

    def test_radius_y_deriv(self):
        sb.SquircleBubble.setWidth(0)
        sb.SquircleBubble.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusYDeriv(0)
        with self.assertRaises(ValueError):
            sb.radiusYDeriv(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusYDeriv(5*math.pi/3)

        sb.SquircleBubble.setWidth(2*8)
        sb.SquircleBubble.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusYDeriv(          0),  8)
        self.assertAlmostEqual(sb.radiusYDeriv(    math.pi), -8)
        self.assertAlmostEqual(sb.radiusYDeriv(  math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDeriv(3*math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDeriv(0.7),   0.552498624152)
        self.assertAlmostEqual(sb.radiusYDeriv(2.1), -0.0964919838899)
        self.assertAlmostEqual(sb.radiusYDeriv(4.3), -0.0513394826451)
        self.assertAlmostEqual(sb.radiusYDeriv(5.9),    3.14254431891)

        sb.SquircleBubble.setWidth(2*273)
        sb.SquircleBubble.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusYDeriv(          0),  273)
        self.assertAlmostEqual(sb.radiusYDeriv(    math.pi), -273)
        self.assertAlmostEqual(sb.radiusYDeriv(  math.pi/2),    0)
        self.assertAlmostEqual(sb.radiusYDeriv(3*math.pi/2),    0)
        self.assertAlmostEqual(sb.radiusYDeriv(0.7),   116.29049998)
        self.assertAlmostEqual(sb.radiusYDeriv(2.1), -29.9472148455)
        self.assertAlmostEqual(sb.radiusYDeriv(4.3), -16.6595945857)
        self.assertAlmostEqual(sb.radiusYDeriv(5.9),  240.527905754)

    def test_radius_x_deriv_norm(self):
        sb.SquircleBubble.setWidth(0)
        sb.SquircleBubble.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(5*math.pi/3)

        sb.SquircleBubble.setWidth(2*8)
        sb.SquircleBubble.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusXDerivNorm(          0),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(    math.pi),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(  math.pi/2), -1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(3*math.pi/2),  1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(0.7), -0.996203290565)
        self.assertAlmostEqual(sb.radiusXDerivNorm(2.1),  -0.99970166443)
        self.assertAlmostEqual(sb.radiusXDerivNorm(4.3),  0.999895068381)
        self.assertAlmostEqual(sb.radiusXDerivNorm(5.9),  0.949840945816)

        sb.SquircleBubble.setWidth(2*273)
        sb.SquircleBubble.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusXDerivNorm(          0),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(    math.pi),  0)
        self.assertAlmostEqual(sb.radiusXDerivNorm(  math.pi/2), -1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(3*math.pi/2),  1)
        self.assertAlmostEqual(sb.radiusXDerivNorm(0.7), -0.904277036943)
        self.assertAlmostEqual(sb.radiusXDerivNorm(2.1), -0.991400051534)
        self.assertAlmostEqual(sb.radiusXDerivNorm(4.3),  0.996950618421)
        self.assertAlmostEqual(sb.radiusXDerivNorm(5.9),  0.490038779493)

    def test_radius_y_deriv_norm(self):
        sb.SquircleBubble.setWidth(0)
        sb.SquircleBubble.setHeight(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(0)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(2*math.pi/3)
        with self.assertRaises(ValueError):
            sb.radiusXDerivNorm(5*math.pi/3)

        sb.SquircleBubble.setWidth(2*8)
        sb.SquircleBubble.setHeight(2*3)
        self.assertAlmostEqual(sb.radiusYDerivNorm(          0),  1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(    math.pi), -1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(  math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(3*math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(0.7),  0.0870574745107)
        self.assertAlmostEqual(sb.radiusYDerivNorm(2.1), -0.0244250309379)
        self.assertAlmostEqual(sb.radiusYDerivNorm(4.3), -0.0144862772005)
        self.assertAlmostEqual(sb.radiusYDerivNorm(5.9),   0.312733397083)

        sb.SquircleBubble.setWidth(2*273)
        sb.SquircleBubble.setHeight(2*187)
        self.assertAlmostEqual(sb.radiusYDerivNorm(          0),  1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(    math.pi), -1)
        self.assertAlmostEqual(sb.radiusYDerivNorm(  math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(3*math.pi/2),  0)
        self.assertAlmostEqual(sb.radiusYDerivNorm(0.7),   0.426946179813)
        self.assertAlmostEqual(sb.radiusYDerivNorm(2.1),  -0.130866106451)
        self.assertAlmostEqual(sb.radiusYDerivNorm(4.3), -0.0780350205358)
        self.assertAlmostEqual(sb.radiusYDerivNorm(5.9),   0.871700633585)

class PointMethods(unittest.TestCase):

    def test_point(self):
        A = sb.Point(2,3)
        self.assertAlmostEqual(A.x, 2)
        self.assertAlmostEqual(A.y, 3)
        B = sb.Point(1.2,5.4)
        self.assertAlmostEqual(B.x, 1.2)
        self.assertAlmostEqual(B.y, 5.4)
        C = sb.Point(-3.4,-7.2)
        self.assertAlmostEqual(C.x, -3.4)
        self.assertAlmostEqual(C.y, -7.2)

    def test_eq(self):
        A = sb.Point(2,3)
        self.assertTrue(A == A)
        B = sb.Point(1.2,5.4)
        self.assertFalse(A == B)

    def test_ne(self):
        A = sb.Point(2,3)
        self.assertFalse(A != A)
        B = sb.Point(1.2,5.4)
        self.assertTrue(A != B)

    def test_point_add(self):
        A = sb.Point(1,2)
        B = sb.Point(3,4)
        C = A + B
        self.assertAlmostEqual(C.x, 4)
        self.assertAlmostEqual(C.y, 6)
        A = sb.Point(1.2,3.4)
        B = sb.Point(5.6,7.8)
        C = A + B
        self.assertAlmostEqual(C.x, 6.8)
        self.assertAlmostEqual(C.y, 11.2)
        A = sb.Point(-1.2,-3.4)
        B = sb.Point(5.6,7.8)
        C = A + B
        self.assertAlmostEqual(C.x, 4.4)
        self.assertAlmostEqual(C.y, 4.4)

    def test_point_sub(self):
        A = sb.Point(1,2)
        B = sb.Point(3,4)
        C = A - B
        self.assertAlmostEqual(C.x, -2)
        self.assertAlmostEqual(C.y, -2)
        A = sb.Point(1.2,3.4)
        B = sb.Point(5.6,7.8)
        C = A - B
        self.assertAlmostEqual(C.x, -4.4)
        self.assertAlmostEqual(C.y, -4.4)
        A = sb.Point(-1.2,-3.4)
        B = sb.Point(5.6,7.8)
        C = A - B
        self.assertAlmostEqual(C.x, -6.8)
        self.assertAlmostEqual(C.y, -11.2)

    def test_point_mul(self):
        A = sb.Point(1,2)
        B = 3
        C = B*A
        self.assertAlmostEqual(C.x, 3)
        self.assertAlmostEqual(C.y, 6)
        A = sb.Point(1,2)
        B = 3
        C = A*B
        self.assertAlmostEqual(C.x, 3)
        self.assertAlmostEqual(C.y, 6)
        A = sb.Point(1.2,3.4)
        B = 3
        C = B*A
        self.assertAlmostEqual(C.x, 3.6)
        self.assertAlmostEqual(C.y, 10.2)
        A = sb.Point(1.2,3.4)
        B = 3
        C = A*B
        self.assertAlmostEqual(C.x, 3.6)
        self.assertAlmostEqual(C.y, 10.2)

    def test_point_div(self):
        A = sb.Point(9,12)
        B = 3
        C = A/B
        self.assertAlmostEqual(C.x, 3)
        self.assertAlmostEqual(C.y, 4)
        A = sb.Point(2,5)
        B = 3
        C = A/B
        self.assertAlmostEqual(C.x, 2/3)
        self.assertAlmostEqual(C.y, 5/3)

if __name__ == '__main__':
    unittest.main()