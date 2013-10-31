#projection.py

import one_color
import copy

def main( d, args ):
    temp = one_color.struc()
    points = []

    #Turns every XYZ coordinate to its 2D equivalent
    length = len( args )
    for i in range( 0, length - 2, 3 ):
        yAP1 = ( args[ i + 1 ] * d ) / args[ i + 2 ]
        xAP1 = ( args[ i ] * d ) / args[ i + 2 ]
        temp.x = xAP1
        temp.y = yAP1
        points.append( copy.deepcopy( temp ) )

    return points
