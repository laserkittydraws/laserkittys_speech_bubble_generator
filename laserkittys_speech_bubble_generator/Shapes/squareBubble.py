from laserkittys_speech_bubble_generator.Shapes.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION

from math import sin, cos, asin, sqrt
import logging

from laserkittys_speech_bubble_generator.config import *

class SquareBubble(SpeechBubble):

    _logger: logging.Logger = None

    def getPreview() -> str:
        if SquareBubble._width <= 0 or SquareBubble._height <= 0: raise ValueError(f'bubble width and height can not be zero: {SquareBubble._width} {SquareBubble._height}')
        A0 =                              -0.5*(SquareBubble._height/2)/(2*(SquareBubble._width/2) + 2*(SquareBubble._height/2))
        A1 =                               0.5*(SquareBubble._height/2)/(2*(SquareBubble._width/2) + 2*(SquareBubble._height/2)) # upper right corner
        A2 =   ((SquareBubble._width/2) + 0.5*(SquareBubble._height/2))/(2*(SquareBubble._width/2) + 2*(SquareBubble._height/2)) # upper left corner
        A3 =   ((SquareBubble._width/2) + 1.5*(SquareBubble._height/2))/(2*(SquareBubble._width/2) + 2*(SquareBubble._height/2)) # lower left corner
        A4 = (2*(SquareBubble._width/2) + 1.5*(SquareBubble._height/2))/(2*(SquareBubble._width/2) + 2*(SquareBubble._height/2)) # lower right corner
        A5 =                          1 + (1.5*(SquareBubble._height/2)/(2*(SquareBubble._width/2) + 2*(SquareBubble._height/2)))

        def squareBubbleX(a):
            if A0 <= a < A1: return (SquareBubble._width/2)
            if A1 <= a < A2: return (1 - 2*(a-A1)/(A2-A1))*(SquareBubble._width/2)
            if A2 <= a < A3: return -(SquareBubble._width/2)
            if A3 <= a < A4: return (-1 + 2*(a-A3)/(A4-A3))*(SquareBubble._width/2)
            if A4 <= a < A5: return (SquareBubble._width/2)
            if SquareBubble._logger is not None:
                SquareBubble._logger.log(LSBG_DEBUG_VERBOSE, f'angle value not in range: {360*a}')
            raise ValueError(f'value not in range: {a}')

        def squareBubbleY(a):
            if A0 <= a < A1: return ((a)/(A1))*(SquareBubble._height/2)
            if A1 <= a < A2: return (SquareBubble._height/2)
            if A2 <= a < A3: return (1 - 2*(a-A2)/(A3-A2))*(SquareBubble._height/2)
            if A3 <= a < A4: return -(SquareBubble._height/2)
            if A4 <= a < A5: return (-1 + (a-A4)/(1-A4))*(SquareBubble._height/2)
            if SquareBubble._logger is not None:
                SquareBubble._logger.log(LSBG_DEBUG_VERBOSE, f'angle value not in range: {360*a}')
            raise ValueError(f'value not in range: {a}')

        tailPointX0 = squareBubbleX((SquareBubble._tailAnglePosition-SquareBubble._tailWidth)/360)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)
        tailPointY0 = squareBubbleY((SquareBubble._tailAnglePosition-SquareBubble._tailWidth)/360)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)
        tailPointX1 = squareBubbleX((SquareBubble._tailAnglePosition+SquareBubble._tailWidth)/360)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)
        tailPointY1 = squareBubbleY((SquareBubble._tailAnglePosition+SquareBubble._tailWidth)/360)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)
        if (SquareBubble._tailAnglePosition/360) < A1-(SquareBubble._tailWidth/360): # right wall
            #    +----------------+
            #    |                | >
            #    |                |
            #    |                |
            #    +----------------+
            tailEndX = squareBubbleX(SquareBubble._tailAnglePosition/360)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)+SquareBubble._tailLength
            tailEndY = squareBubbleY(SquareBubble._tailAnglePosition/360)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)
            bubblePath = f'M {tailPointX0} {tailPointY0} L {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} Z'
        elif (SquareBubble._tailAnglePosition/360) < A1+(SquareBubble._tailWidth/360): # upper right corner
            #                          *
            #                        *
            #     +----------------+
            #     |                |
            #     |                |
            #     |                |
            #     +----------------+
            tailEndX = (SquareBubble._width /2)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)+(0.5*sqrt(2)*SquareBubble._tailLength)
            tailEndY = (SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)+(0.5*sqrt(2)*SquareBubble._tailLength)
            bubblePath = f'M {tailPointX0} {tailPointY0} L {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} Z'
        elif (SquareBubble._tailAnglePosition/360) < A2-(SquareBubble._tailWidth/360): # upper wall
            #                /\
            #     +----------------+
            #     |                |
            #     |                |
            #     |                |
            #     +----------------+
            tailEndX = squareBubbleX(SquareBubble._tailAnglePosition/360)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)
            tailEndY = squareBubbleY(SquareBubble._tailAnglePosition/360)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)+SquareBubble._tailLength
            bubblePath = f'M {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {((SquareBubble._height + 2*SquareBubble._tailLength)/2)} L {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {tailPointX0} {tailPointY0} {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} Z'
        elif (SquareBubble._tailAnglePosition/360) < A2+(SquareBubble._tailWidth/360): # upper left corner
            # *
            #   *
            #     +----------------+
            #     |                |
            #     |                |
            #     |                |
            #     +----------------+
            tailEndX = -(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)-(0.5*sqrt(2)*SquareBubble._tailLength)
            tailEndY = (SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)+(0.5*sqrt(2)*SquareBubble._tailLength)
            bubblePath = f'M {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {((SquareBubble._height + 2*SquareBubble._tailLength)/2)} L {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {tailPointX0} {tailPointY0} {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} Z'
        elif (SquareBubble._tailAnglePosition/360) < A3-(SquareBubble._tailWidth/360): # left wall
            #     +----------------+
            #     |                |
            #     |                |
            #   < |                |
            #     +----------------+
            tailEndX = squareBubbleX(SquareBubble._tailAnglePosition/360)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)-SquareBubble._tailLength
            tailEndY = squareBubbleY(SquareBubble._tailAnglePosition/360)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)
            bubblePath = f'M {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {((SquareBubble._height + 2*SquareBubble._tailLength)/2)} L {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {tailPointX0} {tailPointY0} {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} Z'
        elif (SquareBubble._tailAnglePosition/360) < A3+(SquareBubble._tailWidth/360): # lower left corner
            #     +----------------+
            #     |                |
            #     |                |
            #     |                |
            #     +----------------+
            #   *
            # *
            tailEndX = -(SquareBubble._width /2)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)-(0.5*sqrt(2)*SquareBubble._tailLength)
            tailEndY = -(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)-(0.5*sqrt(2)*SquareBubble._tailLength)
            bubblePath = f'M {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {((SquareBubble._height + 2*SquareBubble._tailLength)/2)} L {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {tailPointX0} {tailPointY0} {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} Z'
        elif (SquareBubble._tailAnglePosition/360) < A4-(SquareBubble._tailWidth/360): # lower wall
            #     +----------------+
            #     |                |
            #     |                |
            #     |                |
            #     +----------------+
            #                \/
            tailEndX = squareBubbleX(SquareBubble._tailAnglePosition/360)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)
            tailEndY = squareBubbleY(SquareBubble._tailAnglePosition/360)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)-SquareBubble._tailLength
            bubblePath = f'M {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {((SquareBubble._height + 2*SquareBubble._tailLength)/2)} L {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {tailPointX0} {tailPointY0} {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} Z'
        elif (SquareBubble._tailAnglePosition/360) < A4+(SquareBubble._tailWidth/360): # lower right corner
            #     +----------------+
            #     |                |
            #     |                |
            #     |                |
            #     +----------------+
            #                        *
            #                          *
            tailEndX =  (SquareBubble._width /2)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)+(0.5*sqrt(2)*SquareBubble._tailLength)
            tailEndY = -(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)-(0.5*sqrt(2)*SquareBubble._tailLength)
            bubblePath = f'M {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} L {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {tailPointX0} {tailPointY0} {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} Z'
        elif (SquareBubble._tailAnglePosition/360) < A5: # right wall
            #     +----------------+
            #     |                |
            #     |                |
            #     |                | >
            #     +----------------+
            tailEndX = squareBubbleX(SquareBubble._tailAnglePosition/360)+((SquareBubble._width + 2*SquareBubble._tailLength) /2)+SquareBubble._tailLength
            tailEndY = squareBubbleY(SquareBubble._tailAnglePosition/360)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)
            bubblePath = f'M {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} L {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {(SquareBubble._width/2)+((SquareBubble._width + 2*SquareBubble._tailLength)/2)} {-(SquareBubble._height/2)+((SquareBubble._height + 2*SquareBubble._tailLength)/2)} {tailPointX0} {tailPointY0} {tailEndX} {tailEndY} {tailPointX1} {tailPointY1} Z'

        if SquareBubble._logger is not None:
            SquareBubble._logger.log(LSBG_DEBUG_VERBOSE, f'angle values: {360*A0}, {360*A1}, {360*A2}, {360*A3}, {360*A4}, {360*A5}')

        return bubblePath