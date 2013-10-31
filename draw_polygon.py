#draw_polygon.py

#This function changes the color
#of certain pixels to draw a polygon
#based on the parameters given

import copy
import one_color
import draw_line

def main( *args ):
    temp = one_color.struc()
    points = [ copy.deepcopy( one_color.struc ) ]

    length = len( args )
    for x1 in range( 0, length - 3, 2 ):
        y1 = x1 + 1
        x2 = y1 + 1
        y2 = x2 + 1
        line = draw_line.main( args[ x1 ], args[ y1 ], args[ x2 ], args[ y2 ] )
        length2 = len( line )
        for i in range( length2 ):
            temp.x = line[ i ].x
            temp.y = line[ i ].y
            points.append( copy.deepcopy( temp ) )

    line = draw_line.main( args[ length - 2 ], args[ length - 1 ], args[ 0 ], args[ 1 ] )
    length2 = len( line )
    for i in range( length2 ):
            temp.x = line[ i ].x
            temp.y = line[ i ].y
            points.append( copy.deepcopy( temp ) )
    


    del points[ 0 ]         
    return points
