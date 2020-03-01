# Artificial-Neural-Network-for-Truth-Tables
Introductory level neural network

<br />

## Activation Functions 
>### Sigmoid(x) = 1/(1+e<sup>-x</sup>)

<br />

## (A xor B) and D
```
A xor B = AB' + A'B
```
*`Truth Table:`*
|   a  |   b   |   c=ab'+a'b   |   d   |   e=c.d   |
|:----:|:-----:|:-------------:|:-----:|:---------:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 |
