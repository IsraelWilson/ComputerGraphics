#draw_ellipse.py

#This function changes the color
#of certain pixels to draw an ellipse
#based on the parameters given

import copy
import one_color
import math

def main( x, y, majA, minB ):
    temp = one_color.struc()
    points = [ copy.deepcopy( one_color.struc ) ]
    xC = majA
    yC = 0
    quadrant = 2
    half = 1 / 2
    aSquared = pow( majA, 2 )
    bSquared = pow( minB, 2 )

    temp.x = xC
    temp.y = yC
    points.append( copy.deepcopy( temp ) )

    accept1 = True
    accept2 = True
    
    #In region 2
    while accept1:
        if ( aSquared * ( yC + 1 ) ) < ( bSquared * ( xC - half ) ):
            yC = yC + 1
            ySquared = pow( yC, 2 )

            #Find the next x and y values
            frac = ySquared / bSquared
            minusFrac = 1 - frac
            times = aSquared * minusFrac
            xC = math.sqrt( times )
            xC = round( xC )
            temp.x = xC
            temp.y = yC
            points.append( copy.deepcopy( temp ) )
            if ( aSquared * ( yC + 1 ) ) >= ( bSquared * ( xC - half ) ):
                accept1 = False

    #In region 1
    while accept2:
        xC = xC - 1
        xSquared = pow( xC, 2 )

        #Find the next x and y values
        frac = xSquared / aSquared
        minusFrac = 1 - frac
        times = bSquared * minusFrac
        yC = math.sqrt( times )
        yC = round( yC )            
        temp.x = xC
        temp.y = yC
        points.append( copy.deepcopy( temp ) )
        if xC <= 0:
            accept2 = False
            

    length = len( points )
    #Find all other symetric points
    while quadrant <= 4:       
        for c in range( 1, length ):
            if quadrant == 2:
                newVal = points[ c ]
                temp.x = -1 * newVal.x
                temp.y = newVal.y
                points.append( copy.deepcopy( temp ) )
            elif quadrant == 3:
                newVal = points[ c ]
                temp.x = -1 * newVal.x
                temp.y = -1 * newVal.y
                points.append( copy.deepcopy( temp ) )
            elif quadrant == 4:
                newVal = points[ c ]
                temp.x = newVal.x
                temp.y = -1 * newVal.y
                points.append( copy.deepcopy( temp ) )
            else:
                print( 'There was an error' )
            #end inner if-else statements
        #end c for loop
        quadrant = quadrant + 1
    #end of while loop

    length = len( points )              
    for f in range( 1, length ):
        points[ f ].y = points[ f ].y + y
        points[ f ].x = points[ f ].x + x

    del points[ 0 ]
    return points
