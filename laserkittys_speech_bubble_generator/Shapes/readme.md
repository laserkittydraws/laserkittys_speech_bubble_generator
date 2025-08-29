# Speech Bubble Subclass Implementation Guide

The [base class](speech_bubble_base.py) already has the attributes along with cooresponding get and set methods:
```python
_width: float
_height: float
_tailAnglePosition: float # 0 <= x <= 360
_tailWidth: float
_tailLength: float
```

## Boilerplate

```python
from laserkittys_speech_bubble_generator.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION
from laserkittys_speech_bubble_generator.config import *

class YourSpeechBubbleType(SpeechBubble):

    """
    other internal methods your speech bubble type
    may need for your implementation (not required)
    """
    def _method1(): ...
    def _method2(): ...
    def _method3(): ...
    ...

    def getPreview() -> str:
        """
        [your code here]
        """

    def __repr__() -> str:
        return f'[your custom attrubtes here], {super.__repr__()}'
```

Base classes also exist for `RoundBubble`, `SquareBubble`, and `SquircleBubble` which alread have implemented methods for getting a point on the shape, the radius and its derivative, and the regular and normalized x and y derivative

> [!TIP]
> It is recommended to include log statements within your code implementation of your speech bubble type for debugging. The base class already has a logger to use: `YourSpeechBubbleType._logger`

## Anatomy of a speech bubble

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/laserkittydraws/laserkittys_speech_bubble_generator/refs/heads/main/images/lsbg%20graphic%20dark.png">
    <img src="https://raw.githubusercontent.com/laserkittydraws/laserkittys_speech_bubble_generator/refs/heads/main/images/lsbg%20graphic%20light.png">
</picture>