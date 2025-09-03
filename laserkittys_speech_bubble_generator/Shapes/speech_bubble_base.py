from laserkittys_speech_bubble_generator.Shapes.misc import Point

import math

import logging

SPEECH_BUBBLE_BASE_VERSION = '1.2'

class SpeechBubble:

    """
    Base class for implementing custom speech bubble types


    some guides for SVG formatting:

    https://www.w3schools.com/graphics/svg_intro.asp

    https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch
    """

    _width: float = 0
    _height: float = 0

    _tailAnglePosition: float = 0 # 0 <= x <= 360
    _tailWidth: float = 0
    _tailLength: float = 0

    _logger: logging.Logger = None

    @staticmethod
    def radius(a: float) -> float:
        raise NotImplementedError

    @staticmethod
    def radiusDeriv(a: float) -> float:
        raise NotImplementedError

    @staticmethod
    def radiusXDeriv(a: float) -> float:
        raise NotImplementedError

    @staticmethod
    def radiusYDeriv(a: float) -> float:
        raise NotImplementedError

    @staticmethod
    def radiusDerivVec(a: float) -> Point:
        raise NotImplementedError

    @staticmethod
    def radiusMagnitude(a: float) -> float:
        raise NotImplementedError

    @staticmethod
    def radiusXDerivNorm(a: float) -> float:
        raise NotImplementedError

    @staticmethod
    def radiusYDerivNorm(a: float) -> float:
        raise NotImplementedError

    @staticmethod
    def radiusDerivNormVec(a: float) -> Point:
        raise NotImplementedError

    @staticmethod
    def width() -> float:
        return SpeechBubble._width

    @staticmethod
    def setWidth(w: float) -> None:
        if w < 0:
            SpeechBubble._logger.log(logging.ERROR, f'bubble width can not be less than zero: {w}')
            raise ValueError(f'bubble width can not be less than zero: {w}')
        else: SpeechBubble._width = w

    @staticmethod
    def height() -> float:
        return SpeechBubble._height

    @staticmethod
    def setHeight(h: float) -> None:
        if h < 0:
            SpeechBubble._logger.log(logging.ERROR, f'bubble height can not be less than zero: {h}')
            raise ValueError(f'bubble width can not be less than zero: {h}')
        else: SpeechBubble._height = h

    @staticmethod
    def tailAnglePosition() -> float:
        return SpeechBubble._tailAnglePosition

    @staticmethod
    def setTailAnglePosition(a: float):
        """
        sets the angle position of the speech bubble tail

        ### Args:
            a (float): new angle position (0 <= x <= 360)

        ### Raises:
            ValueError: new angle value out of bounds
        """
        if 0 <= a and a <= 360: SpeechBubble._tailAnglePosition = a
        else: raise ValueError(f'new angle value out of bounds (0 <= x <= 360): {a}')

    @staticmethod
    def tailWidth() -> float:
        return SpeechBubble._tailWidth

    @staticmethod
    def setTailWidth(tW: float) -> None:
        if tW < 0:
            SpeechBubble._logger.log(logging.ERROR, f'tail width can not be less than zero: {tW}')
            raise ValueError(f'tail width can not be less than zero: {tW}')
        else: SpeechBubble._tailWidth = tW

    @staticmethod
    def tailLength() -> float:
        return SpeechBubble._tailLength

    @staticmethod
    def setTailLength(tL: float) -> None:
        if tL < 0:
            SpeechBubble._logger.log(logging.ERROR, f'tail length can not be less than zero: {tL}')
            raise ValueError(f'tail length can not be less than zero: {tL}')
        else: SpeechBubble._tailLength = tL

    @staticmethod
    def setup(
        width: float = 0,
        height: float = 0,
        tailAnglePosition: float = 0,
        tailWidth: float = 0,
        tailLength: float = 0
    ) -> None:

        SpeechBubble._width = width
        SpeechBubble._height = height
        SpeechBubble._tailAnglePosition = tailAnglePosition
        SpeechBubble._tailWidth = tailWidth
        SpeechBubble._tailLength = tailLength

    @staticmethod
    def clear() -> None:
        SpeechBubble._width = 0
        SpeechBubble._height = 0
        SpeechBubble._tailAnglePosition = 0
        SpeechBubble._tailWidth = 0
        SpeechBubble._tailLength = 0

    @staticmethod
    def getPreview() -> str:
        """
        returns the svg path data for the speech bubble

        ### Returns:
            svg path data (str)
        """
        raise NotImplementedError('subclass method not implemented yet')

    @staticmethod
    def __repr__() -> str:
        return f'speech bubble base version: {SPEECH_BUBBLE_BASE_VERSION}, tail angle position: {SpeechBubble._tailAnglePosition}, tail width: {SpeechBubble._tailWidth}, tail length: {SpeechBubble._tailLength}\n'