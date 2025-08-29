from laserkittys_speech_bubble_generator.Shapes.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION
from laserkittys_speech_bubble_generator.Shapes.misc import Point
from laserkittys_speech_bubble_generator.config import *

import math
import warnings

SQUARE_BUBBLE_BASE_VERSION = '1.0'

class SquareBubbleBase(SpeechBubble):

    """
    Base class for implementing custom speech bubble
    types that follow a square shape

    some guides for SVG formatting:

    https://www.w3schools.com/graphics/svg_intro.asp

    https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch
    """

    @staticmethod
    def radius(a: float) -> float:
        raise NotImplementedError('Did you mean radiusX() or radiusY()? SquareBubbleBase does not implement the default radius() method, instead it uses radiusX() and radiusY().')

    @staticmethod
    def radiusDeriv(a: float) -> float:
        raise NotImplementedError('Did you mean radiusXDeriv() or radiusYDeriv()? SquareBubbleBase does not implement the default radiusDeriv() method, instead it uses radiusXDeriv() and radiusYDeriv().')

    @staticmethod
    def radiusX(a: float) -> float:
        """
        returns the horizontal distance from the origin given an angle a (0 <= x <= 2pi)
        """

        if (SquareBubbleBase._width/2) <= 0 or (SquareBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {SquareBubbleBase._width} {SquareBubbleBase._height}')
        urCornerAng = (                                0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        ulCornerAng = (  (SquareBubbleBase._width/2) + 0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        llCornerAng = (  (SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        lrCornerAng = (2*(SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        if a/(2*math.pi) <= urCornerAng: return SquareBubbleBase._width/2
        if a/(2*math.pi) <= ulCornerAng: return (1 - ( 2*( (a/(2*math.pi)) - urCornerAng)/(ulCornerAng - urCornerAng) ))*(SquareBubbleBase._width/2)
        if a/(2*math.pi) <= llCornerAng: return -SquareBubbleBase._width/2
        if a/(2*math.pi) <= lrCornerAng: return (-1 + ( 2*( (a/(2*math.pi)) - llCornerAng)/(lrCornerAng - llCornerAng) ))*(SquareBubbleBase._width/2)
        return SquareBubbleBase._width/2

    @staticmethod
    def radiusY(a: float) -> float:
        """
        returns the vertical distance from the origin given an angle a (0 <= x <= 2pi)
        """
        if (SquareBubbleBase._width/2) <= 0 or (SquareBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {SquareBubbleBase._width} {SquareBubbleBase._height}')
        urCornerAng = (                                0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        ulCornerAng = (  (SquareBubbleBase._width/2) + 0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        llCornerAng = (  (SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        lrCornerAng = (2*(SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        if a/(2*math.pi) <= urCornerAng: return ( ((a/(2*math.pi)) - 0)/(urCornerAng - 0) )*(SquareBubbleBase._height/2)
        if a/(2*math.pi) <= ulCornerAng: return SquareBubbleBase._height/2
        if a/(2*math.pi) <= llCornerAng: return (1 - 2*( ((a/(2*math.pi)) - ulCornerAng)/(llCornerAng - ulCornerAng) ))*(SquareBubbleBase._height/2)
        if a/(2*math.pi) <= lrCornerAng: return -SquareBubbleBase._height/2
        return (-1 + ( ((a/(2*math.pi)) - lrCornerAng)/(1 - lrCornerAng) ))*(SquareBubbleBase._height/2)

    @staticmethod
    def radiusXDeriv(a: float):
        warnings.warn('this method is an alias to radiusXDerivNorm() since the two are mathematically equivalent')
        return SquareBubbleBase.radiusXDerivNorm(a)

    @staticmethod
    def radiusXDerivNorm(a: float):
        """
        returns the normalized change in horizontal distance from the origin given an angle a (0 <= x <= 2pi)
        """
        if (SquareBubbleBase._width/2) <= 0 or (SquareBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {SquareBubbleBase._width} {SquareBubbleBase._height}')
        urCornerAng = (                                0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        ulCornerAng = (  (SquareBubbleBase._width/2) + 0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        llCornerAng = (  (SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        lrCornerAng = (2*(SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        if a/(2*math.pi) <= urCornerAng: return 0
        if a/(2*math.pi) <= ulCornerAng: return -1
        if a/(2*math.pi) <= llCornerAng: return 0
        if a/(2*math.pi) <= lrCornerAng: return 1
        return 0

    @staticmethod
    def radiusYDeriv(a: float):
        warnings.warn('this method is an alias to radiusYDerivNorm() since the two are mathematically equivalent')
        return SquareBubbleBase.radiusYDerivNorm(a)

    @staticmethod
    def radiusYDerivNorm(a: float):
        """
        returns the normalized change in vertical distance from the origin given an angle a (0 <= x <= 2pi)
        """
        if (SquareBubbleBase._width/2) <= 0 or (SquareBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {SquareBubbleBase._width} {SquareBubbleBase._height}')
        urCornerAng = (                                0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        ulCornerAng = (  (SquareBubbleBase._width/2) + 0.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        llCornerAng = (  (SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        lrCornerAng = (2*(SquareBubbleBase._width/2) + 1.5*(SquareBubbleBase._height/2))/(2*(SquareBubbleBase._width/2) + 2*(SquareBubbleBase._height/2))
        if a/(2*math.pi) <= urCornerAng: return 1
        if a/(2*math.pi) <= ulCornerAng: return 0
        if a/(2*math.pi) <= llCornerAng: return -1
        if a/(2*math.pi) <= lrCornerAng: return 0
        return 1

    @staticmethod
    def SquareBubblePoint(a: float) -> Point:
        """
        takes an angle 'a' and returns a point on the bubble

        ### Args:
            a (float): angle from positive x-axis to bubble point (0 <= x <= 2pi)

        ### Returns:
            Point: an x,y coordinate on the bubble
        """
        if (SquareBubbleBase._width/2) <= 0 or (SquareBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {SquareBubbleBase._width} {SquareBubbleBase._height}')
        return Point(SquareBubbleBase.radiusX(a), SquareBubbleBase.radiusY(a))

    @staticmethod
    def __repr__() -> str:
        return super().__repr__() + f'speech bubble base version: {SQUARE_BUBBLE_BASE_VERSION}'