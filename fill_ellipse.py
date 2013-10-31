#fill_ellipse.py

#This function changes the color
#of certain pixels and fills a circle
#based on the points given

#NOTE that if you want a ellipse fill a different
#color from the border, you should redraw the circle
#as this function does not take into consideration
#that some of the points found may be apart of the
#border or a single point at the top or bottom of the shape

import copy
import draw_ellipse
import draw_line
import one_color


def main( x, y, majA, minB ):
    border = draw_ellipse.main( x, y, majA, minB )
    

    temp = one_color.struc()
    points = [ copy.deepcopy( one_color.struc ) ]
    length = len( border )

    for i in range( length - 1 ):
        for t in range( 1, length ):
            if border[ i ].y == border[ t ].y:
                fill = draw_line.main( border[ i ].x, border[ i ].y, border[ t ].x, border[ t ].y )
                length2 = len( fill )
                for e in range( length2 ):
                    temp.x = fill[ e ].x
                    temp.y = fill[ e ].y
                    points.append( copy.deepcopy( temp ) )
                #end e for loop
            #end of if-else statement
        #end of t for loop
    #end of i for loop
    
    del points[ 0 ]
    return points
                
        
