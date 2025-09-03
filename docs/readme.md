# Speech Bubble Subclass Implementation Guide

## Anatomy of a speech bubble

<div style="text-align:center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/laserkittydraws/laserkittys_speech_bubble_generator/refs/heads/main/images/lsbg%20graphic%20dark.png">
        <img width=75% src="https://raw.githubusercontent.com/laserkittydraws/laserkittys_speech_bubble_generator/refs/heads/main/images/lsbg%20graphic%20light.png">
    </picture>
</div>

## Boilerplate Code

```ruby
from laserkittys_speech_bubble_generator.Shapes.speech_bubble_base import SpeechBubble, SPEECH_BUBBLE_BASE_VERSION
# OR
from laserkittys_speech_bubble_generator.Shapes.(round/square/squircle)BubbleBase import (Round/Square/Squircle)BubbleBase

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
        return super.__repr__() + f'[your custom attrubtes here]'
```

Base classes also exist for round, square, and squircle shapes which alread have implemented methods for getting a point on the shape, the radius and its derivative, and the regular and normalized x and y derivative: [`RoundBubbleBase`](/docs/round_bubble.md), [`SquareBubbleBase`](/docs/square_bubble.md), and [`SquircleBubbleBase`](/docs/squircle_bubble.md)

> [!TIP]
> It is recommended to include log statements within your code implementation of your speech bubble type for debugging. The base class already has a logger to use: `YourSpeechBubbleType._logger`