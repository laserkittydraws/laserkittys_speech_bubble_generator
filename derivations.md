# Derivations

## Ellipse Constant Width Chord Angle Delta

Given an ellipse defined by $`(x-h)^2/a^2 + (y-k)^2/b^2 = 1`$:

```math
x=a*cos(\theta)+h
```
```math
y=b*sin(\theta)+k
```

$`d=\sqrt{ \left( (x_L-x_R)^2 + (y_L-y_R)^2 \right) }`$

$`d=\sqrt{ ( a*cos(\theta + \theta_d) - a*cos(\theta - \theta_d) )^2 + ( b*sin(\theta + \theta_d) - b*sin(\theta - \theta_d) )^2 }`$

$`d=\sqrt{ a^2( cos(\theta + \theta_d) - cos(\theta - \theta_d) )^2 + b^2( sin(\theta + \theta_d) - sin(\theta - \theta_d) )^2 }`$

$`d=\sqrt{ a^2( cos(\theta)cos(\theta_d)-sin(\theta)sin(\theta_d) - (cos(\theta)cos(\theta_d)+sin(\theta)sin(\theta_d)) )^2 + b^2( sin(\theta)cos(\theta_d)-cos(\theta)sin(\theta_d) - (sin(\theta)cos(\theta_d)+cos(\theta)sin(\theta_d)) )^2 }`$

$`d=\sqrt{ a^2(-2sin(\theta)sin(\theta_d))^2 + b^2(2cos(\theta)sin(\theta_d)) }`$

$`d=\sqrt{ 4a^2sin^2(\theta)sin^2(\theta_d) + 4b^2cos^2(\theta)sin^2(\theta_d) }`$

$`d=sin(\theta_d)\sqrt{ 4a^2sin^2(\theta) + 4b^2(1-sin^2(\theta)) }`$

$`d=sin(\theta_d)\sqrt{ (4a^2-4b^2)sin^2(\theta) + 4b^2 }`$

$`sin(\theta_d)=d / \sqrt{ (4a^2-4b^2)sin^2(\theta) + 4b^2 }`$

$`\theta_d=sin^-1(d / \sqrt{ (4a^2-4b^2)sin^2(\theta) + 4b^2 })`$