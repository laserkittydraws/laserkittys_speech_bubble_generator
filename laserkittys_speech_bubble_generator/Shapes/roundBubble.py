from laserkittys_speech_bubble_generator.Shapes.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION

from math import sin, cos, asin, sqrt
import logging

from laserkittys_speech_bubble_generator.config import *

class RoundBubble(SpeechBubble):

    _logger: logging.Logger = None

    def getPreview() -> str:
        if RoundBubble._width <= 0 or RoundBubble._height <= 0: raise ValueError(f'bubble width and height can not be zero: {RoundBubble._width} {RoundBubble._height}')
        if RoundBubble._tailLength > 0 and RoundBubble._tailWidth > 0:
            fourASqr = 4*(RoundBubble._width/2)*(RoundBubble._width/2)
            fourBSqr = 4*(RoundBubble._height/2)*(RoundBubble._height/2)

            if (sqrtDiscriminant := (fourASqr + fourBSqr)*sin(RoundBubble._tailAnglePosition)*sin(RoundBubble._tailAnglePosition) + fourBSqr) <= 0:
                RoundBubble._logger.log(logging.ERROR, f'sqrt discriminant not in domain (x>0): {sqrtDiscriminant}')
            elif (asinDiscriminant := RoundBubble._tailWidth / sqrt( (fourASqr + fourBSqr)*sin(RoundBubble._tailAnglePosition)*sin(RoundBubble._tailAnglePosition) + fourBSqr )) < -1 or asinDiscriminant > 1:
                RoundBubble._logger.log(logging.ERROR, f'asin discriminant not in domain (-1<x<1): {asinDiscriminant}')

            RoundBubble._tailAnglePositionD = asin(RoundBubble._tailWidth / sqrt( (fourASqr + fourBSqr)*sin(RoundBubble._tailAnglePosition)*sin(RoundBubble._tailAnglePosition) + fourBSqr ))

            tailPointX0 = ((RoundBubble._width  / 2)*cos(RoundBubble._tailAnglePosition - RoundBubble._tailAnglePositionD)) + ((RoundBubble._width + 2*RoundBubble._tailLength)  / 2)
            tailPointY0 = ((RoundBubble._height / 2)*sin(RoundBubble._tailAnglePosition - RoundBubble._tailAnglePositionD)) + ((RoundBubble._height + 2*RoundBubble._tailLength) / 2)
            tailPointX1 = ((RoundBubble._width  / 2)*cos(RoundBubble._tailAnglePosition + RoundBubble._tailAnglePositionD)) + ((RoundBubble._width + 2*RoundBubble._tailLength)  / 2)
            tailPointY1 = ((RoundBubble._height / 2)*sin(RoundBubble._tailAnglePosition + RoundBubble._tailAnglePositionD)) + ((RoundBubble._height + 2*RoundBubble._tailLength) / 2)

            dX = (RoundBubble._width  / 2) * sin(RoundBubble._tailAnglePosition) * -1
            dY = (RoundBubble._height / 2) * cos(RoundBubble._tailAnglePosition)
            tailEndX = (RoundBubble._width  / 2) * cos(RoundBubble._tailAnglePosition) + ((RoundBubble._width + 2*RoundBubble._tailLength)  / 2) + (max(RoundBubble._tailLength,1) * (dY / sqrt(dX*dX + dY*dY)))
            tailEndY = (RoundBubble._height / 2) * sin(RoundBubble._tailAnglePosition) + ((RoundBubble._height + 2*RoundBubble._tailLength) / 2) - (max(RoundBubble._tailLength,1) * (dX / sqrt(dX*dX + dY*dY)))
            
            if RoundBubble._logger is not None:
                RoundBubble._logger.log(LSBG_DEBUG_VERBOSE, f'tail angle position: {RoundBubble._tailAnglePosition}, tail angle position delta: {RoundBubble._tailAnglePositionD}, \
                    tail width: {RoundBubble._tailWidth}, tail length: {RoundBubble._tailLength}, \
                    tail points: ({tailPointX0},{tailPointY0}) ({tailPointX1},{tailPointY1}) ({tailEndX},{tailEndY})')

            return (
                f'M {tailPointX0} {tailPointY0} A {RoundBubble._width/2} {RoundBubble._height/2} ' +
                f'0 1 0 {tailPointX1} {tailPointY1} L {tailEndX} {tailEndY} Z'
            )

        else:
            ellipsePX = (RoundBubble._width/2) + ((RoundBubble._width + 2*RoundBubble._tailLength)/2)
            ellipsePY = (RoundBubble._height + 2*RoundBubble._tailLength)/2

            if RoundBubble._logger is not None:
                RoundBubble._logger.log(LSBG_DEBUG_VERBOSE,
                    f'tail disabled, ellipse points: ({ellipsePX-RoundBubble._width}, {ellipsePY}) ({ellipsePX}, {ellipsePY})'
                )

            return (
                f'M {ellipsePX} {ellipsePY} ' +
                f'A {RoundBubble._width/2} {RoundBubble._height/2} 0 1 0 {ellipsePX-RoundBubble._width} {ellipsePY}' +
                f'A {RoundBubble._width/2} {RoundBubble._height/2} 0 1 0 {ellipsePX} {ellipsePY} Z'
            )