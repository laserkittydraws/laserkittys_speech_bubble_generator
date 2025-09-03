from laserkittys_speech_bubble_generator.Shapes.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION
from laserkittys_speech_bubble_generator.Shapes.misc import Point

import math

from laserkittys_speech_bubble_generator.config import *

SQUIRCLE_BUBBLE_BASE_VERSION = '1.0'

class SquircleBubbleBase(SpeechBubble):

    """
    Base class for implementing custom speech bubble
    types that follow a squircle shape

    some guides for SVG formatting:

    https://www.w3schools.com/graphics/svg_intro.asp

    https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch
    """

    _squirclePower: float = 2.8

    @staticmethod
    def radius(a: float) -> float:
        """
        returns the distance from the origin to a point on the squircle given some angle a (0 <= x <= 2pi)
        """
        if (SquircleBubbleBase._width/2) <= 0 or (SquircleBubbleBase._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubbleBase._width} {SquircleBubbleBase._height}')
        x1: float = abs(((SquircleBubbleBase._height/2)*(math.cos(a)))**SquircleBubbleBase._squirclePower)
        x2: float = abs(((SquircleBubbleBase._width/2)*(math.sin(a)))**SquircleBubbleBase._squirclePower)
        return (SquircleBubbleBase._width/2)*(SquircleBubbleBase._height/2)/abs((x1+x2)**(1/SquircleBubbleBase._squirclePower))

    @staticmethod
    def radiusDeriv(a: float) -> float:
        """
        returns the change in the distance from the origin to a point on the squircle given some angle a (0 <= x <= 2pi)
        """
        if (SquircleBubbleBase._width/2) <= 0 or (SquircleBubbleBase._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubbleBase._width} {SquircleBubbleBase._height}')
        x1: float = -(SquircleBubbleBase._width/2) * (SquircleBubbleBase._height/2)

        x2: float = math.pow(SquircleBubbleBase._height/2,SquircleBubbleBase._squirclePower)*(-math.sin(a))*math.copysign(math.pow(abs(math.cos(a)),SquircleBubbleBase._squirclePower-1),math.cos(a))
        x3: float = math.pow(SquircleBubbleBase._width/2,SquircleBubbleBase._squirclePower)*(math.cos(a))*math.copysign(math.pow(abs(math.sin(a)),SquircleBubbleBase._squirclePower-1),math.sin(a))
        x4: float = x2+x3

        x5: float = abs(((SquircleBubbleBase._height/2)*math.cos(a))**SquircleBubbleBase._squirclePower)
        x6: float = abs(((SquircleBubbleBase._width/2)*math.sin(a))**SquircleBubbleBase._squirclePower)
        x7: float = abs((x5+x6)**(-1-(1/SquircleBubbleBase._squirclePower)))

        return (x1*x4*x7)

    @staticmethod
    def radiusXDeriv(a: float) -> float:
        """
        returns the change in the x-direction of the change in the distance from the origin to a point on the squircle given some angle a (0 <= x <= 2pi)
        """
        if (SquircleBubbleBase._width/2) <= 0 or (SquircleBubbleBase._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubbleBase._width} {SquircleBubbleBase._height}')
        return ((SquircleBubbleBase.radius(a))*(-math.sin(a))) + ((SquircleBubbleBase.radiusDeriv(a))*(math.cos(a)))

    @staticmethod
    def radiusYDeriv(a: float) -> float:
        """
        returns the change in the y-direction of the change in the distance from the origin to a point on the squircle given some angle a (0 <= x <= 2pi)
        """
        if (SquircleBubbleBase._width/2) <= 0 or (SquircleBubbleBase._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubbleBase._width} {SquircleBubbleBase._height}')
        return ((SquircleBubbleBase.radius(a))*(math.cos(a))) + ((SquircleBubbleBase.radiusDeriv(a))*(math.sin(a)))

    @staticmethod
    def radiusDerivVec(a):
        return Point(SquircleBubbleBase.radiusXDerivNorm(a), SquircleBubbleBase.radiusYDerivNorm(a))

    @staticmethod
    def radiusMagnitude(a):
        return math.sqrt( (SquircleBubbleBase.radiusXDeriv(a)**2) + (SquircleBubbleBase.radiusYDeriv(a)**2) )

    @staticmethod
    def radiusXDerivNorm(a: float) -> float:
        """
        returns the normalized change in the x-direction of the change in the distance from the origin to a point on the squircle given some angle a (0 <= x <= 2pi)
        """
        if (SquircleBubbleBase._width/2) <= 0 or (SquircleBubbleBase._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubbleBase._width} {SquircleBubbleBase._height}')
        xDeriv: float = SquircleBubbleBase.radiusXDeriv(a)
        yDeriv: float = SquircleBubbleBase.radiusYDeriv(a)
        ret: float = xDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
        return ret

    @staticmethod
    def radiusYDerivNorm(a: float) -> float:
        """
        returns the normalized change in the y-direction of the change in the distance from the origin to a point on the squircle given some angle a (0 <= x <= 2pi)
        """
        if (SquircleBubbleBase._width/2) <= 0 or (SquircleBubbleBase._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubbleBase._width} {SquircleBubbleBase._height}')
        xDeriv = SquircleBubbleBase.radiusXDeriv(a)
        yDeriv = SquircleBubbleBase.radiusYDeriv(a)
        ret: float = yDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
        return ret

    @staticmethod
    def radiusDerivNormVec(a) -> Point:
        return Point(SquircleBubbleBase.radiusXDerivNorm(a), SquircleBubbleBase.radiusYDerivNorm(a))

    @staticmethod
    def squirclePoint(a: float) -> Point:
        """takes an angle 'a' and returns a point on the squircle

        ### Args:
            a (float): angle from positive x-axis to squircle point (0 <= x <= 2pi)

        ### Returns:
            (Point): an x,y coordinate on the squircle
        """
        if (SquircleBubbleBase._width/2) <= 0 or (SquircleBubbleBase._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubbleBase._width} {SquircleBubbleBase._height}')
        xp: float = (SquircleBubbleBase.radius(a)*math.cos(a))+(SquircleBubbleBase._width /2)+SquircleBubbleBase._tailLength
        yp: float = (SquircleBubbleBase.radius(a)*math.sin(a))+(SquircleBubbleBase._height/2)+SquircleBubbleBase._tailLength
        return Point(xp, yp)