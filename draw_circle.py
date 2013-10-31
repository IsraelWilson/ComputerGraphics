#draw_circle.py

#This function changes the color
#of certain pixels to draw a circle
#based on the parameters given

import copy
import one_color
import math

def main( x, y, r ):
    temp = one_color.struc()
    points = [ copy.deepcopy( one_color.struc ) ]
    yC = 0
    xC = r
    octant = 2
    
    temp.x = xC
    temp.y = yC
    points.append( copy.deepcopy( temp ) )

    while xC >= yC:
        yC = yC + 1
        xC = math.sqrt( pow( r, 2 ) - pow( yC, 2 ) )
        xC = int( xC )
        temp.x = xC
        temp.y = yC
        points.append( copy.deepcopy( temp ) )
        #end of while
        #points for first octant
           
    length = len( points )
    
    while octant <= 8:       
        for c in range( 1, length ):
            #Find the other symetric points
            #When adding the center, might need to increase length by 1
            #to add center to actual poitns. Point[ 0 ] is empty.
            if octant == 2:
                newVal = points[ c ]
                temp.x = newVal.y
                temp.y = newVal.x
                points.append( copy.deepcopy( temp ) )
            elif octant == 3:
                newVal = points[ c ]
                temp.x = -1 * newVal.y
                temp.y = newVal.x
                points.append( copy.deepcopy( temp ) )
            elif octant == 4:
                newVal = points[ c ]
                temp.x = -1 * newVal.x
                temp.y = newVal.y
                points.append( copy.deepcopy( temp ) )
            elif octant == 5:
                newVal = points[ c ]
                temp.x = -1 * newVal.x
                temp.y = -1 * newVal.y
                points.append( copy.deepcopy( temp ) )
            elif octant == 6:
                newVal = points[ c ]
                temp.x = -1 * newVal.y
                temp.y = -1 * newVal.x
                points.append( copy.deepcopy( temp ) )
            elif octant == 7:
                newVal = points[ c ]
                temp.x = newVal.y
                temp.y = -1 * newVal.x
                points.append( copy.deepcopy( temp ) )
            elif octant == 8:
                newVal = points[ c ]
                temp.x = newVal.x
                temp.y = -1 * newVal.y
                points.append( copy.deepcopy( temp ) )
            else:
                print( 'There was an error' )
            #end inner if-else statements
        #end of inner for loop
        octant = octant + 1
        #end of while loop

    length = len( points )              
    for t in range( 1, length ):
        points[ t ].y = points[ t ].y + y
        points[ t ].x = points[ t ].x + x


    
    del points[ 0 ]

    for i in range( len( points ) ):
        print( points[ i ].x, points[ i ].y )
        
    return points
        




