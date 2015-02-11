# Portolan

Convert between [compass points](https://en.wikipedia.org/wiki/Points_of_the_compass) and degrees. It's a super tiny library with no dependencies.

````
pip install portolan
````

## Methods

Just a few:
`point`, `traditional`, `degrees`, `middle`, `range`.

## Examples

Convert from abbreviations or a decimal degree to the compass point:

````python
import portolan

portolan.point(abbr='nnw')
# 'north-northwest'

portolan.point(degree=275.1)
# 'west'
````

Convert to traditional names of the Mediterranean basin:

```python
portolan.traditional(degree=12.6)
# 'Quarto di Tramontana verso Greco'

portolan.traditional(abbr='NEbE')
# 'Quarto di Greco verso Levante'
````

Convert between degrees and abbrevations:

````python
portolan.abbr(145.0)
# 'SEbS'

portolan.middle('SEbS')
# 146.25

portolan.range('SEbS')
# (140.625, 151.875)

# Remember that North spans the origin
portolan.range('n')
# (354.375, 5.625)

# the degrees method returns the minimum, middle, and maximum of a compass point
portolan.degrees('SEbS')
# (140.625, 146.25, 151.875)
````
