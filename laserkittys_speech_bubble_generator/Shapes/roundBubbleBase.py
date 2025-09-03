from laserkittys_speech_bubble_generator.Shapes.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION
from laserkittys_speech_bubble_generator.Shapes.misc import Point

import math

from laserkittys_speech_bubble_generator.config import *

ROUND_BUBBLE_BASE_VERSION = '1.1'

class RoundBubbleBase(SpeechBubble):

    """
    Base class for implementing custom speech bubble
    types that follow a round elliptical shape

    some guides for SVG formatting:

    https://www.w3schools.com/graphics/svg_intro.asp

    https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch
    """

    @staticmethod
    def radius(a: float) -> float:
        """
        returns the distance between the origin and a point on the ellipse given an angle a
        """
        if (RoundBubbleBase._width/2) <= 0 or (RoundBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {RoundBubbleBase._width} {RoundBubbleBase._height}')
        return (RoundBubbleBase._width/2)*(RoundBubbleBase._height/2)/math.sqrt(
            (((RoundBubbleBase._height/2)*math.cos(a))**2) +
            (((RoundBubbleBase._width/2)*math.sin(a))**2)
        )

    @staticmethod
    def radiusDeriv(a: float) -> float:
        """
        returns the change in the distance between the origin and a point on the ellipse given an angle a
        """
        if (RoundBubbleBase._width/2) <= 0 or (RoundBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {RoundBubbleBase._width} {RoundBubbleBase._height}')
        x1: float = -(RoundBubbleBase._width/2) * (RoundBubbleBase._height/2)

        x2: float = ((RoundBubbleBase._height/2)**2)*(-math.sin(a))*(math.cos(a))
        x3: float = ((RoundBubbleBase._width/2)**2)*(math.cos(a))*(math.sin(a))
        x4: float = x2+x3

        x5: float = ((RoundBubbleBase._height/2)*math.cos(a))**2
        x6: float = ((RoundBubbleBase._width/2)*math.sin(a))**2
        x7: float = abs((x5+x6)**(-1.5))

        return (x1*x4*x7)

    @staticmethod
    def radiusXDeriv(a: float) -> float:
        """
        returns the change in the x-direction of the change in the distance between the origin and a point on the ellipse given an angle a
        """
        if (RoundBubbleBase._width/2) <= 0 or (RoundBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {RoundBubbleBase._width} {RoundBubbleBase._height}')
        return ((RoundBubbleBase.radius(a))*(-math.sin(a))) + ((RoundBubbleBase.radiusDeriv(a))*(math.cos(a)))

    @staticmethod
    def radiusYDeriv(a: float) -> float:
        """
        returns the change in the y-direction of the change in the distance between the origin and a point on the ellipse given an angle a
        """
        if (RoundBubbleBase._width/2) <= 0 or (RoundBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {RoundBubbleBase._width} {RoundBubbleBase._height}')
        return ((RoundBubbleBase.radius(a))*(math.cos(a))) + ((RoundBubbleBase.radiusDeriv(a))*(math.sin(a)))

    @staticmethod
    def radiusDerivVec(a):
        return Point(RoundBubbleBase.radiusXDeriv(a), RoundBubbleBase.radiusYDeriv(a))

    @staticmethod
    def radiusMagnitude(a):
        return math.sqrt( (RoundBubbleBase.radiusXDeriv(a)**2) + (RoundBubbleBase.radiusYDeriv(a)**2) )

    @staticmethod
    def radiusXDerivNorm(a: float) -> float:
        """
        returns the normalized change in the x-direction of the change in the distance between the origin and a point on the ellipse given an angle a
        """
        if (RoundBubbleBase._width/2) <= 0 or (RoundBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {RoundBubbleBase._width} {RoundBubbleBase._height}')
        xDeriv: float = RoundBubbleBase.radiusXDeriv(a)
        yDeriv: float = RoundBubbleBase.radiusYDeriv(a)
        ret: float = xDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
        if RoundBubbleBase._logger is not None:
            RoundBubbleBase._logger.log(LSBG_DEBUG_VERBOSE, f'xDeriv: {xDeriv} yDeriv: {yDeriv} xDerivNorm: {ret}')
        return ret

    @staticmethod
    def radiusYDerivNorm(a: float) -> float:
        """
        returns the normalized change in the y-direction of the change in the distance between the origin and a point on the ellipse given an angle a
        """
        if (RoundBubbleBase._width/2) <= 0 or (RoundBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {RoundBubbleBase._width} {RoundBubbleBase._height}')
        xDeriv: float = RoundBubbleBase.radiusXDeriv(a)
        yDeriv: float = RoundBubbleBase.radiusYDeriv(a)
        ret: float = yDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
        if RoundBubbleBase._logger is not None:
            RoundBubbleBase._logger.log(LSBG_DEBUG_VERBOSE, f'xDeriv: {xDeriv} yDeriv: {yDeriv} xDerivNorm: {ret}')
        return ret

    @staticmethod
    def radiusDerivNormVec(a) -> Point:
        return Point(RoundBubbleBase.radiusXDerivNorm(a), RoundBubbleBase.radiusYDerivNorm(a))

    @staticmethod
    def RoundBubblePoint(a: float) -> Point:
        """
        takes an angle 'a' and returns a point on the bubble

        ### Args:
            a (float): angle from positive x-axis to bubble point (0 <= x <= 2pi)

        ### Returns:
            Point: an x,y coordinate on the bubble
        """
        if (RoundBubbleBase._width/2) <= 0 or (RoundBubbleBase._height/2) <= 0: raise ValueError(f'bubble width and height must both be greater than zero: {RoundBubbleBase._width} {RoundBubbleBase._height}')
        xp: float = (RoundBubbleBase.radius(a)*math.cos(a))+(RoundBubbleBase._width /2)+RoundBubbleBase._tailLength
        yp: float = (RoundBubbleBase.radius(a)*math.sin(a))+(RoundBubbleBase._height/2)+RoundBubbleBase._tailLength
        if RoundBubbleBase._logger is not None:
            RoundBubbleBase._logger.log(LSBG_DEBUG_VERBOSE, f'point x,y: {xp} {yp}')
        return Point(xp, yp)

    @staticmethod
    def __repr__() -> str:
        return super().__repr__() + f'speech bubble base version: {ROUND_BUBBLE_BASE_VERSION}'