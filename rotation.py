#rotation.py

#Rotates a line about a specific point

import translation
import math

def main( x1, y1, x2, y2, xf, yf, d ):

    line = translation.main( x1, y1, x2, y2, -xf, -yf )
    r = math.radians( d )

    #translated start and end points
    x1 = line[ 0 ].x
    y1 = line[ 0 ].y
    x2 = line[ 1 ].x
    y2 = line[ 1 ].y

    cos = math.cos( r )
    sin = math.sin( r )

    #Start point for line
    first = x1 * cos
    second = y1 * sin
    newX1 = round( first - second )

    first = y1 * cos
    second = x1 * sin
    newY1 = round( first + second )

    #End point for line
    first = x2 * cos
    second = y2 * sin
    newX2 = round( first - second )

    first = y2 * cos
    second = x2 * sin
    newY2 = round( first + second )

    line = translation.main( newX1, newY1, newX2, newY2, xf, yf )


    return line
