from laserkittys_speech_bubble_generator.Shapes.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION
from laserkittys_speech_bubble_generator.Shapes.misc import Point

import math
import logging

from laserkittys_speech_bubble_generator.config import *

def radius(a: float) -> float:
    if (SquircleBubble._width/2) <= 0 or (SquircleBubble._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubble._width} {SquircleBubble._height}')
    x1: float = abs(((SquircleBubble._height/2)*(math.cos(a)))**SquircleBubble._squirclePower)
    x2: float = abs(((SquircleBubble._width/2)*(math.sin(a)))**SquircleBubble._squirclePower)
    return (SquircleBubble._width/2)*(SquircleBubble._height/2)/abs((x1+x2)**(1/SquircleBubble._squirclePower))

def radiusAngDeriv(a: float) -> float:
    if (SquircleBubble._width/2) <= 0 or (SquircleBubble._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubble._width} {SquircleBubble._height}')
    x1: float = -(SquircleBubble._width/2) * (SquircleBubble._height/2)

    x2: float = math.pow(SquircleBubble._height/2,SquircleBubble._squirclePower)*(-math.sin(a))*math.copysign(math.pow(abs(math.cos(a)),SquircleBubble._squirclePower-1),math.cos(a))
    x3: float = math.pow(SquircleBubble._width/2,SquircleBubble._squirclePower)*(math.cos(a))*math.copysign(math.pow(abs(math.sin(a)),SquircleBubble._squirclePower-1),math.sin(a))
    x4: float = x2+x3

    x5: float = abs(((SquircleBubble._height/2)*math.cos(a))**SquircleBubble._squirclePower)
    x6: float = abs(((SquircleBubble._width/2)*math.sin(a))**SquircleBubble._squirclePower)
    x7: float = abs((x5+x6)**(-1-(1/SquircleBubble._squirclePower)))

    return (x1*x4*x7)

def radiusXDeriv(a: float) -> float:
    if (SquircleBubble._width/2) <= 0 or (SquircleBubble._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubble._width} {SquircleBubble._height}')
    return ((radius(a))*(-math.sin(a))) + ((radiusAngDeriv(a))*(math.cos(a)))

def radiusYDeriv(a: float) -> float:
    if (SquircleBubble._width/2) <= 0 or (SquircleBubble._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubble._width} {SquircleBubble._height}')
    return ((radius(a))*(math.cos(a))) + ((radiusAngDeriv(a))*(math.sin(a)))

def radiusXDerivNorm(a: float) -> float:
    if (SquircleBubble._width/2) <= 0 or (SquircleBubble._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubble._width} {SquircleBubble._height}')
    r: float = radius(a)
    dr: float = radiusAngDeriv(a)
    xDeriv: float = radiusXDeriv(a)
    yDeriv: float = radiusYDeriv(a)
    ret: float = xDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
    return ret

def radiusYDerivNorm(a: float) -> float:
    if (SquircleBubble._width/2) <= 0 or (SquircleBubble._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubble._width} {SquircleBubble._height}')
    xDeriv = radiusXDeriv(a)
    yDeriv = radiusYDeriv(a)
    ret: float = yDeriv/( ((xDeriv*xDeriv) + (yDeriv*yDeriv))**0.5 )
    return ret

def squirclePoint(a: float) -> Point:
    """takes an angle 'a' and returns a point on the squircle

    ### Args:
        a (float): angle from positive x-axis to squircle point (0 <= x <= 2pi)

    ### Returns:
        Point: an x,y coordinate on the squircle
    """
    if (SquircleBubble._width/2) <= 0 or (SquircleBubble._height/2) <= 0: raise ValueError(f'squircle width and height must both be greater than zero: {SquircleBubble._width} {SquircleBubble._height}')
    xp: float = (radius(a)*math.cos(a))+(SquircleBubble._width /2)+SquircleBubble._tailLength
    yp: float = (radius(a)*math.sin(a))+(SquircleBubble._height/2)+SquircleBubble._tailLength
    return Point(xp, yp)

class SquircleBubble(SpeechBubble):

    _logger: logging.Logger = None

    _squirclePower: float = 2.8
    _numSquirclePoints: int = 200

    def getPreview() -> str:

        if SquircleBubble._logger is not None:
            SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'bubble width, height: {SquircleBubble._width} {SquircleBubble._height}')

        thetaD = SquircleBubble._tailAnglePosition
        thetaR = 2*math.pi*(SquircleBubble._tailAnglePosition/360)
        thetaDeltaD = SquircleBubble._tailWidth
        thetaDeltaR = 2*math.pi*(SquircleBubble._tailWidth/360)

        tBaseMidPoint   = squirclePoint(thetaR)
        tBaseLeftPoint  = squirclePoint(thetaR - thetaDeltaR)
        tBaseRightPoint = squirclePoint(thetaR + thetaDeltaR)

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
                tailEndPoint = tBaseMidPoint + ( SquircleBubble._tailLength*Point( radiusYDerivNorm(thetaR), -radiusXDerivNorm(thetaR) ) )
                pathPoints.append(tailEndPoint)
                pathPoints.append(tBaseRightPoint)
                if SquircleBubble._logger is not None:
                    SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'tail base mid point: {tBaseMidPoint}')
                    SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'tail points: {tBaseLeftPoint} {tailEndPoint} {tBaseRightPoint}')
            i += 1

        bubblePath = f'M {pathPoints[0].x} {pathPoints[0].y} L '
        for n in range(1,len(pathPoints)): bubblePath += f'{pathPoints[n].x} {pathPoints[n].y} '
        bubblePath += 'Z'

        # SquircleBubble._logger.log(LSBG_DEBUG_VERBOSE, f'squircle bubble path: {bubblePath}')

        return bubblePath