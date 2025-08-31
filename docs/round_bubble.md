# RoundBubbleBase

<div style="text-align:center">

```mermaid
graph BT;
RoundBubbleBase --> SpeechBubble;
```

</div>

## Description

Base class for implementing custom speech bubble types that follow a round elliptical shape

Some guides for SVG formatting:
- https://www.w3schools.com/graphics/svg_intro.asp
- https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch

## Attributes

<details>

<summary>Attributes inherited from SpeechBubble</summary>

- `_width` float
- `_height` float
- `_tailAnglePosition` float
- `_tailWidth` float
- `_tailLength` float

</details>

## Methods

#### `radius()`
    returns the radius of the ellipse at a given angle

#### `radiusDeriv()`
    returns the derivative of the radius of the ellipse at a given angle

#### `radiusXDeriv()`
    returns the derivative of the ellipse in the x-direction at a given angle

#### `radiusXDerivNorm()`
    returns the normalized derivative of the ellipse in the x-direction at a given angle

#### `radiusYDeriv()`
    returns the derivative of the ellipse in the y-direction at a given angle

#### `radiusYDerivNorm()`
    returns the normalized derivative of the ellipse in the y-direction at a given angle

<details>

<summary>Methods inherited from SpeechBubble</summary>

#### `clear()`
    resets all attributes to zero

#### `getPreview()`
    not implemented

#### `height()`
    returns the height of the bubble

#### `setHeight()`
    sets the height of the bubble

#### `setTailAnglePosition()`
    sets the angle position of the bubble tail

#### `setTailLength()`
    sets the length of the bubble tail

#### `setTailWidth()`
    sets the width of the bubble tail

#### `setup()`
    a method to initialize all the attributes at once

#### `setWidth()`
    sets the width of the bubble

#### `tailAnglePosition()`
    returns the angle position of the bubble tail

#### `tailLength()`
    returns the length of the bubble tail

#### `tailWidth()`
    returns the width of the bubble tail

#### `width()`
    returns the width of the bubble

</details>