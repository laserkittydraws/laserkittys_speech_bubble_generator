import unittest

from laserkittys_speech_bubble_generator.Shapes.misc import Point


class PointMethods(unittest.TestCase):

    def test_point(self):
        A = Point(2,3)
        self.assertAlmostEqual(A.x, 2)
        self.assertAlmostEqual(A.y, 3)
        B = Point(1.2,5.4)
        self.assertAlmostEqual(B.x, 1.2)
        self.assertAlmostEqual(B.y, 5.4)
        C = Point(-3.4,-7.2)
        self.assertAlmostEqual(C.x, -3.4)
        self.assertAlmostEqual(C.y, -7.2)

    def test_eq(self):
        A = Point(2,3)
        self.assertTrue(A == A)
        B = Point(1.2,5.4)
        self.assertFalse(A == B)

    def test_ne(self):
        A = Point(2,3)
        self.assertFalse(A != A)
        B = Point(1.2,5.4)
        self.assertTrue(A != B)

    def test_point_add(self):
        A = Point(1,2)
        B = Point(3,4)
        C = A + B
        self.assertAlmostEqual(C.x, 4)
        self.assertAlmostEqual(C.y, 6)
        A = Point(1.2,3.4)
        B = Point(5.6,7.8)
        C = A + B
        self.assertAlmostEqual(C.x, 6.8)
        self.assertAlmostEqual(C.y, 11.2)
        A = Point(-1.2,-3.4)
        B = Point(5.6,7.8)
        C = A + B
        self.assertAlmostEqual(C.x, 4.4)
        self.assertAlmostEqual(C.y, 4.4)

    def test_point_sub(self):
        A = Point(1,2)
        B = Point(3,4)
        C = A - B
        self.assertAlmostEqual(C.x, -2)
        self.assertAlmostEqual(C.y, -2)
        A = Point(1.2,3.4)
        B = Point(5.6,7.8)
        C = A - B
        self.assertAlmostEqual(C.x, -4.4)
        self.assertAlmostEqual(C.y, -4.4)
        A = Point(-1.2,-3.4)
        B = Point(5.6,7.8)
        C = A - B
        self.assertAlmostEqual(C.x, -6.8)
        self.assertAlmostEqual(C.y, -11.2)

    def test_point_mul(self):
        A = Point(1,2)
        B = 3
        C = B*A
        self.assertAlmostEqual(C.x, 3)
        self.assertAlmostEqual(C.y, 6)
        A = Point(1,2)
        B = 3
        C = A*B
        self.assertAlmostEqual(C.x, 3)
        self.assertAlmostEqual(C.y, 6)
        A = Point(1.2,3.4)
        B = 3
        C = B*A
        self.assertAlmostEqual(C.x, 3.6)
        self.assertAlmostEqual(C.y, 10.2)
        A = Point(1.2,3.4)
        B = 3
        C = A*B
        self.assertAlmostEqual(C.x, 3.6)
        self.assertAlmostEqual(C.y, 10.2)

    def test_point_div(self):
        A = Point(9,12)
        B = 3
        C = A/B
        self.assertAlmostEqual(C.x, 3)
        self.assertAlmostEqual(C.y, 4)
        A = Point(2,5)
        B = 3
        C = A/B
        self.assertAlmostEqual(C.x, 2/3)
        self.assertAlmostEqual(C.y, 5/3)