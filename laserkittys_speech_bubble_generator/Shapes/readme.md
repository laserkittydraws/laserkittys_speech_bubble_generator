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

> [!TIP]
> It is recommended to include log statements within your code implementation of your speech bubble type for debugging. The base class already has a logger to use: `YourSpeechBubbleType._logger`

## Anatomy of a speech bubble

```
 +--------------------------------------------------------------------------------> X
 |          tailLength
 |   <-------->
 |                                 padding           (  theta = 0 starts  )
 |                              <---->               ( at the pos x-axis, )
 |            <---- bubbleWidth  ---->               ( theta increases CW )
 |                 <-textWidth ->
 |   +----------------------------------------+                                  /|\
 |   |                                        |                                   |
 |   |                                        |                                   |
 |   |        +----------------------+        | /|\             /|\               | frameHeight
 |   |        |                      |        |  | padding       |                |
 |   |        |                      |        | \|/              |                |
 |   |        |    +------------+    |        | /|\              | bubbleHeight   |
 |   |        |    |            |    |        |  |               |                |
 |   |        |    |    text    |    |        |  | textHeight    |                |
 |   |        |    |            |    |        |  |               |                |
 |   |        |    +------------+    |        | \|/              |                |
 |   |        |                      |        |                  |                |
 |   |        |                      |        |                  |                |
 |   |        +----------------------+        | /|\             \|/               |
 |   |          \    /                        |  | tailLength                     |
 |   |           \  /                         |  |                                |
\|/  +----------------------------------------+ \|/                              \|/
 Y
```