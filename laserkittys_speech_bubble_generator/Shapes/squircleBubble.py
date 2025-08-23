from laserkittys_speech_bubble_generator.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION
from laserkittys_speech_bubble_generator.config import *

from typing import Iterator
import math
import logging

class SquircleBubble(SpeechBubble):

    _logger: logging.Logger

    _squirclePower: float = 2.8
    _numSquirclePoints: int = 200

    def getPreview() -> str:

        SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'bubble width, height: {SquircleBubble._width} {SquircleBubble._height}')

        def radius(a: float) -> float:
            # if a < 0 or a > 2*math.pi: raise ValueError(f'angle value out of bounds (0 <= x <= 2pi): {a}')
            # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'radius- angle: {a}')
            # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'radius- cos: {math.cos(a)}, sin: {math.sin(a)}')
            # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'radius- bwidth, bheight: {SquircleBubble._width} {SquircleBubble._height}')
            # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'radius- x1a, x2a: {(SquircleBubble._height/2)*(math.cos(a))} {(SquircleBubble._width/2)*(math.sin(a))}')
            x1: float = abs(((SquircleBubble._height/2)*(math.cos(a)))**SquircleBubble._squirclePower)
            x2: float = abs(((SquircleBubble._width/2)*(math.sin(a)))**SquircleBubble._squirclePower)
            # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'radius- x1: {x1}, x2: {x2}')
            return (SquircleBubble._width/2)*(SquircleBubble._height/2)/abs((x1+x2)**(1/SquircleBubble._squirclePower))

        def radiusAngDeriv(a: float) -> float:
            return -1 * (SquircleBubble._width/2) * (SquircleBubble._height/2) * (
                ( (-math.sin(a))*((SquircleBubble._height/2)**SquircleBubble._squirclePower)*abs( (math.cos(a))**(SquircleBubble._squirclePower - 1) ) ) + 
                ( ( math.cos(a))*((SquircleBubble._width /2)**SquircleBubble._squirclePower)*abs( (math.sin(a))**(SquircleBubble._squirclePower - 1) ) )
            ) / abs(
                (
                    ( ( (SquircleBubble._height/2)*(math.cos(a)) )**SquircleBubble._squirclePower ) + 
                    ( ( (SquircleBubble._width /2)*(math.sin(a)) )**SquircleBubble._squirclePower )
                )**( (1/SquircleBubble._squirclePower) + 1 )
            )

        def radiusXDeriv(a: float) -> float:
            # if a < 0 or a > 2*math.pi: raise ValueError(f'angle value out of bounds (0 <= x <= 2pi): {a}')
            return ((radius(a))*(-math.sin(a))) + ((radiusAngDeriv(a))*(math.cos(a)))

        def radiusYDeriv(a: float) -> float:
            # if a < 0 or a > 2*math.pi: raise ValueError(f'angle value out of bounds (0 <= x <= 2pi): {a}')
            return ((radius(a))*(math.cos(a))) + ((radiusAngDeriv(a))*(math.sin(a)))

        def radiusXDerivNorm(a: float) -> float:
            r: float = radius(a)
            dr: float = radiusAngDeriv(a)
            xDeriv: float = radiusXDeriv(a)
            yDeriv: float = radiusYDeriv(a)
            ret: float = xDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
            SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'radius: {r} rDeriv: {dr} xDeriv: {xDeriv} yDeriv: {yDeriv} xDerivNorm: {ret}')
            return ret

        def radiusYDerivNorm(a: float) -> float:
            xDeriv = radiusXDeriv(a)
            yDeriv = radiusYDeriv(a)
            ret: float = yDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
            SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'yDerivNorm: {ret}')
            return ret

        class Point:

            x: float
            y: float

            def __init__(self, a,b):
                self.x = a
                self.y = b

            def __add__(self, p):
                if not (type(p) is Point): raise TypeError(f'value not a Point: {p}')
                return Point(self.x + p.x, self.y + p.y)

            def __sub__(self, p):
                if not (type(p) is Point): raise TypeError(f'value not a Point: {p}')
                return Point(self.x - p.x, self.y - p.y)
            
            def __mul__(self, n):
                if not (type(n) in [int, float]): raise TypeError(f'value not an int or float: {n}')
                return Point(self.x * n, self.y * n)

            def __rmul__(self, n):
                if not (type(n) in [int, float]): raise TypeError(f'value not an int or float: {n}')
                return Point(self.x * n, self.y * n)

            def __truediv__(self, n):
                if not (type(n) in [int, float]): raise TypeError(f'value not an int or float: {n}')
                return Point(self.x / n, self.y / n)
            
            def __repr__(self):
                return f'Point: (x: {self.x} y: {self.y})'

        def squirclePoint(a: float) -> Point:
            """takes an angle 'a' and returns a point on the squircle

            ### Args:
                a (float): angle from positive x-axis to squircle point (0 <= x <= 2pi)

            ### Returns:
                Point: an x,y coordinate on the squircle
            """
            # if a < 0 or a > 2*math.pi: raise ValueError(f'angle value out of bounds (0 <= x <= 2pi): {a}')
            xp: float = (radius(a)*math.cos(a))+(SquircleBubble._width /2)+SquircleBubble._tailLength
            yp: float = (radius(a)*math.sin(a))+(SquircleBubble._height/2)+SquircleBubble._tailLength
            # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'point x,y: {xp} {yp}')
            return Point(xp, yp)

        thetaD = SquircleBubble._tailAnglePosition
        thetaR = 2*math.pi*(SquircleBubble._tailAnglePosition/360)
        thetaDeltaD = SquircleBubble._tailWidth
        thetaDeltaR = 2*math.pi*(SquircleBubble._tailWidth/360)

        tBaseMidPoint   = squirclePoint(thetaR)
        tBaseLeftPoint  = squirclePoint(thetaR - thetaDeltaR)
        tBaseRightPoint = squirclePoint(thetaR + thetaDeltaR)

        tBaseLMidPt = tBaseMidPoint + ((tBaseLeftPoint - tBaseMidPoint)/2)
        tBaseRMidPt = tBaseMidPoint + ((tBaseRightPoint - tBaseMidPoint)/2)

        i = 0
        tailAdded = False
        pathPoints: list[Point] = []
        while i < SquircleBubble._numSquirclePoints+1:
            currAng = 2*math.pi*(i/SquircleBubble._numSquirclePoints)
            if ( i < SquircleBubble._numSquirclePoints*(thetaD-thetaDeltaD)/360 ) or ( i > SquircleBubble._numSquirclePoints*(thetaD+thetaDeltaD)/360 ):
                pathPoints.append(squirclePoint(currAng))
            elif not tailAdded:
                tailAdded = True
                pathPoints.append(tBaseLeftPoint)
                if thetaD >= 180:
                    tailEndPoint = tBaseMidPoint + ( SquircleBubble._tailLength*Point( radiusYDerivNorm(thetaR), -radiusXDerivNorm(thetaR) ) )
                else:
                    tailEndPoint = tBaseMidPoint - ( SquircleBubble._tailLength*Point( radiusYDerivNorm(thetaR), -radiusXDerivNorm(thetaR) ) )
                pathPoints.append(tailEndPoint)
                pathPoints.append(tBaseRightPoint)
                SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'tail base mid point: {tBaseMidPoint}')
                SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'tail points: {tBaseLeftPoint} {tailEndPoint} {tBaseRightPoint}')
            i += 1

        bubblePath = f'M {pathPoints[0].x} {pathPoints[0].y} L '
        for n in range(1,len(pathPoints)): bubblePath += f'{pathPoints[n].x} {pathPoints[n].y} '
        bubblePath += 'Z'

        # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'squircle bubble path: {bubblePath}')

        return bubblePath