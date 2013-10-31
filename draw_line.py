#draw_line.py

#This function changes the color
#of certain pixels to draw a line
#based on the points given

#NOTE: updated function checks for the case
#that the x1 or y1 values are greater than
#thier x2, y2 counterparts and draws the line
#in reverse order, else the for loops doesnt
#execute and points arent returned

import copy
import one_color

def main( x1, y1, x2, y2 ):
    temp = one_color.struc()
    linepoints = [ copy.deepcopy( one_color.struc ) ]
    xLen = abs( x1 - x2 )
    yLen = abs( y1 - y2 )

    temp.x = x1
    temp.y = y1
    linepoints.append( copy.deepcopy( temp ) )
    
    if xLen > yLen:
        if x2 > x1:
            for i in range( x1 + 1, x2 ):
                temp.x = i
                m = ( y2 - y1 ) / ( x2 - x1 )
                first = -1 * m
                second = first * x1
                b = second + y1
                yPoint = ( m * i ) + b
                temp.y = round( yPoint )
                linepoints.append( copy.deepcopy( temp ) )
            #end for loop on i
        else:
            for i in range( x1 - 1, x2, -1 ):
                temp.x = i
                m = ( y2 - y1 ) / ( x2 - x1 )
                first = -1 * m
                second = first * x1
                b = second + y1
                yPoint = ( m * i ) + b
                temp.y = round( yPoint )
                linepoints.append( copy.deepcopy( temp ) )
            #end for loop on i
            
    else:
        if y2 > y1:
            for t in range( y1 + 1, y2 ):
                temp.y = t
                #break function into smaller parts
                fraction = ( x2 - x1 ) / ( y2 - y1 )
                first = fraction * t
                second = ( fraction * y1 )
                third = first - second
                xPoint = third + x1
                temp.x = round( xPoint )
                linepoints.append( copy.deepcopy( temp ) )
            #end for loop on t
        else:
            for t in range( y1 - 1, y2, -1 ):
                temp.y = t
                #break function into smaller parts
                fraction = ( x2 - x1 ) / ( y2 - y1 )
                first = fraction * t
                second = ( fraction * y1 )
                third = first - second
                xPoint = third + x1
                temp.x = round( xPoint )
                linepoints.append( copy.deepcopy( temp ) )
            #end for loop on t
    #end if else statement
    temp.x = x2
    temp.y = y2
    linepoints.append( copy.deepcopy( temp ) )
    
    del linepoints[ 0 ] #remove ununsed locatation

    length = len( linepoints )

    return linepoints
